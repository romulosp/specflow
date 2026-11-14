"""Current artifacts, behavior evidence, traceability and coverage gates."""
from ..storage import require, text, verify, identity, bind, confined, digest, read_json
from ..security import audit


def target(record, expected):
    require(identity(record["targetManifest"]) == identity(expected), "TARGET_MANIFEST_STALE", 1)


def evidence(root, record, expected):
    target(record, expected)
    bind(root, record["artifactRefs"], record["artifactManifest"], "evidence")
    require(record["artifactRefs"] and record["outcome"] == "passed"
            and record["actualCode"] == record["expectedCode"], "EVIDENCE_NOT_PASSED", 1)


def matrix(root, trace, evidence_map, expected):
    for row in trace["items"]:
        require(row["evidenceIds"], "TRACEABILITY_UNCOVERED", 1)
        for ref in row["artifactRefs"]:
            require(confined(root, ref).is_file(), "TRACEABILITY_ARTIFACT_MISSING", 1)
        for ident in row["evidenceIds"]:
            require(ident in evidence_map, "EVIDENCE_ID_MISSING")
            record = evidence_map[ident]
            require(row["acceptanceId"] in record["criterionIds"], "CRITERION_UNCOVERED", 1)
            require(record["method"] == row["requiredMethod"], "EVIDENCE_METHOD_MISMATCH", 1)
            evidence(root, record, expected)


def coverage(root, record, expected):
    target(record, expected)
    verify(root, expected)
    source_paths = {x["path"] for x in expected if x["role"] == "source"}
    excluded = {x["path"] for x in record["exclusions"]}
    non_executable = {x["path"] for x in expected if x["role"] == "artifact"}
    require(not excluded & source_paths, "SOURCE_EXCLUSION_FORBIDDEN", 1)
    require(set(record["scope"]) == source_paths | excluded, "COVERAGE_SCOPE_MISMATCH", 1)
    require(len(excluded) == len(record["exclusions"]), "EXCLUSION_DUPLICATE")
    for row in record["exclusions"]:
        require(confined(root, row["sourceRef"]).is_file(), "EXCLUSION_SOURCE_MISSING", 1)
    require(excluded <= non_executable, "EXCLUSION_SCOPE_INVALID")
    require(source_paths or excluded, "COVERAGE_SCOPE_EMPTY", 1)
    paths = {x["path"] for x in record["files"]}
    require(paths == source_paths and not paths & excluded, "COVERAGE_FILES_UNCOVERED", 1)
    for row in record["files"]:
        require(row["total"] > 0 and 100 * row["covered"] >= 80 * row["total"], "COVERAGE_BELOW_FLOOR", 1)
    # Exclusions are only non-executable artifacts with explicit contractual justification.
    require(record["files"] or excluded == non_executable, "COVERAGE_EMPTY", 1)
    tests = {x["path"] for x in expected if x["role"] == "test"}
    require((tests or not source_paths) and tests == {x["path"] for x in record["testManifest"]}, "TEST_SCOPE_MISMATCH", 1)
    require(not source_paths or record["testEvidenceRefs"], "TEST_SUITE_EVIDENCE_MISSING", 1)
    bind(root, sorted(tests), record["testManifest"], "test")
    roles = {x: "report" for x in record["reportRefs"]}
    require(not set(record["reportRefs"]) & set(record["testEvidenceRefs"]), "EVIDENCE_ROLE_CONFLICT")
    roles.update({x: "evidence" for x in record["testEvidenceRefs"]})
    bind(root, list(roles), record["artifactManifest"], roles)


def security(root, record, expected, change_id):
    target(record, expected)
    audit_path, gate_path = (confined(root, record[k]) for k in ["auditRef", "gateRef"])
    require(audit_path.is_file() and gate_path.is_file(), "SECURITY_REPORT_MISSING", 1)
    require(digest(audit_path.read_bytes()) == record["auditDigest"]
            and digest(gate_path.read_bytes()) == record["gateDigest"], "SECURITY_BINDING_STALE", 1)
    report, gate = read_json(audit_path), read_json(gate_path)
    from ..storage import version, strings
    version(gate, {"changeId", "status", "validationAllowed", "exitCode", "reasons", "method", "limitations"})
    strings(gate["reasons"])
    strings(gate["limitations"])
    refs = audit(report, root, change_id)
    source_scope = {x["path"] for x in expected if x["role"] == "source"}
    require(source_scope <= set(report["scope"]), "SECURITY_SOURCE_SCOPE_UNCOVERED", 1)
    expected_sources = {x["path"]: x for x in expected}
    for entry in report["artifacts"]:
        require(entry["path"] in expected_sources, "SECURITY_SCOPE_EXTRA", 1)
        original = expected_sources[entry["path"]]
        require(entry["sha256"] == original["sha256"] and entry["digestProfile"] == original["digestProfile"], "SECURITY_TARGET_STALE", 1)
    require(type(gate.get("exitCode")) is int and gate.get("exitCode") == record["exitCode"] == 0
            and gate.get("status") == record["status"] == "verificada"
            and gate.get("validationAllowed") is True and gate.get("changeId") == change_id,
            "SECURITY_PENDING", 1)
    require(not {record["auditRef"], record["gateRef"]} & set(refs), "SECURITY_SELF_REFERENCE")
    require(set(record["findingRefs"]) <= set(refs), "SECURITY_FINDING_SCOPE_INVALID")
    bind(root, refs, record["evidenceManifest"], "evidence")


def handoff(root, record, expected, manual=False, evidences=(), target_manifest=None):
    target(record, expected if target_manifest is None else target_manifest)
    require(identity(record["artifactManifest"]) == identity(expected), "HANDOFF_BUILD_MISMATCH", 1)
    verify(root, record["artifactManifest"])
    require(confined(root, record["quickstartRef"]).is_file(), "QUICKSTART_MISSING", 1)
    if manual:
        require(record["outcomes"] and all(x == "passed" for x in record["outcomes"])
                and text(record["actor"]) and confined(root, record["sourceRef"]).is_file(), "MANUAL_TEST_PENDING", 1)
        scenarios, refs = set(), set()
        for item in evidences:
            if item["method"] == "manual" and set(item["criterionIds"]) & set(record["scenarioIds"]):
                evidence(root, item, expected if target_manifest is None else target_manifest)
                scenarios.update(item["criterionIds"])
                refs.update(item["artifactRefs"])
        require(set(record["scenarioIds"]) <= scenarios
                and {record["sourceRef"], record["quickstartRef"]} <= refs, "MANUAL_EVIDENCE_UNBOUND", 1)
