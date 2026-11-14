import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from specflow.cli import main, catalog
from specflow.consumer import initialize, new_change
from support import make, CHANGE, edit, put, snapshot


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve() / "project"

    def run_cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as stdout, contextlib.redirect_stderr(io.StringIO()) as stderr:
            code = main(list(args))
        return code, stdout.getvalue(), stderr.getvalue()

    def test_packaged_catalog_matches_every_editor_instruction(self):
        initialize(self.root, ["copilot", "codex"])
        installed = json.loads((self.root / "docs/comandos/comandos.json").read_text(encoding="utf-8"))
        conventions = (self.root / "specs/shared/process/evidence-conventions.md").read_text(encoding="utf-8")
        for destination in ("reviews/spec/", "reviews/implementation/", "decisions/spec/", "decisions/final/", "coverage/", "evidence/security/"):
            self.assertIn(destination, conventions)
        self.assertEqual({x["name"].removeprefix("specflow-"): x for x in installed["commands"]}, catalog())
        for item in installed["commands"]:
            for ref in [".agents/skills/" + item["name"] + "/SKILL.md",
                        ".github/prompts/" + item["name"] + ".prompt.md"]:
                content = (self.root / ref).read_text(encoding="utf-8")
                self.assertIn(item["description"], content)
                for step in item["steps"]:
                    self.assertIn(step, content)
            for step in item["steps"]:
                import re
                for helper in re.findall(r"specs/shared/process/helpers/[a-z-]+\.md", step):
                    self.assertTrue((self.root / helper).is_file(), helper)
            for alias in item.get("aliases", []):
                self.assertTrue((self.root / (".agents/skills/" + alias + "/SKILL.md")).is_file())
                self.assertTrue((self.root / (".github/prompts/" + alias + ".prompt.md")).is_file())

    def test_first_time_cli_flow_and_mixed_global_flag_positions(self):
        code, out, err = self.run_cli("--json", "init", str(self.root), "--integration", "copilot")
        self.assertEqual(code, 0, out)
        self.assertFalse(json.loads(out)["phaseExecuted"])
        code, out, _ = self.run_cli("doctor", "--project=" + str(self.root), "--json")
        self.assertEqual(code, 0, out)
        self.assertTrue(all(not x["configurationReady"] for x in json.loads(out)["resources"].values()))
        code, out, _ = self.run_cli("--project", str(self.root), "nova-change", "Demo", "--json")
        ident = json.loads(out)["changeId"]
        self.assertEqual(code, 0, out)
        for name in ["contexto", "context"]:
            code, out, _ = self.run_cli(name, "--project", str(self.root), "--change", ident, "--json")
            self.assertEqual((code, json.loads(out)["observedState"]), (0, "RASCUNHO"))
        for name in ["especificar", "esclarecer"]:
            code, out, _ = self.run_cli(name, "--change", ident, "--project", str(self.root), "--json")
            self.assertEqual(code, 0, out)
            self.assertFalse(json.loads(out)["phaseExecuted"])
        for name in ["planejar", "implementar", "teste-humano", "revisar-spec", "revisar-implementacao", "validar", "aprovar", "encerrar"]:
            code, out, _ = self.run_cli(name, "--change", ident, "--project", str(self.root), "--json")
            self.assertEqual(code, 1, out)
            self.assertFalse(json.loads(out)["phaseExecuted"])

    def test_phase_preconditions_and_read_only_handoffs(self):
        for name, level in [("revisar-spec", 0), ("planejar", 1), ("implementar", 2), ("teste-humano", 2),
                            ("revisar-implementacao", 2), ("aprovar", 5), ("encerrar", 5)]:
            root = self.root / name
            make(root, level)
            before = snapshot(root)
            code, out, _ = self.run_cli(name, "--project", str(root), "--change", CHANGE, "--json")
            self.assertEqual(code, 0, out)
            self.assertEqual(snapshot(root), before)
            self.assertEqual(json.loads(out)["localChecksExecuted"], [])
        root = self.root / "missing-plan"
        make(root, 1)
        self.assertEqual(self.run_cli("implementar", "--project", str(root), "--change", CHANGE, "--json")[0], 1)

    def test_validar_calls_real_gate_and_requires_bindings(self):
        make(self.root, 4)
        code, out, _ = self.run_cli("validar", "--project", str(self.root), "--change", CHANGE, "--json")
        self.assertEqual(code, 0, out)
        value = json.loads(out)
        self.assertFalse(value["phaseExecuted"])
        self.assertEqual(value["localChecksExecuted"], ["security_gate"])
        path = self.root / f"specs/changes/{CHANGE}/change.json"
        edit(path, lambda d: d.update(securityRefs=[], claimedState="IMPLEMENTACAO_APROVADA"))
        code, out, _ = self.run_cli("validar", "--project", str(self.root), "--change", CHANGE, "--json")
        self.assertEqual(code, 1, out)
        self.assertIn("SECURITY_BINDING_MISSING", out)
        put(self.root, f"specs/changes/{CHANGE}/security-gate.json", "human text")
        self.assertEqual(self.run_cli("validar", "--project", str(self.root), "--change", CHANGE, "--json")[0], 1)

    def test_validar_any_security_problem_remains_pending(self):
        make(self.root, 3)
        code, out, _ = self.run_cli("validar", "--project", str(self.root), "--change", CHANGE, "--json")
        self.assertEqual(code, 1, out)
        gate = json.loads((self.root / f"specs/changes/{CHANGE}/evidence/security/security-gate.json").read_text())
        self.assertFalse(gate["validationAllowed"])
        self.assertIn("AUDIT_REPORT_MISSING", gate["reasons"])

    def test_validar_preserves_conflicting_gate(self):
        make(self.root, 3)
        ref = f"specs/changes/{CHANGE}/evidence/security/security-gate.json"
        gate = {"schemaVersion": 1, "changeId": CHANGE, "status": "pendente",
                "validationAllowed": False, "exitCode": 1, "reasons": ["old"],
                "method": "old", "limitations": []}
        put(self.root, ref, gate)
        before = (self.root / ref).read_bytes()
        code, out, _ = self.run_cli("validar", "--project", str(self.root), "--change", CHANGE, "--json")
        self.assertEqual(code, 1, out)
        self.assertIn("CONTENT_CONFLICT", out)
        self.assertEqual((self.root / ref).read_bytes(), before)

    def test_argument_errors_and_configuration_never_expose_values(self):
        for arguments in [["unknown-command", "synthetic-secret"], ["--json"], ["--project"],
                          ["doctor", "--project", "a", "--project=b"], ["init", str(self.root), "--integration", "unsupported"],
                          ["check", "--change", CHANGE, "--target", "BAD"]]:
            code, out, err = self.run_cli(*arguments, "--json")
            self.assertEqual(code, 2, out)
            self.assertNotIn("synthetic-secret", out + err)
        initialize(self.root)
        put(self.root, "configuracao.properties", "unknown.secret=synthetic-secret\n")
        code, out, err = self.run_cli("doctor", "--project", str(self.root), "--json")
        self.assertEqual(code, 2, out)
        self.assertNotIn("synthetic-secret", out + err)

    def test_explicit_project_init_cannot_escape_base(self):
        for destination in ["../escape", str(self.root.parent / "absolute")]:
            code, out, _ = self.run_cli("init", destination, "--project", str(self.root), "--json")
            self.assertEqual(code, 2, out)
        self.assertFalse((self.root.parent / "escape").exists())
        self.assertEqual(self.run_cli("init", "nested", "--project", str(self.root), "--json")[0], 0)

    def test_code_handoff_cannot_ignore_state_conflict(self):
        path = make(self.root, 2)
        edit(path, lambda d: d.update(claimedState="EM_REVISAO_SPEC"))
        self.assertEqual(self.run_cli("implementar", "--project", str(self.root), "--change", CHANGE, "--json")[0], 1)
        code, out, err = self.run_cli("implementar", "--project", str(self.root), "--change", "../synthetic-secret", "--json")
        self.assertEqual(code, 2)
        self.assertNotIn("synthetic-secret", out + err)

    def test_help_version_project_discovery_and_text_mode(self):
        for args in [["--help"], ["--version"], ["init", "--help"]]:
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as raised:
                main(args)
            self.assertEqual(raised.exception.code, 0)
        initialize(self.root)
        with patch("pathlib.Path.cwd", return_value=self.root):
            code, out, _ = self.run_cli("doctor")
            self.assertEqual(code, 0, out)
            self.assertIn("inactive_placeholder", out)
        code, out, _ = self.run_cli("nova-change", "Example", "--project", str(self.root))
        self.assertEqual(code, 0, out)
        self.assertIn("Change:", out)
        ident = sorted((self.root / "specs/changes").glob("*/draft.json"))[0].parent.name
        code, out, _ = self.run_cli("especificar", "--change", ident, "--project", str(self.root))
        self.assertEqual(code, 0, out)
        self.assertIn("Editor:", out)
        self.assertEqual(len(catalog()), 11)

    def test_busy_and_doctor_invalid_filled_resource(self):
        initialize(self.root)
        values = {"sonar.url": "bad-url", "sonar.autenticacao": "token", "sonar.usuario": "NAO_APLICAVEL",
                  "sonar.senha": "NAO_APLICAVEL", "sonar.token": "synthetic-secret", "sonar.projeto": "demo"}
        put(self.root, "configuracao.properties", "\n".join(k + "=" + v for k, v in values.items()))
        code, out, _ = self.run_cli("doctor", "--project", str(self.root), "--json")
        self.assertEqual(code, 1, out)
        self.assertNotIn("synthetic-secret", out)
        put(self.root, ".specflow/write.lock", "another writer")
        self.assertEqual(self.run_cli("doctor", "--project", str(self.root), "--json")[0], 1)

    def test_check_and_evaluate_use_core_without_writes(self):
        make(self.root, 1)
        for name in ["check", "evaluate"]:
            before = snapshot(self.root)
            code, out, _ = self.run_cli(name, "--project", str(self.root), "--change", CHANGE, "--target", "SPEC_APROVADA", "--json")
            self.assertEqual(code, 0, out)
            self.assertTrue(json.loads(out)["allowed"])
            self.assertEqual(before, snapshot(self.root))
