"""Synthetic consumers only. Their records are NOT real application approvals."""
from pathlib import Path
import json
from specflow.storage import capture, digest, dump
from specflow.policy import POLICY_DIGEST, POLICY_ID, POLICY_VERSION
from specflow.security import gate_result
from specflow.contracts import STATES

CHANGE = "00001-demo"


def put(root, ref, value):
    path = Path(root) / ref
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((dump(value) if not isinstance(value, str) else value).encode("utf-8"))
    return path


def base_record(ident, target, **kwargs):
    return {"schemaVersion": 1, "id": ident, "targetManifest": target, **kwargs}


def make(root, level=0, project_id="consumer-a"):
    root = Path(root)
    folder = f"specs/changes/{CHANGE}"
    put(root, ".specflow/project.json", {"schemaVersion": 1, "projectId": project_id,
        "policyId": POLICY_ID, "policyVersion": POLICY_VERSION, "policyDigest": POLICY_DIGEST,
        "changesPath": "specs/changes", "knowledgePath": "specs/knowledge"})
    contract = []
    for role, name in [("proposal", "proposal.md"), ("spec", "spec.md"), ("design", "DESIGN.md"), ("tasks", "tasks.md")]:
        ref = folder + "/" + name
        put(root, ref, f"# Synthetic {role}\nCA-01 T01\n")
        contract.extend(capture(root, [ref], role, "sha256-utf8-lf-v1"))
    change = {"schemaVersion": 1, "changeId": CHANGE, "revision": "r1", "claimedState": STATES[level],
              "contractManifest": contract, "implementationManifest": [], "traceabilityRef": folder + "/matrix.json"}
    for name in ["reviewRefs", "decisionRefs", "evidenceRefs", "coverageRefs", "securityRefs", "phaseExecutionRefs", "handoffRefs"]:
        change[name] = []
    def record(collection, name, value):
        ref = folder + "/" + name + ".json"
        put(root, ref, value)
        change[collection].append(ref)
        return ref
    put(root, "synthetic-human.txt", "Synthetic fixture actor, not an actual human approval or test.\n")
    def decision(kind, target):
        return base_record("decision-" + kind, target, kind=kind, actor="synthetic-fixture-only",
              occurredAt="2026-11-13T00:00:00+00:00", scope={"projectId": project_id, "changeId": CHANGE, "revision": "r1"},
              outcome="approved", rationale="Synthetic gate test; never real product acceptance", sourceRef="synthetic-human.txt")
    if level >= 1:
        record("reviewRefs", "spec-review", base_record("review-spec", contract, kind="spec", reviewer="synthetic", findings=[]))
        record("decisionRefs", "spec-decision", decision("spec", contract))
    if level >= 2:
        put(root, "apps/demo/main.py", "def add(a, b):\n    return a + b\n")
        put(root, "tests/test_demo.py", "# Synthetic fixture only\nassert 1 + 1 == 2\n")
        put(root, folder + "/implementation-plan.md", "# Synthetic plan\n")
        implementation = capture(root, ["apps/demo/main.py"], "source") + capture(root, ["tests/test_demo.py"], "test")
        change["implementationManifest"] = implementation
        technical_target = contract + implementation
        put(root, "suite.log", "Synthetic suite outcome for gate tests only.\n")
        put(root, "coverage-report.json", {"synthetic": True})
        record("evidenceRefs", "suite-evidence", base_record("suite", technical_target, criterionIds=["CA-01"],
            method="functional", command="synthetic-fixture-not-a-real-test-command", cwd=".", environment="synthetic",
            expectedCode=0, actualCode=0, outcome="passed", artifactRefs=["suite.log"], artifactManifest=capture(root, ["suite.log"], "evidence")))
        record("coverageRefs", "coverage", base_record("coverage", technical_target, scope=["apps/demo/main.py"], metric="lines",
            files=[{"path": "apps/demo/main.py", "covered": 2, "total": 2}], reportRefs=["coverage-report.json"],
            testEvidenceRefs=["suite.log"], exclusions=[], testManifest=capture(root, ["tests/test_demo.py"], "test"),
            artifactManifest=capture(root, ["coverage-report.json"], "report") + capture(root, ["suite.log"], "evidence")))
    if level >= 3:
        record("reviewRefs", "implementation-review", base_record("review-implementation", technical_target, kind="implementation", reviewer="synthetic", findings=[]))
    if level >= 4:
        put(root, "security.log", "Synthetic audit evidence for gate tests only.\n")
        audit_ref = folder + "/security-audit.json"
        put(root, audit_ref, {"schemaVersion": 1, "changeId": CHANGE, "revision": "r1",
            "review": {"skill": "security-audit", "reviewer": "synthetic-fixture-only", "status": "completed", "limitations": ["Synthetic only"]},
            "scope": [x["path"] for x in implementation], "artifacts": [{k: v for k, v in x.items() if k != "role"} for x in implementation],
            "findings": [], "checks": [{"id": "SEC-01", "method": "static", "expectedCode": 0, "actualCode": 0,
                                         "outcome": "passed", "evidenceRefs": ["security.log"]}]})
        gate_ref = folder + "/security-gate.json"
        put(root, gate_ref, gate_result(root, root / folder))
        record("securityRefs", "security-binding", base_record("security", technical_target, auditRef=audit_ref, gateRef=gate_ref,
            auditDigest=digest((root / audit_ref).read_bytes()), gateDigest=digest((root / gate_ref).read_bytes()),
            status="verificada", exitCode=0, findingRefs=[], evidenceManifest=capture(root, ["security.log"], "evidence")))
    if level >= 5:
        put(root, "quickstart.md", "# Synthetic quickstart\n")
        record("evidenceRefs", "manual-evidence", base_record("manual", technical_target, criterionIds=["M01"], method="manual",
            command="synthetic manual outcome, not real acceptance", cwd=".", environment="synthetic", expectedCode=0, actualCode=0,
            outcome="passed", artifactRefs=["synthetic-human.txt", "quickstart.md"],
            artifactManifest=capture(root, ["synthetic-human.txt", "quickstart.md"], "evidence")))
        record("handoffRefs", "handoff", base_record("handoff", technical_target, artifactManifest=implementation,
            quickstartRef="quickstart.md", scenarioIds=["M01"], outcomes=["passed"], actor="synthetic-fixture-only", sourceRef="synthetic-human.txt"))
        record("decisionRefs", "final-decision", decision("final", contract + implementation))
    if level >= 6:
        (root / "specs/archive" / CHANGE).mkdir(parents=True)
        put(root, "specs/system.md", "# Synthetic system update\n")
        put(root, "receipt.json", {"schemaVersion": 1, "changeId": CHANGE, "archivePath": "specs/archive/" + CHANGE,
              "systemRefs": ["specs/system.md"], "manifest": implementation, "commit": None})
        record("phaseExecutionRefs", "closure", base_record("closure", technical_target, phase="ARQUIVADA", outcome="completed",
               sourceRef="receipt.json", reason="Synthetic receipt, not an actual archive operation"))
    put(root, change["traceabilityRef"], {"schemaVersion": 1, "items": [{"requirementId": "RF-01", "acceptanceId": "CA-01",
        "taskIds": ["T01"], "artifactRefs": ["apps/demo/main.py"] if level >= 2 else [contract[0]["path"]],
        "evidenceIds": ["suite"] if level >= 2 else [], "requiredMethod": "functional"}]})
    path = put(root, folder + "/change.json", change)
    return path


def edit(path, mutate):
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    mutate(value)
    Path(path).write_text(dump(value), encoding="utf-8")


def snapshot(root):
    return {p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in Path(root).rglob("*") if p.is_file()}
