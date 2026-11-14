"""Closed domain record validators. This is deliberately not JSON Schema."""
import re
from datetime import datetime
from ..storage import (fields, version, require, text, strings, portable, manifest,
                       hex_digest)

STATES = ("EM_REVISAO_SPEC", "SPEC_APROVADA", "IMPLEMENTADA", "IMPLEMENTACAO_APROVADA",
          "VALIDADA", "APROVADA", "ARQUIVADA")
METHODS = {"structural", "functional", "manual"}
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}")


def ident(value):
    require(isinstance(value, str) and ID.fullmatch(value) is not None, "ID_INVALID")


def refs(value, nonempty=False):
    for ref in strings(value, nonempty):
        portable(ref)
    return value


def enum(value, choices):
    require(isinstance(value, str) and value in choices, "ENUM_INVALID")


def project(value):
    version(value, {"projectId", "policyId", "policyVersion", "policyDigest", "changesPath", "knowledgePath"})
    ident(value["projectId"])
    require(text(value["policyId"]) and text(value["policyVersion"]), "POLICY_INVALID")
    hex_digest(value["policyDigest"])
    refs([value["changesPath"], value["knowledgePath"]])
    a, b = value["changesPath"], value["knowledgePath"]
    require(a != b and not a.startswith(b + "/") and not b.startswith(a + "/"), "PROJECT_PATH_OVERLAP")
    return value


def draft(value):
    version(value, {"changeId", "revision", "objective", "documentRefs"})
    ident(value["changeId"])
    require(text(value["revision"]) and text(value["objective"]), "DRAFT_INVALID")
    fields(value["documentRefs"], {"proposal", "spec", "design", "tasks", "validation", "memory"})
    refs(list(value["documentRefs"].values()), True)
    return value


def change(value):
    required = {"changeId", "revision", "claimedState", "contractManifest", "implementationManifest",
                "reviewRefs", "evidenceRefs", "decisionRefs", "traceabilityRef", "coverageRefs",
                "securityRefs", "phaseExecutionRefs", "handoffRefs"}
    version(value, required)
    ident(value["changeId"])
    require(text(value["revision"]), "REVISION_INVALID")
    enum(value["claimedState"], {*STATES, "REPROVADA", "BLOQUEADA"})
    manifest(value["contractManifest"], contract=True)
    manifest(value["implementationManifest"])
    for key in required:
        if key.endswith("Refs"):
            refs(value[key])
    portable(value["traceabilityRef"])
    return value


def _base(value, required, optional=()):
    version(value, {"id", "targetManifest", *required}, optional)
    ident(value["id"])
    manifest(value["targetManifest"])


def review(value):
    _base(value, {"kind", "reviewer", "findings"})
    enum(value["kind"], {"spec", "implementation"})
    require(text(value["reviewer"]) and isinstance(value["findings"], list), "REVIEW_INVALID")
    seen = set()
    for item in value["findings"]:
        fields(item, {"id", "severity", "status", "source"})
        ident(item["id"])
        require(item["id"] not in seen, "FINDING_DUPLICATE")
        seen.add(item["id"])
        enum(item["severity"], {"info", "minor", "material"})
        enum(item["status"], {"open", "resolved"})
        portable(item["source"])
    return value


def decision(value):
    _base(value, {"kind", "actor", "occurredAt", "scope", "outcome", "rationale", "sourceRef"}, {"supersedes"})
    enum(value["kind"], {"spec", "final"})
    enum(value["outcome"], {"approved", "rejected"})
    require(text(value["actor"]) and text(value["rationale"]), "DECISION_INVALID")
    require(isinstance(value["occurredAt"], str), "DATE_INVALID")
    try:
        require(datetime.fromisoformat(value["occurredAt"]).utcoffset() is not None, "DATE_OFFSET_REQUIRED")
    except ValueError as error:
        from ..storage import Fault
        raise Fault(2, "DATE_INVALID") from error
    fields(value["scope"], {"projectId", "changeId", "revision"})
    ident(value["scope"]["projectId"])
    ident(value["scope"]["changeId"])
    require(text(value["scope"]["revision"]), "SCOPE_INVALID")
    portable(value["sourceRef"])
    if "supersedes" in value:
        ident(value["supersedes"])
    return value


def evidence(value):
    _base(value, {"criterionIds", "method", "command", "cwd", "environment", "expectedCode",
                  "actualCode", "outcome", "artifactRefs", "artifactManifest"})
    strings(value["criterionIds"], True)
    enum(value["method"], METHODS)
    enum(value["outcome"], {"passed", "failed", "not_run"})
    require(text(value["command"]) and text(value["environment"]), "EVIDENCE_INVALID")
    require(value["cwd"] == "." or text(value["cwd"]), "CWD_INVALID")
    if value["cwd"] != ".":
        portable(value["cwd"])
    require(type(value["expectedCode"]) is int and (value["actualCode"] is None or type(value["actualCode"]) is int), "EXIT_CODE_INVALID")
    refs(value["artifactRefs"])
    manifest(value["artifactManifest"])
    return value


def traceability(value):
    version(value, {"items"})
    require(isinstance(value["items"], list) and value["items"], "TRACEABILITY_EMPTY")
    seen = set()
    for item in value["items"]:
        fields(item, {"requirementId", "acceptanceId", "taskIds", "artifactRefs", "evidenceIds", "requiredMethod"})
        require(text(item["requirementId"]) and text(item["acceptanceId"]), "TRACEABILITY_INVALID")
        key = (item["requirementId"], item["acceptanceId"])
        require(key not in seen, "TRACEABILITY_DUPLICATE")
        seen.add(key)
        strings(item["taskIds"], True)
        refs(item["artifactRefs"], True)
        strings(item["evidenceIds"])
        enum(item["requiredMethod"], METHODS)
    return value


def coverage(value):
    _base(value, {"scope", "metric", "files", "reportRefs", "testEvidenceRefs", "exclusions", "testManifest", "artifactManifest"})
    refs(value["scope"], True)
    enum(value["metric"], {"lines", "statements"})
    require(isinstance(value["files"], list) and isinstance(value["exclusions"], list), "COVERAGE_INVALID")
    seen = set()
    for item in value["files"]:
        fields(item, {"path", "covered", "total"})
        portable(item["path"])
        require(item["path"].casefold() not in seen, "COVERAGE_DUPLICATE")
        seen.add(item["path"].casefold())
        a, b = item["covered"], item["total"]
        require(type(a) is int and type(b) is int and 0 <= a <= b, "COVERAGE_COUNTER_INVALID")
    for item in value["exclusions"]:
        fields(item, {"path", "reason", "sourceRef"})
        portable(item["path"])
        portable(item["sourceRef"])
        require(text(item["reason"]), "EXCLUSION_INVALID")
    refs(value["reportRefs"], True)
    refs(value["testEvidenceRefs"])
    manifest(value["testManifest"])
    manifest(value["artifactManifest"])
    return value


def security(value):
    _base(value, {"auditRef", "gateRef", "auditDigest", "gateDigest", "exitCode", "status", "findingRefs", "evidenceManifest"})
    refs([value["auditRef"], value["gateRef"]])
    hex_digest(value["auditDigest"])
    hex_digest(value["gateDigest"])
    require(type(value["exitCode"]) is int, "EXIT_CODE_INVALID")
    enum(value["status"], {"verificada", "pendente"})
    refs(value["findingRefs"])
    manifest(value["evidenceManifest"])
    return value


def phase(value):
    _base(value, {"phase", "outcome", "sourceRef", "reason"})
    enum(value["phase"], STATES)
    enum(value["outcome"], {"completed", "failed", "not_run"})
    portable(value["sourceRef"])
    require(text(value["reason"]), "PHASE_REASON_INVALID")
    return value


def handoff(value):
    _base(value, {"artifactManifest", "quickstartRef", "scenarioIds", "outcomes", "actor", "sourceRef"})
    manifest(value["artifactManifest"])
    portable(value["quickstartRef"])
    strings(value["scenarioIds"], True)
    require(len(set(value["scenarioIds"])) == len(value["scenarioIds"]), "SCENARIO_DUPLICATE")
    require(isinstance(value["outcomes"], list) and len(value["outcomes"]) == len(value["scenarioIds"]), "HANDOFF_INVALID")
    for outcome in value["outcomes"]:
        enum(outcome, {"passed", "failed", "not_run"})
    require(isinstance(value["actor"], str) and isinstance(value["sourceRef"], str), "HANDOFF_INVALID")
    if any(x != "not_run" for x in value["outcomes"]):
        require(text(value["actor"]) and text(value["sourceRef"]), "HANDOFF_ACTOR_REQUIRED")
        portable(value["sourceRef"])
    return value


def knowledge(value):
    version(value, {"id", "kind", "sourceRefs"}, {"alternatives", "reason", "status", "supersedes", "incident", "action", "applicability", "impact", "nextAction"})
    ident(value["id"])
    enum(value["kind"], {"decision", "lesson", "pending"})
    refs(value["sourceRefs"], True)
    required = {"decision": {"alternatives", "reason", "status"},
                "lesson": {"incident", "action", "applicability"}, "pending": {"impact", "nextAction"}}[value["kind"]]
    require(required <= value.keys(), "KNOWLEDGE_INCOMPLETE")
    for key in required:
        strings(value[key], True) if key == "alternatives" else require(text(value[key]), "KNOWLEDGE_INVALID")
    if "supersedes" in value:
        ident(value["supersedes"])
    return value
