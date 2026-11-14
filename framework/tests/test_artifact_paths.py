from pathlib import Path
import tempfile
import unittest

from specflow.security import security_path, gate_result
from specflow.storage import Fault


class SecurityPathTests(unittest.TestCase):
    def test_new_legacy_and_conflicting_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            folder = root / 'changes' / 'demo'
            folder.mkdir(parents=True)
            name = 'security-audit.json'
            self.assertEqual(security_path(root, folder, name), 'changes/demo/evidence/security/' + name)
            legacy = folder / name
            legacy.write_text('{}')
            self.assertEqual(security_path(root, folder, name), 'changes/demo/' + name)
            new = folder / 'evidence' / 'security' / name
            new.parent.mkdir(parents=True)
            new.write_text('{}')
            with self.assertRaises(Fault) as raised:
                security_path(root, folder, name)
            self.assertEqual(raised.exception.reason, 'SECURITY_PATH_CONFLICT')
            self.assertEqual(gate_result(root, folder)['reasons'], ['SECURITY_PATH_CONFLICT'])
            self.assertEqual(legacy.read_text(), '{}')
            self.assertEqual(new.read_text(), '{}')

    def test_rejects_folder_outside_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve() / 'root'
            root.mkdir()
            with self.assertRaises(Fault) as raised:
                security_path(root, root.parent, 'security-gate.json')
            self.assertEqual(raised.exception.reason, 'PATH_ESCAPE')
