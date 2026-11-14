"""Recover a consumer's context with provenance and no persistent indexes."""
from pathlib import Path
import re
from .. import contracts
from ..policy import load_policy, POLICY_ID, POLICY_VERSION, POLICY_DIGEST, policy_bytes
from ..storage import (Fault, require, confined, read_json, digest, text)
from ..workflow import active, observed, assess

RECORDS = {"reviewRefs": ("reviews", contracts.review), "decisionRefs": ("decisions", contracts.decision),
           "evidenceRefs": ("evidences", contracts.evidence), "coverageRefs": ("coverages", contracts.coverage),
           "securityRefs": ("securities", contracts.security), "phaseExecutionRefs": ("phases", contracts.phase),
           "handoffRefs": ("handoffs", contracts.handoff)}


def _read(root, ref, validator):
    path = confined(root, ref)
    try:
        return validator(read_json(path, source=ref))
    except Fault as error:
        if error.source is None:
            error.source = ref
        raise


def read_project(root):
    root = Path(root).resolve()
    load_policy()
    project = _read(root, ".specflow/project.json", contracts.project)
    if project["policyId"] != POLICY_ID or project["policyVersion"] != POLICY_VERSION:
        raise Fault(2, "POLICY_VERSION_INVALID", ".specflow/project.json", "policyId-policyVersion")
    if project["policyDigest"] != POLICY_DIGEST:
        raise Fault(1, "PROJECT_POLICY_STALE", ".specflow/project.json", "policyDigest")
    copy = confined(root, ".specflow/policies/policy-v1.json")
    if copy.exists():
        require(digest(copy.read_bytes()) == POLICY_DIGEST, "CONSUMER_POLICY_STALE", 1)
    return project


def load(root, change_id):
    root = Path(root).resolve()
    contracts.ident(change_id)
    project = read_project(root)
    folder = confined(root, project["changesPath"] + "/" + change_id)
    require(folder.is_dir(), "CHANGE_MISSING")
    ctx = {"root": root, "folder": folder, "project": project, "draft": None, "change": None,
           "sources": [".specflow/project.json"], "knowledge": []}
    for key, _ in RECORDS.values():
        ctx[key] = []
    for filename, validator, key in [("draft.json", contracts.draft, "draft"), ("change.json", contracts.change, "change")]:
        path = confined(root, (folder / filename).relative_to(root).as_posix())
        if path.is_file():
            record = _read(root, path.relative_to(root).as_posix(), validator)
            require(record["changeId"] == change_id, "CHANGE_ID_MISMATCH")
            ctx[key] = record
            ctx["sources"].append(path.relative_to(root).as_posix())
    require(ctx["draft"] is not None or ctx["change"] is not None, "CHANGE_RECORD_MISSING")
    if ctx["draft"]:
        for ref in ctx["draft"]["documentRefs"].values():
            require(confined(root, ref).is_file(), "DRAFT_DOCUMENT_MISSING")
    if ctx["change"]:
        change = ctx["change"]
        for key, (collection, validator) in RECORDS.items():
            seen = set()
            for ref in change[key]:
                item = _read(root, ref, validator)
                require(item["id"] not in seen, "RECORD_ID_DUPLICATE")
                seen.add(item["id"])
                ctx[collection].append(item)
                ctx["sources"].append(ref)
        active(ctx["decisions"])
        ctx["trace"] = _read(root, change["traceabilityRef"], contracts.traceability)
        ctx["sources"].append(change["traceabilityRef"])
        ctx["evidence_map"] = {x["id"]: x for x in ctx["evidences"]}
        for row in ctx["trace"]["items"]:
            require(set(row["evidenceIds"]) <= ctx["evidence_map"].keys(), "EVIDENCE_ID_MISSING")
    knowledge_dir = confined(root, project["knowledgePath"])
    if knowledge_dir.is_dir():
        for path in sorted(knowledge_dir.glob("*.json")):
            ref = path.relative_to(root).as_posix()
            ctx["knowledge"].append(_read(root, ref, contracts.knowledge))
            ctx["sources"].append(ref)
    ctx["knowledge"] = active(ctx["knowledge"])
    for item in ctx["knowledge"]:
        for ref in item["sourceRefs"]:
            require(confined(root, ref).is_file(), "KNOWLEDGE_SOURCE_MISSING", 1)
    return ctx


def result(root, change_id, operation="context", requested=None):
    envelope = {"schemaVersion": 1, "operation": operation if isinstance(operation, str) and operation in {"context", "check", "evaluate"} else None,
                "projectId": None, "changeId": None, "observedState": None,
                "requestedState": requested if requested in contracts.STATES else None, "allowed": None if operation == "context" else False,
                "findings": [], "sources": [], "decisions": [], "lessons": [], "pending": [], "nextSteps": [],
                "limitations": ["Checks record consistency; does not authenticate people or prove evidence truth"], "exitCode": 0}
    try:
        require(operation in {"context", "check", "evaluate"}, "OPERATION_INVALID")
        if operation != "context":
            require(requested in contracts.STATES, "TARGET_STATE_INVALID")
        ctx = load(root, change_id)
        envelope["projectId"] = ctx["project"]["projectId"]
        envelope["changeId"] = change_id
        envelope["sources"] = sorted(set(ctx["sources"]))
        envelope["decisions"] = [{"id": x["id"], "kind": x["kind"], "outcome": x["outcome"]}
                                  for x in sorted(active(ctx["decisions"]), key=lambda x: x["id"])]
        envelope["lessons"] = [x for x in ctx["knowledge"] if x["kind"] == "lesson"]
        envelope["pending"] = [x for x in ctx["knowledge"] if x["kind"] == "pending"]
        state = reconciled(ctx)
        envelope["observedState"] = state
        if operation != "context":
            assess(ctx, requested)
            envelope["allowed"] = True
        else:
            if state in {"REPROVADA", "BLOQUEADA"}:
                raise Fault(1, "CURRENT_STATE_PENDING")
            if state != "RASCUNHO" and state != contracts.STATES[-1]:
                try:
                    assess(ctx, contracts.STATES[contracts.STATES.index(state) + 1])
                except Fault as error:
                    envelope["nextSteps"] = [error.reason]
            else:
                envelope["nextSteps"] = ["COMPLETE_SPECIFICATION"] if state == "RASCUNHO" else []
    except (Fault, OSError, UnicodeError, TypeError, KeyError, AttributeError, RuntimeError) as error:
        code = error.code if isinstance(error, Fault) else 2
        reason = error.reason if isinstance(error, Fault) else "INPUT_INVALID"
        envelope["exitCode"] = code
        envelope["lessons"] = []
        envelope["pending"] = []
        envelope["findings"] = [{"id": reason, "severity": "material", "source": error.location() if isinstance(error, Fault) else None,
                                  "method": "structural", "reason": reason}]
        if code == 1:
            if reason in {"CLAIMED_STATE_CONFLICT", "DRAFT_CHANGE_CONFLICT", "STATUS_CONFLICT", "CONFLICTING_DECISIONS"}:
                envelope["observedState"] = "INDETERMINADO"
            envelope["pending"].append({"id": reason})
    return envelope


def reconciled(ctx):
    state = observed(ctx)
    marker = confined(ctx["root"], (ctx["folder"] / "STATUS.md").relative_to(ctx["root"]).as_posix())
    if marker.is_file():
        content = marker.read_text(encoding="utf-8-sig")
        claims = re.findall(r"^Status:\s*`?([A-Z_]+)`?\s*$", content, re.M)
        require(not claims or claims[0] == state, "STATUS_CONFLICT", 1)
    return state
