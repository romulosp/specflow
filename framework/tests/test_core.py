import contextlib
import copy
import io
from pathlib import Path
import tempfile
import unittest
import runpy
import warnings
from unittest.mock import patch

from specflow import contracts, security, validation, policy
from specflow.storage import (Fault, digest, decode_json, portable, confined, manifest, verify, capture, bind, read_json, dump)
from specflow.memory import load, result
from specflow.workflow import assess, active
from specflow.harness import main
from support import CHANGE, make, put, edit, snapshot, base_record


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_all_gates_read_only_deterministic_and_two_consumers(self):
        for level, state in enumerate(contracts.STATES):
            with self.subTest(state=state):
                root = self.root / str(level)
                make(root, level)
                before = snapshot(root)
                a = result(root, CHANGE)
                self.assertEqual((a["exitCode"], a["observedState"]), (0, state), a)
                self.assertEqual(a, result(root, CHANGE))
                b = result(root, CHANGE, "evaluate", state)
                self.assertEqual((b["exitCode"], b["allowed"]), (0, True), b)
                self.assertEqual(before, snapshot(root))
        a, b = self.root / "A", self.root / "B"
        make(a, 1, "consumer-a")
        make(b, 1, "consumer-b")
        put(a, "specs/knowledge/lesson.json", {"schemaVersion": 1, "id": "lesson", "kind": "lesson", "sourceRefs": ["synthetic-human.txt"],
              "incident": "private-marker-A", "action": "keep local", "applicability": "A only"})
        self.assertIn("private-marker-A", dump(result(a, CHANGE)))
        self.assertNotIn("private-marker-A", dump(result(b, CHANGE)))

    def test_missing_human_never_advanced_by_filename_or_checkbox(self):
        make(self.root)
        put(self.root, "APROVADA.md", "[x] approved\n")
        out = result(self.root, CHANGE, "evaluate", "IMPLEMENTADA")
        self.assertEqual((out["exitCode"], out["allowed"]), (1, False))
        self.assertEqual(result(self.root, CHANGE)["observedState"], "EM_REVISAO_SPEC")

    def test_digest_profiles(self):
        variants = [b"a\nb\n", b"a\r\nb\r\n", b"a\rb\r", b"\xef\xbb\xbfa\nb\n"]
        self.assertEqual(len({digest(v, "sha256-utf8-lf-v1") for v in variants}), 1)
        for v in [b"a\nb", b"a \nb\n", b"a\nc\n"]:
            self.assertNotEqual(digest(v, "sha256-utf8-lf-v1"), digest(variants[0], "sha256-utf8-lf-v1"))
        self.assertNotEqual(digest(variants[0]), digest(variants[1]))
        for raw, profile in [(b"\xff", "sha256-utf8-lf-v1"), (b"a", "unknown")]:
            with self.assertRaises(Fault):
                digest(raw, profile)

    def test_strict_json_and_paths(self):
        for raw in [b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":Infinity}', b"\xff", b"{"]:
            with self.subTest(raw=raw), self.assertRaises(Fault):
                decode_json(raw)
        for value in ["../escape", "/absolute", "C:/secret", "\\server\\share", "a//b", "./x", "CON.txt", "aux", "a.", "a ", "a|b", "x\x00", None]:
            with self.subTest(value=value), self.assertRaises(Fault):
                portable(value)
        self.assertEqual(portable(".specflow/policy.json"), [".specflow", "policy.json"])
        with self.assertRaises(Fault):
            read_json(self.root / "missing")
        with patch("specflow.storage.link", return_value=True), self.assertRaises(Fault):
            confined(self.root, "x", writing=True)

    def test_input_diagnostic_names_source_without_echoing_unknown_keys(self):
        make(self.root)
        path = self.root / ".specflow/project.json"
        edit(path, lambda d: d.update({"synthetic-secret-key": "synthetic-secret-value"}))
        out = result(self.root, CHANGE)
        self.assertEqual(out["exitCode"], 2)
        self.assertEqual(out["findings"][0]["source"], ".specflow/project.json#unknown-field")
        self.assertNotIn("synthetic-secret", dump(out))

    def test_actual_links_cannot_escape(self):
        outside = self.root / "outside"
        outside.mkdir()
        root = self.root / "project"
        root.mkdir()
        try:
            (root / "link").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("OS does not permit symlink creation")
        with self.assertRaises(Fault):
            confined(root, "link/value")

    def test_policy_is_pinned(self):
        make(self.root, 1)
        for key, value, code in [("policyDigest", "0" * 64, 1), ("policyVersion", "99", 2), ("schemaVersion", True, 2), ("knowledgePath", "specs/changes", 2)]:
            path = self.root / ".specflow/project.json"
            old = path.read_bytes()
            edit(path, lambda d: d.update({key: value}))
            self.assertEqual(result(self.root, CHANGE)["exitCode"], code)
            path.write_bytes(old)
        put(self.root, ".specflow/policies/policy-v1.json", "{}")
        self.assertEqual(result(self.root, CHANGE)["exitCode"], 1)
        with patch("specflow.policy.policy_bytes", return_value=policy.policy_bytes() + b" "), self.assertRaises(Fault):
            policy.load_policy()

    def test_status_and_declared_state_conflicts(self):
        path = make(self.root, 1)
        edit(path, lambda d: d.update(claimedState="EM_REVISAO_SPEC"))
        out = result(self.root, CHANGE)
        self.assertEqual((out["exitCode"], out["observedState"]), (1, "INDETERMINADO"))
        edit(path, lambda d: d.update(claimedState="SPEC_APROVADA"))
        put(self.root, f"specs/changes/{CHANGE}/STATUS.md", "Status: IMPLEMENTADA\n")
        self.assertEqual(result(self.root, CHANGE)["observedState"], "INDETERMINADO")

    def test_contract_change_and_scope_invalidate_approval(self):
        path = make(self.root, 1)
        put(self.root, f"specs/changes/{CHANGE}/spec.md", "changed content\n")
        self.assertEqual(result(self.root, CHANGE, "check", "SPEC_APROVADA")["exitCode"], 1)
        make(self.root, 1)
        decision = self.root / f"specs/changes/{CHANGE}/spec-decision.json"
        edit(decision, lambda d: d["scope"].update(projectId="consumer-b"))
        with self.assertRaises(Fault) as raised:
            assess(load(self.root, CHANGE), "SPEC_APROVADA")
        self.assertEqual(raised.exception.reason, "DECISION_SCOPE_MISMATCH")

    def test_new_contract_cannot_reuse_old_implementation_evidence(self):
        path = make(self.root, 3)
        change = read_json(path)
        put(self.root, f"specs/changes/{CHANGE}/spec.md", "New contract content\n")
        changed = capture(self.root, [f"specs/changes/{CHANGE}/spec.md"], "spec", "sha256-utf8-lf-v1")[0]
        change["contractManifest"] = [changed if x["role"] == "spec" else x for x in change["contractManifest"]]
        put(self.root, path.relative_to(self.root).as_posix(), change)
        for name in ["spec-decision.json", "spec-review.json"]:
            edit(path.parent / name, lambda d: d.update(targetManifest=change["contractManifest"]))
        # Even with fresh SPEC decision/review, old suite/coverage/review cannot carry over.
        with self.assertRaises(Fault) as error:
            assess(load(self.root, CHANGE), "IMPLEMENTADA")
        self.assertEqual(error.exception.reason, "TARGET_MANIFEST_STALE")

    def test_manual_source_and_quickstart_bytes_are_bound(self):
        for ref in ["synthetic-human.txt", "quickstart.md"]:
            make(self.root, 5)
            put(self.root, ref, "changed after recorded manual result")
            self.assertEqual(result(self.root, CHANGE, "check", "APROVADA")["exitCode"], 1)

    def test_supersession_and_human_rejection(self):
        path = make(self.root, 1)
        ctx = load(self.root, CHANGE)
        old = ctx["decisions"][0]
        new = {**old, "id": "new", "supersedes": old["id"], "outcome": "rejected"}
        self.assertEqual(active([old, new]), [new])
        for records in [[new], [old, {**new, "supersedes": "new"}], [old, old]]:
            with self.assertRaises(Fault):
                active(records)
        old["supersedes"] = "new"
        with self.assertRaises(Fault):
            active([old, new])
        edit(self.root / f"specs/changes/{CHANGE}/spec-decision.json", lambda d: d.update(outcome="rejected"))
        edit(path, lambda d: d.update(claimedState="REPROVADA"))
        self.assertEqual(result(self.root, CHANGE)["observedState"], "REPROVADA")

    def test_draft_and_conflicting_records(self):
        path = make(self.root)
        change = read_json(path)
        refs = {x["role"]: x["path"] for x in change["contractManifest"]}
        refs.update(validation=f"specs/changes/{CHANGE}/validation.md", memory=f"specs/changes/{CHANGE}/AGENTS-MEMORY.md")
        put(self.root, refs["validation"], "pending")
        put(self.root, refs["memory"], "pending")
        draft = {"schemaVersion": 1, "changeId": CHANGE, "revision": "r1", "objective": "Synthetic", "documentRefs": refs}
        put(self.root, f"specs/changes/{CHANGE}/draft.json", draft)
        self.assertEqual(result(self.root, CHANGE)["observedState"], "INDETERMINADO")
        path.unlink()
        self.assertEqual((result(self.root, CHANGE)["exitCode"], result(self.root, CHANGE)["observedState"]), (0, "RASCUNHO"))
        self.assertEqual(result(self.root, CHANGE, "evaluate", "SPEC_APROVADA")["exitCode"], 1)

    def test_traceability_methods_and_missing_ids(self):
        path = make(self.root, 4)
        matrix = self.root / f"specs/changes/{CHANGE}/matrix.json"
        for value, code in [("structural", 1), ("manual", 1), ("unknown", 2), (None, 2)]:
            edit(matrix, lambda d: d["items"][0].update(requiredMethod=value))
            self.assertEqual(result(self.root, CHANGE, "check", "VALIDADA")["exitCode"], code)
        edit(matrix, lambda d: d["items"][0].update(requiredMethod="functional", evidenceIds=["missing"]))
        self.assertEqual(result(self.root, CHANGE)["exitCode"], 2)

    def test_coverage_floor_exact_and_no_zero_success(self):
        make(self.root, 2)
        path = self.root / f"specs/changes/{CHANGE}/coverage.json"
        for a, b, code in [(7999, 10000, 1), (80, 100, 0), (90, 100, 0), (100, 100, 0), (0, 0, 1), (True, 1, 2), (2, 1, 2)]:
            edit(path, lambda d: d["files"][0].update(covered=a, total=b))
            self.assertEqual(result(self.root, CHANGE, "evaluate", "IMPLEMENTADA")["exitCode"], code)

    def test_changed_test_log_report_or_source_invalidates(self):
        for ref in ["tests/test_demo.py", "suite.log", "coverage-report.json", "apps/demo/main.py"]:
            with self.subTest(ref=ref):
                make(self.root, 2)
                put(self.root, ref, "changed\n")
                self.assertEqual(result(self.root, CHANGE, "check", "IMPLEMENTADA")["exitCode"], 1)

    def test_security_all_severities_pending_and_no_command_execution(self):
        for severity in ["critical", "high", "medium", "low", "info"]:
            make(self.root, 4)
            path = self.root / f"specs/changes/{CHANGE}/security-audit.json"
            edit(path, lambda d: d["findings"].append({"id": "F1", "severity": severity, "status": "open", "evidenceRefs": ["security.log"]}))
            with patch("subprocess.run", side_effect=AssertionError("must not execute")):
                gate = security.gate_result(self.root, path.parent)
            self.assertEqual((gate["exitCode"], gate["validationAllowed"]), (1, False))
        make(self.root, 4)
        put(self.root, "security.log", "changed")
        self.assertEqual(result(self.root, CHANGE, "check", "VALIDADA")["exitCode"], 1)
        path.unlink()
        self.assertEqual(security.gate_result(self.root, path.parent)["exitCode"], 1)

    def test_manual_and_omission_never_approve(self):
        path = make(self.root, 5)
        edit(self.root / f"specs/changes/{CHANGE}/handoff.json", lambda d: d.update(outcomes=["not_run"]))
        self.assertEqual(result(self.root, CHANGE, "check", "APROVADA")["exitCode"], 1)
        make(self.root, 4)
        change = read_json(path)
        event = base_record("skip", change["contractManifest"] + change["implementationManifest"], phase="VALIDADA", outcome="not_run",
                            sourceRef="synthetic-human.txt", reason="Synthetic explicit omission")
        put(self.root, "skip.json", event)
        edit(path, lambda d: d["phaseExecutionRefs"].append("skip.json"))
        self.assertEqual(result(self.root, CHANGE, "evaluate", "VALIDADA")["exitCode"], 1)
        edit(path, lambda d: d.update(claimedState="BLOQUEADA"))
        self.assertEqual(result(self.root, CHANGE)["observedState"], "BLOQUEADA")

    def test_strict_records_mutations(self):
        path = make(self.root, 5)
        ctx = load(self.root, CHANGE)
        samples = [(contracts.project, ctx["project"]), (contracts.change, ctx["change"]),
                   (contracts.review, ctx["reviews"][0]), (contracts.decision, ctx["decisions"][0]),
                   (contracts.evidence, ctx["evidences"][0]), (contracts.traceability, ctx["trace"]),
                   (contracts.coverage, ctx["coverages"][0]), (contracts.security, ctx["securities"][0]),
                   (contracts.handoff, ctx["handoffs"][0])]
        for validator, original in samples:
            for edit_value in [lambda d: d.update(extra=True), lambda d: d.update(schemaVersion=True), lambda d: d.pop(next(k for k in d if k != "schemaVersion"))]:
                value = copy.deepcopy(original)
                edit_value(value)
                with self.subTest(validator=validator.__name__), self.assertRaises(Fault):
                    validator(value)
        decision = copy.deepcopy(ctx["decisions"][0])
        for timestamp in ["bad", "2026-11-13T00:00:00", None]:
            decision["occurredAt"] = timestamp
            with self.assertRaises(Fault):
                contracts.decision(decision)

    def test_manifest_invariants_and_errors(self):
        make(self.root)
        entries = capture(self.root, ["synthetic-human.txt"], "evidence")
        for invalid in [entries + entries, [{**entries[0], "sha256": "bad"}], [{**entries[0], "digestProfile": "bad"}]]:
            with self.assertRaises(Fault):
                manifest(invalid)
        with self.assertRaises(Fault):
            manifest(entries, contract=True)
        with self.assertRaises(Fault):
            bind(self.root, [], entries, "evidence")
        with self.assertRaises(Fault):
            bind(self.root, ["synthetic-human.txt"], entries, "report")
        (self.root / "synthetic-human.txt").unlink()
        with self.assertRaises(Fault) as error:
            verify(self.root, entries)
        self.assertEqual(error.exception.code, 1)

    def test_harness_and_redacted_errors(self):
        make(self.root, 1)
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(main(["context", "--project", str(self.root), "--change", CHANGE]), 0)
        self.assertIn('"observedState": "SPEC_APROVADA"', stdout.getvalue())
        self.assertEqual(result(self.root, CHANGE, "check", "INVALID")["exitCode"], 2)
        self.assertEqual(result(self.root, "../private-secret")["exitCode"], 2)
        self.assertNotIn("private-secret", dump(result(self.root, "../private-secret"))[dump(result(self.root, "../private-secret")).find('"findings"'):])

    def test_module_entrypoint(self):
        make(self.root, 1)
        with patch("sys.argv", ["specflow", "context", "--project", str(self.root), "--change", CHANGE]), contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as raised:
            runpy.run_module("specflow", run_name="__main__")
        self.assertEqual(raised.exception.code, 0)

    def test_harness_invalid_arguments_do_not_echo_values(self):
        with contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(main(["unknown", "synthetic-secret"]), 2)
        self.assertNotIn("synthetic-secret", stdout.getvalue())
        with warnings.catch_warnings(), patch("sys.argv", ["core", "unknown"]), contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as raised:
            warnings.simplefilter("ignore", RuntimeWarning)
            runpy.run_module("specflow.harness", run_name="__main__")
        self.assertEqual(raised.exception.code, 2)

    def test_executable_source_cannot_be_excluded(self):
        make(self.root, 2)
        ctx = load(self.root, CHANGE)
        coverage = ctx["coverages"][0]
        coverage["files"] = []
        coverage["exclusions"] = [{"path": "apps/demo/main.py", "reason": "generated", "sourceRef": "synthetic-human.txt"}]
        with self.assertRaises(Fault) as error:
            validation.coverage(self.root, coverage, ctx["change"]["contractManifest"] + ctx["change"]["implementationManifest"])
        self.assertEqual(error.exception.reason, "SOURCE_EXCLUSION_FORBIDDEN")
