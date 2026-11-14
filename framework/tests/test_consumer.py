import contextlib
import copy
import io
import json
import os
from pathlib import Path
import runpy
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from specflow import configuration as config
from specflow.consumer import initialize, doctor, new_change, generate_application, find_project
from specflow.fileops import Transaction, busy
from specflow.storage import Fault, dump, read_json
from specflow.memory import result
from support import make, CHANGE, put, edit, snapshot


class ConsumerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve() / "consumer"

    def test_initialize_empty_and_repeated_adaptive_integrations(self):
        initialize(self.root)
        self.assertFalse((self.root / ".github/prompts").exists())
        self.assertFalse((self.root / "apps").exists())
        self.assertEqual(doctor(self.root)["exitCode"], 0)
        props = config.parse((self.root / "configuracao.properties").read_bytes())
        self.assertEqual(len(props), 25)
        self.assertEqual(set(props.values()), {"DEFINIR"})
        before = snapshot(self.root)
        initialize(self.root)
        self.assertEqual(before, snapshot(self.root))
        initialize(self.root, ["copilot"])
        self.assertEqual(len(list((self.root / ".github/prompts").glob("*.prompt.md"))), 12)
        write = put(self.root, "apps/custom.txt", "authorial application")
        agents = put(self.root, "AGENTS.md", "authorial instructions")
        properties = put(self.root, "configuracao.properties", "sonar.token=synthetic-secret\n")
        initialize(self.root, ["codex"])
        self.assertEqual(agents.read_text(), "authorial instructions")
        self.assertEqual(properties.read_text(), "sonar.token=synthetic-secret\n")
        self.assertEqual(write.read_text(), "authorial application")
        self.assertEqual(len(list((self.root / ".agents/skills").glob("specflow-*/SKILL.md"))), 11)
        self.assertTrue((self.root / ".agents/skills/speckflow-teste-humano/SKILL.md").is_file())
        self.assertEqual(find_project(self.root / "apps"), self.root)
        self.assertEqual(read_json(self.root / ".specflow/managed-files.json")["integrations"], ["codex", "copilot"])

    def test_existing_authorial_files_conflict_before_any_content_write(self):
        put(self.root, "specs/shared/process/workflow.md", "human authored")
        with self.assertRaises(Fault) as raised:
            initialize(self.root, ["copilot"])
        self.assertEqual(raised.exception.code, 1)
        self.assertEqual((self.root / "specs/shared/process/workflow.md").read_text(), "human authored")
        self.assertFalse((self.root / "configuracao.properties").exists())
        self.assertFalse((self.root / ".specflow/write.lock").exists())
        with self.assertRaises(Fault):
            initialize(self.root, ["unknown"])

    def test_owned_divergence_and_invalid_ownership_never_overwritten(self):
        initialize(self.root)
        put(self.root, "specs/shared/process/workflow.md", "local customization")
        before = snapshot(self.root)
        with self.assertRaises(Fault):
            initialize(self.root, ["copilot"])
        self.assertEqual(before, snapshot(self.root))
        with self.assertRaises(Fault):
            doctor(self.root)
        # Metadata that would include its own digest is never accepted.
        edit(self.root / ".specflow/managed-files.json", lambda d: d["files"].update({".specflow/managed-files.json": "0" * 64}))
        with self.assertRaises(Fault):
            doctor(self.root)

    def test_ignore_preserves_bytes_and_detects_negation(self):
        ignore = put(self.root, ".gitignore", b"".decode() + "user-rule\r\n")
        initialize(self.root)
        self.assertEqual(ignore.read_bytes(), b"user-rule\r\n/configuracao.properties\r\n")
        before = ignore.read_bytes()
        initialize(self.root)
        self.assertEqual(ignore.read_bytes(), before)
        ignore.write_bytes(before + b"!*.properties\r\n")
        with self.assertRaises(Fault):
            initialize(self.root)
        self.assertTrue(ignore.read_bytes().endswith(b"!*.properties\r\n"))

    def test_properties_literal_values_and_errors_are_redacted(self):
        raw = b"\xef\xbb\xbfsonar.token=  abc=def#ghi  \r\ngo.executavel=C:\\Go\\bin\\go.exe\r\n"
        values = config.parse(raw)
        self.assertEqual(values["sonar.token"], "  abc=def#ghi  ")
        self.assertEqual(values["go.executavel"], "C:\\Go\\bin\\go.exe")
        for invalid in [b"sonar.token=a\nsonar.token=b", b"unknown.secret=synthetic-secret", b"sonar.token", b"\xff", b"sonar.token=abc\r", b"sonar.token=\x00"]:
            with self.subTest(invalid=invalid), self.assertRaises(Fault) as raised:
                config.parse(invalid)
            self.assertNotIn("synthetic-secret", str(raised.exception))
        self.assertEqual(config.parse(b"  # comment\n\n"), {})

    def test_every_placeholder_prevents_probes_independently(self):
        initialize(self.root)
        values = config.parse((self.root / "configuracao.properties").read_bytes())
        with patch("subprocess.run", side_effect=AssertionError("no process")), patch("socket.create_connection", side_effect=AssertionError("no network")):
            states = config.statuses((self.root / "configuracao.properties").read_bytes())
            self.assertTrue(all(x["status"] == "inactive_placeholder" for x in states.values()))
            values["sonar.url"] = "https://example.invalid"
            self.assertEqual(config.resolve("sonar", values)["status"], "inactive_placeholder")
            self.assertEqual(config.resolve("go", values)["status"], "inactive_placeholder")
            self.assertEqual(doctor(self.root)["exitCode"], 0)
        with self.assertRaises(Fault) as raised:
            config.require_resource("sonar", (self.root / "configuracao.properties").read_bytes())
        self.assertEqual(raised.exception.code, 1)
        with self.assertRaises(Fault):
            config.resolve("undeclared", values)

    def test_optional_authentication_and_bad_configuration(self):
        valid = {"sonar.url": "https://example.invalid", "sonar.autenticacao": "token", "sonar.projeto": "demo",
                 "sonar.usuario": "NAO_APLICAVEL", "sonar.senha": "NAO_APLICAVEL", "sonar.token": "synthetic-secret"}
        self.assertTrue(config.resolve("sonar", valid)["configurationReady"])
        self.assertNotIn("synthetic-secret", dump(config.resolve("sonar", valid)))
        for key, value in [("sonar.url", "NAO_APLICAVEL"), ("sonar.token", "NAO_APLICAVEL"),
                           ("sonar.autenticacao", "unsupported"), ("sonar.url", "javascript:bad"),
                           ("sonar.url", "https://user:password@example.invalid"), ("sonar.url", "https://example.invalid:bad")]:
            bad = {**valid, key: value}
            self.assertEqual(config.resolve("sonar", bad)["status"], "inactive_invalid")
        self.assertEqual(config.resolve("sonar", {**valid, "sonar.token": " definir "})["status"], "inactive_placeholder")
        self.assertEqual(config.resolve("sonar", {})["status"], "inactive_missing")
        basic = {**valid, "sonar.autenticacao": "basic", "sonar.usuario": "user", "sonar.senha": "  password=literal  ", "sonar.token": "NAO_APLICAVEL"}
        self.assertTrue(config.resolve("sonar", basic)["configurationReady"])
        raw = "\n".join(k + "=" + v for k, v in valid.items()).encode()
        self.assertTrue(config.require_resource("sonar", raw)["configurationReady"])

    def test_new_changes_never_recycle_reservations_or_overwrite(self):
        initialize(self.root)
        first = new_change(self.root, "Cadastro de clientes")
        second = new_change(self.root, "Cadastro de clientes")
        self.assertTrue(first["changeId"].startswith("00001-"))
        self.assertTrue(second["changeId"].startswith("00002-"))
        self.assertEqual(result(self.root, first["changeId"])["observedState"], "RASCUNHO")
        self.assertEqual(result(self.root, second["changeId"], "evaluate", "IMPLEMENTADA")["exitCode"], 1)
        with patch.object(Transaction, "apply", side_effect=OSError("injected")):
            with self.assertRaises(OSError):
                new_change(self.root, "failure")
        third = new_change(self.root, "recovery")
        self.assertTrue(third["changeId"].startswith("00004-"))
        unicode_goal = "\u5de5\u7a0b"
        fourth = new_change(self.root, unicode_goal)
        self.assertTrue(fourth["changeId"].endswith("mudanca"))
        draft = read_json(self.root / fourth["path"] / "draft.json")
        self.assertEqual(draft["objective"], unicode_goal)
        self.assertLessEqual(len(new_change(self.root, "a" * 500)["changeId"]), 80)
        for objective in ["", " ", None, "x\x00"]:
            with self.assertRaises(Fault):
                new_change(self.root, objective)

    def test_generation_gate_and_paths(self):
        make(self.root)
        with self.assertRaises(Fault):
            generate_application(self.root, "demo", {"main.py": b"x"}, {"changeId": CHANGE, "paths": ["apps/demo/main.py"]})
        self.assertFalse((self.root / "apps").exists())
        make(self.root, 1)
        put(self.root, f"specs/changes/{CHANGE}/implementation-plan.md", "plan")
        result_paths = generate_application(self.root, "demo", {"main.py": b"code"}, {"changeId": CHANGE, "paths": ["apps/demo/main.py"]})
        self.assertEqual(result_paths, ["apps/demo/main.py"])
        self.assertEqual((self.root / "apps/demo/main.py").read_bytes(), b"code")
        with self.assertRaises(Fault):
            generate_application(self.root, "demo", {"main.py": b"different"}, {"changeId": CHANGE, "paths": ["apps/demo/main.py"]})
        for ref in ["../escape.py", "CON.txt", "a./b.py"]:
            with self.assertRaises(Fault):
                generate_application(self.root, "other", {ref: b"bad"}, {"changeId": CHANGE, "paths": ["apps/other/" + ref]})
        with self.assertRaises(Fault):
            generate_application(self.root, "../bad", {"x": b"x"}, {"changeId": CHANGE, "paths": []})
        with self.assertRaises(Fault):
            generate_application(self.root, "demo", {"x": b"x"}, {"changeId": CHANGE, "paths": ["apps/demo/y"]})

    def test_write_lock_conflict_and_ownership(self):
        with Transaction(self.root) as tx:
            with self.assertRaises(Fault) as raised:
                busy(self.root)
            self.assertEqual(raised.exception.code, 1)
            with self.assertRaises(Fault):
                with Transaction(self.root):
                    pass
            tx.apply({"one.txt": b"one"})
        self.assertFalse((self.root / ".specflow/write.lock").exists())
        with self.assertRaises(Fault):
            Transaction(self.root).apply({"x": b"x"})
        with self.assertRaises(Fault):
            with Transaction(self.root) as tx:
                tx.lock.write_bytes(b"changed by another owner")
        self.assertEqual((self.root / ".specflow/write.lock").read_bytes(), b"changed by another owner")

    def test_preflight_case_and_file_directory_collisions(self):
        for plan in [{"a": b"x", "a/b": b"y"}, {"Dir/a": b"x", "dir/b": b"y"}, {"A.txt": b"x", "a.txt": b"y"}]:
            with Transaction(self.root) as tx, patch.object(tx, "_write") as write, self.assertRaises(Fault):
                tx.apply(plan)
            write.assert_not_called()
        put(self.root, "Case.txt", "old")
        with Transaction(self.root) as tx, self.assertRaises(Fault):
            tx.apply({"case.txt": b"x"})

    def test_atomic_replace_does_not_modify_hardlink_target(self):
        target = put(self.root, "outside.txt", "authorial")
        os.link(target, self.root / "managed.txt")
        with Transaction(self.root) as tx:
            tx.apply({"managed.txt": b"managed update"}, mutable={"managed.txt"})
        self.assertEqual(target.read_text(), "authorial")
        self.assertEqual((self.root / "managed.txt").read_text(), "managed update")

    def test_failed_write_rolls_back_without_deleting_external_edit(self):
        original = Transaction._write
        calls = []
        def fail_second(tx, path, value, expected):
            calls.append(path)
            if len(calls) == 2:
                raise OSError("injected disk failure")
            original(tx, path, value, expected)
        with self.assertRaises(Fault) as raised:
            with Transaction(self.root) as tx, patch.object(Transaction, "_write", fail_second):
                tx.apply({"nested/one": b"one", "nested/two": b"two"})
        self.assertEqual(raised.exception.reason, "WRITE_IO_ERROR")
        self.assertFalse((self.root / "nested/one").exists())
        calls.clear()
        def edited_failure(tx, path, value, expected):
            calls.append(path)
            if len(calls) == 2:
                (tx.root / "one").write_bytes(b"external edit")
                raise OSError("injected")
            original(tx, path, value, expected)
        with self.assertRaises(Fault) as raised:
            with Transaction(self.root) as tx, patch.object(Transaction, "_write", edited_failure):
                tx.apply({"one": b"ours", "two": b"ours"})
        self.assertEqual(raised.exception.reason, "WRITE_PARTIAL")
        self.assertEqual((self.root / "one").read_bytes(), b"external edit")

    def test_failed_mutable_update_restores_baseline(self):
        path = put(self.root, "managed", "old")
        original = Transaction._write
        def hook(tx, destination, value, expected):
            if destination.name == "last":
                raise OSError("failure")
            original(tx, destination, value, expected)
        with self.assertRaises(Fault):
            with Transaction(self.root) as tx, patch.object(Transaction, "_write", hook):
                tx.apply({"managed": b"new", "last": b"x"}, mutable={"managed"})
        self.assertEqual(path.read_text(), "old")

    def test_actual_junction_cannot_escape_or_receive_writes(self):
        self.root.mkdir()
        outside = self.root.parent / "outside"
        outside.mkdir()
        link = self.root / "alias"
        if os.name == "nt":
            command = subprocess.run(["cmd", "/d", "/c", "mklink", "/J", str(link), str(outside)], capture_output=True)
            if command.returncode:
                self.skipTest("Windows junction creation unavailable")
        else:
            link.symlink_to(outside, target_is_directory=True)
        try:
            with Transaction(self.root) as tx, self.assertRaises(Fault):
                tx.apply({"alias/escape.txt": b"bad"})
            self.assertFalse((outside / "escape.txt").exists())
        finally:
            link.rmdir() if os.name == "nt" else link.unlink()

    def test_explicit_wrapper_uses_only_trusted_fixed_cli_operation(self):
        from importlib.resources import files
        wrapper = files("specflow").joinpath("assets/gate_wrapper.py")
        namespace = runpy.run_path(str(wrapper))
        callback = namespace["main"]
        target = self.root / "specs/changes" / CHANGE
        target.mkdir(parents=True)
        callback.__globals__["__file__"] = str(self.root / "docs/security-audit/verificar_seguranca.py")
        with patch("shutil.which", return_value="trusted-specflow"), patch("subprocess.run", return_value=subprocess.CompletedProcess([], 0)) as run:
            self.assertEqual(callback(["--change", str(target)]), 0)
            argv = run.call_args.args[0]
            self.assertEqual(argv[:2], ["trusted-specflow", "validar"])
            self.assertFalse(run.call_args.kwargs["shell"])
        with contextlib.redirect_stdout(io.StringIO()):
            with patch("shutil.which", return_value=None):
                self.assertEqual(callback(["--change", str(target)]), 2)
            self.assertEqual(callback(["--change", str(self.root.parent)]), 2)
            with patch("shutil.which", return_value="trusted"), patch("subprocess.run", side_effect=OSError("unavailable")):
                self.assertEqual(callback(["--change", str(target)]), 2)
            with patch("shutil.which", return_value="trusted"), patch("subprocess.run", return_value=subprocess.CompletedProcess([], 99)):
                self.assertEqual(callback(["--change", str(target)]), 2)
            with patch.object(Path, "resolve", side_effect=OSError("synthetic-secret")):
                self.assertEqual(callback(["--change", str(target)]), 2)
            with patch("sys.argv", ["gate", "--unknown", "synthetic-secret"]), self.assertRaises(SystemExit) as raised:
                runpy.run_path(str(wrapper), run_name="__main__")
            self.assertEqual(raised.exception.code, 2)
