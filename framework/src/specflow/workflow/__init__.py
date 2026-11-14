"""Evaluate seven gates without applying transitions or producing approvals."""
from .. import validation
from ..storage import (Fault, require, verify, identity, confined, read_json, fields,
                       version, text, strings)
from ..contracts import STATES
import re


def active(records):
    by_id = {x["id"]: x for x in records}
    require(len(by_id) == len(records), "RECORD_ID_DUPLICATE")
    superseded = set()
    for item in records:
        seen = {item["id"]}
        cursor = item
        while "supersedes" in cursor:
            ident = cursor["supersedes"]
            require(ident in by_id, "SUPERSESSION_REFERENCE_MISSING")
            require(ident not in seen, "SUPERSESSION_CYCLE")
            require(by_id[ident]["kind"] == item["kind"], "SUPERSESSION_KIND_MISMATCH")
            seen.add(ident)
            superseded.add(ident)
            cursor = by_id[ident]
    return [x for x in records if x["id"] not in superseded]


def implementation_target(ctx):
    return ctx["change"]["contractManifest"] + ctx["change"]["implementationManifest"]


def decision(ctx, kind):
    selected = [x for x in active(ctx["decisions"]) if x["kind"] == kind]
    require(selected, "HUMAN_DECISION_MISSING", 1)
    expected = ctx["change"]["contractManifest"]
    if kind == "final":
        expected = expected + ctx["change"]["implementationManifest"]
    outcomes = set()
    for item in selected:
        require(item["scope"] == {"projectId": ctx["project"]["projectId"],
                                  "changeId": ctx["change"]["changeId"],
                                  "revision": ctx["change"]["revision"]}, "DECISION_SCOPE_MISMATCH", 1)
        validation.target(item, expected)
        require(confined(ctx["root"], item["sourceRef"]).is_file(), "DECISION_SOURCE_MISSING", 1)
        outcomes.add(item["outcome"])
    require(len(outcomes) == 1, "CONFLICTING_DECISIONS", 1)
    require(outcomes == {"approved"}, "HUMAN_DECISION_REJECTED", 1)


def review(ctx, kind):
    selected = [x for x in ctx["reviews"] if x["kind"] == kind]
    require(selected, "TECHNICAL_REVIEW_MISSING", 1)
    expected = ctx["change"]["contractManifest"] if kind == "spec" else implementation_target(ctx)
    # Every referenced current review must be coherent; conflicting reviews cannot be ignored.
    for item in selected:
        validation.target(item, expected)
        for finding in item["findings"]:
            require(confined(ctx["root"], finding["source"]).is_file(), "REVIEW_SOURCE_MISSING", 1)
            require(not (finding["severity"] == "material" and finding["status"] == "open"), "MATERIAL_FINDING_OPEN", 1)


def _implementation(ctx):
    root, change = ctx["root"], ctx["change"]
    expected = change["implementationManifest"]
    technical_target = implementation_target(ctx)
    require(expected, "IMPLEMENTATION_MISSING", 1)
    verify(root, expected)
    plan = confined(root, (ctx["folder"] / "implementation-plan.md").relative_to(root).as_posix())
    require(plan.is_file() and plan.stat().st_size > 0, "IMPLEMENTATION_PLAN_MISSING", 1)
    require(ctx["coverages"], "COVERAGE_MISSING", 1)
    suite_refs = set()
    for item in ctx["evidences"]:
        if item["method"] == "functional" and item["expectedCode"] == item["actualCode"] == 0:
            validation.evidence(root, item, technical_target)
            suite_refs.update(item["artifactRefs"])
    if any(x["role"] == "source" for x in expected):
        require(suite_refs, "TEST_SUITE_EVIDENCE_MISSING", 1)
    for item in ctx["coverages"]:
        validation.coverage(root, item, technical_target)
        require(set(item["testEvidenceRefs"]) <= suite_refs, "TEST_SUITE_SCOPE_MISMATCH", 1)


def _closure(ctx):
    events = [x for x in ctx["phases"] if x["phase"] == "ARQUIVADA" and x["outcome"] == "completed"]
    require(events, "CLOSURE_RECEIPT_MISSING", 1)
    for item in events:
        validation.target(item, implementation_target(ctx))
        receipt = read_json(confined(ctx["root"], item["sourceRef"]))
        version(receipt, {"changeId", "archivePath", "systemRefs", "manifest", "commit"})
        require(receipt["changeId"] == ctx["change"]["changeId"], "CLOSURE_CHANGE_MISMATCH", 1)
        destination = confined(ctx["root"], receipt["archivePath"])
        require(destination.is_dir() and destination != ctx["folder"], "ARCHIVE_NOT_EFFECTIVE", 1)
        strings(receipt["systemRefs"], True)
        for ref in receipt["systemRefs"]:
            require(confined(ctx["root"], ref).is_file(), "SYSTEM_UPDATE_MISSING", 1)
        require(identity(receipt["manifest"]) == identity(ctx["change"]["implementationManifest"]), "CLOSURE_MANIFEST_STALE", 1)
        verify(ctx["root"], receipt["manifest"])
        if receipt["commit"] is not None:
            fields(receipt["commit"], {"location", "hash"})
            require(isinstance(receipt["commit"]["hash"], str)
                    and re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", receipt["commit"]["hash"]) is not None
                    and confined(ctx["root"], receipt["commit"]["location"]).exists(), "COMMIT_RECEIPT_INVALID")


def assess(ctx, requested):
    require(requested in STATES, "TARGET_STATE_INVALID")
    require(not ctx.get("draft"), "DRAFT_CONTRACT_INCOMPLETE", 1)
    root, change = ctx["root"], ctx["change"]
    verify(root, change["contractManifest"])
    level = STATES.index(requested)
    if level >= 1:
        review(ctx, "spec")
        decision(ctx, "spec")
    if level >= 2:
        _implementation(ctx)
    if level >= 3:
        review(ctx, "implementation")
    if level >= 4:
        validation.matrix(root, ctx["trace"], ctx["evidence_map"], implementation_target(ctx))
        require(ctx["securities"], "SECURITY_BINDING_MISSING", 1)
        for item in ctx["securities"]:
            validation.security(root, item, implementation_target(ctx), change["changeId"])
        for event in ctx["phases"]:
            if event["phase"] == "VALIDADA" and event["outcome"] != "completed":
                validation.target(event, implementation_target(ctx))
                require(confined(root, event["sourceRef"]).is_file(), "PHASE_SOURCE_MISSING", 1)
                raise Fault(1, "VALIDATION_NOT_EXECUTED" if event["outcome"] == "not_run" else "VALIDATION_FAILED")
    if level >= 5:
        require(ctx["handoffs"], "HUMAN_HANDOFF_MISSING", 1)
        for item in ctx["handoffs"]:
            validation.handoff(root, item, change["implementationManifest"], manual=True,
                               evidences=ctx["evidences"], target_manifest=implementation_target(ctx))
        decision(ctx, "final")
    if level >= 6:
        _closure(ctx)


def observed(ctx):
    if ctx.get("draft"):
        require(not ctx.get("change"), "DRAFT_CHANGE_CONFLICT", 1)
        return "RASCUNHO"
    achieved = None
    failure = None
    for state in STATES:
        try:
            assess(ctx, state)
            achieved = state
        except Fault as error:
            if error.code == 2:
                raise
            failure = error
            break
    claimed = ctx["change"]["claimedState"]
    if claimed == "REPROVADA" and failure and failure.reason in {"HUMAN_DECISION_REJECTED", "MATERIAL_FINDING_OPEN"}:
        return "REPROVADA"
    if claimed == "BLOQUEADA":
        events = [x for x in ctx["phases"] if x["outcome"] in {"failed", "not_run"}]
        require(events, "BLOCK_REASON_MISSING", 1)
        for item in events:
            validation.target(item, implementation_target(ctx))
            require(confined(ctx["root"], item["sourceRef"]).is_file(), "PHASE_SOURCE_MISSING", 1)
        return "BLOQUEADA"
    require(claimed == achieved, "CLAIMED_STATE_CONFLICT", 1)
    return achieved
