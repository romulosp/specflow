"""Security evidence gate. No scanner and no execution of evidence commands."""
from .storage import (version, fields, require, text, strings, portable, manifest,
                      verify, confined, read_json, digest)


def audit(report, root, change_id):
    version(report, {"changeId", "revision", "review", "scope", "artifacts", "findings", "checks"})
    require(text(report["revision"]) and text(report["changeId"]), "AUDIT_ID_INVALID")
    require(report["changeId"] == change_id, "AUDIT_CHANGE_MISMATCH", 1)
    review = report["review"]
    fields(review, {"skill", "reviewer", "status", "limitations"})
    require(review["skill"] == "security-audit" and isinstance(review["status"], str)
            and review["status"] in {"completed", "pending"}, "AUDIT_REVIEW_INVALID")
    strings(review["limitations"])
    require(text(review["reviewer"]) and review["status"] == "completed", "AUDIT_REVIEW_PENDING", 1)
    strings(report["scope"], True)
    require(len(set(report["scope"])) == len(report["scope"]), "AUDIT_SCOPE_DUPLICATE")
    require(isinstance(report["artifacts"], list), "AUDIT_ARTIFACT_INVALID")
    entries = []
    for entry in report["artifacts"]:
        fields(entry, {"path", "digestProfile", "sha256"})
        entries.append({**entry, "role": "source"})
    manifest(entries)
    require(set(report["scope"]) == {x["path"] for x in entries}, "AUDIT_SCOPE_UNCOVERED", 1)
    require(isinstance(report["findings"], list) and isinstance(report["checks"], list), "AUDIT_LIST_INVALID")
    reference_set, reasons = set(), []
    for name, keys in [("findings", {"id", "severity", "status", "evidenceRefs"}),
                       ("checks", {"id", "method", "expectedCode", "actualCode", "outcome", "evidenceRefs"})]:
        seen = set()
        for row in report[name]:
            fields(row, keys)
            require(text(row["id"]) and row["id"] not in seen, "AUDIT_ID_DUPLICATE")
            seen.add(row["id"])
            strings(row["evidenceRefs"])
            for ref in row["evidenceRefs"]:
                portable(ref)
                require(confined(root, ref).is_file(), "AUDIT_EVIDENCE_MISSING", 1)
                reference_set.add(ref)
            if not row["evidenceRefs"]:
                reasons.append("AUDIT_EVIDENCE_INCOMPLETE")
            if name == "findings":
                require(isinstance(row["severity"], str) and row["severity"] in {"critical", "high", "medium", "low", "info"}
                        and isinstance(row["status"], str) and row["status"] in {"open", "resolved"}, "AUDIT_FINDING_INVALID")
                if row["status"] == "open":
                    reasons.append("AUDIT_FINDING_OPEN")
            else:
                require(isinstance(row["method"], str) and row["method"] in {"static", "automated", "manual"}
                        and isinstance(row["outcome"], str) and row["outcome"] in {"passed", "failed", "not_run"}, "AUDIT_CHECK_INVALID")
                require(type(row["expectedCode"]) is int
                        and (row["actualCode"] is None or type(row["actualCode"]) is int), "AUDIT_CODE_INVALID")
                if row["outcome"] != "passed" or row["actualCode"] != row["expectedCode"]:
                    reasons.append("AUDIT_CHECK_PENDING")
    verify(root, entries)
    require(report["checks"] and not reasons, sorted(reasons)[0] if reasons else "AUDIT_CHECKS_MISSING", 1)
    return sorted(reference_set)


def security_path(root, folder, filename):
    """Select an existing legacy path or the organized destination, never both."""
    root = root.resolve()
    folder = folder.resolve()
    require(folder.is_relative_to(root), "PATH_ESCAPE")
    legacy = (folder / filename).relative_to(root).as_posix()
    organized = (folder / "evidence" / "security" / filename).relative_to(root).as_posix()
    old = confined(root, legacy, writing=True)
    new = confined(root, organized, writing=True)
    require(not (old.exists() and new.exists()), "SECURITY_PATH_CONFLICT", 1)
    return legacy if old.exists() else organized


def gate_result(root, folder):
    """Compute only: writing is performed by the shared transaction layer."""
    from .storage import Fault
    root = root.resolve()
    folder = folder.resolve()
    require(folder.is_relative_to(root.resolve()), "PATH_ESCAPE")
    code, reasons = 0, []
    try:
        ref = security_path(root, folder, "security-audit.json")
        path = confined(root, ref)
        require(path.is_file(), "AUDIT_REPORT_MISSING", 1)
        audit(read_json(path), root, folder.name)
    except Fault as error:
        code, reasons = error.code, [error.reason]
    return {"schemaVersion": 1, "changeId": folder.name, "status": "verificada" if code == 0 else "pendente",
            "validationAllowed": code == 0, "exitCode": code, "reasons": reasons,
            "method": "Evidence gate; actual security analysis remains mandatory",
            "limitations": ["Does not authenticate reviewer or execute audit commands",
                            "Evidence bindings and implementation review are required separately"]}
