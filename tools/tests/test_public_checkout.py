"""Testes do checkout publico e da separacao explicita do acervo local."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verificar_checkout_publico as public
import verificar_dossie as dossier


class PublicCheckoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ('LICENSE', 'LICENSE-SCOPE.md', 'THIRD_PARTY_NOTICES.md',
                     'specs/shared/process/workflow.md', 'specs/shared/process/evidence-conventions.md',
                     'docs/comandos/comandos.json', 'docs/modelagem/GUIA.md', 'tools/gerar_comandos_specflow.py'):
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('authorial', encoding='utf-8')
        self.inventory = self.root / 'docs/release/inventario-retirada-acervo.json'
        self.inventory.parent.mkdir(parents=True)
        self.write([{'path': 'private.txt'}])

    def write(self, files):
        self.inventory.write_text(json.dumps({'files': files}), encoding='utf-8')

    def run_check(self, code=0):
        with patch.object(public.subprocess, 'run', return_value=type('Run', (), {'returncode': code})()):
            # Explicit runner makes the test independent from the default bound callable.
            return public.evaluate(self.root, runner=public.subprocess.run)

    def test_absent_corpus_and_replacement(self):
        result = self.run_check()
        self.assertEqual(result['exitCode'], 0)
        self.assertEqual(result['localCorpus'], 'not_run')
        replacement = self.root / 'new.txt'
        replacement.write_bytes(b'authorial')
        self.write([{'path': 'new.txt', 'replacementSha256': hashlib.sha256(b'authorial').hexdigest()}])
        self.assertEqual(self.run_check()['exitCode'], 0)
        replacement.write_bytes(b'authorial\r\n')
        self.write([{'path': 'new.txt', 'replacementSha256': hashlib.sha256(b'authorial\n').hexdigest()}])
        self.assertEqual(self.run_check()['exitCode'], 0)
        replacement.write_bytes(b'changed')
        self.assertEqual(self.run_check()['exitCode'], 1)

    def test_forbidden_file_missing_required_and_tool_failure(self):
        (self.root / 'private.txt').write_text('private')
        self.assertEqual(self.run_check()['exitCode'], 1)
        (self.root / 'private.txt').unlink()
        (self.root / 'LICENSE').unlink()
        self.assertEqual(self.run_check()['exitCode'], 1)
        self.assertEqual(self.run_check(2)['exitCode'], 1)

    def test_invalid_inventory_and_paths(self):
        for files in ([], [{'path': '../escape'}], [{'path': '/absolute'}],
                      [{'path': 'C:/escape'}], [{'path': 'a\\b'}], [{'path': None}],
                      [{'path': 'a'}, {'path': 'a'}]):
            self.write(files)
            self.assertEqual(self.run_check()['exitCode'], 2)
        self.inventory.write_text('{broken')
        self.assertEqual(self.run_check()['exitCode'], 2)
        self.inventory.unlink()
        self.assertEqual(self.run_check()['exitCode'], 2)

    def test_modes_and_partial_local_corpus(self):
        with patch.object(dossier, 'ROOT', self.root), patch.object(dossier, 'IMPORT', self.root / 'imports'):
            with contextlib.redirect_stdout(io.StringIO()), patch.object(public, 'evaluate', return_value={'exitCode': 0, 'localCorpus': 'not_run'}) as call:
                self.assertEqual(dossier.main([]), 0)
                call.assert_called_once_with(self.root)
            (self.root / 'imports').mkdir()
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(dossier.main([]), 2)
                self.assertEqual(json.loads(out.getvalue())['mode'], 'local')

    def test_links_and_runner_errors_are_reported(self):
        with patch.object(Path, 'is_symlink', return_value=True):
            self.assertEqual(self.run_check()['exitCode'], 2)
        def fail(*args, **kwargs):
            raise OSError('unavailable')
        self.assertEqual(public.evaluate(self.root, runner=fail)['exitCode'], 2)

    def test_local_manifest_paths_cannot_escape(self):
        corpus = self.root / 'imports'
        corpus.mkdir()
        with patch.object(dossier, 'ROOT', self.root), patch.object(dossier, 'IMPORT', corpus):
            for ref in ('../outside', '/absolute', 'C:/bad', 'a\\b', None):
                (corpus / 'manifest.json').write_text(json.dumps({'files': [{'path': ref}]}))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(dossier.main(['--mode', 'local']), 2)
            with patch.object(Path, 'is_symlink', return_value=True), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(dossier.main(['--mode', 'local']), 2)

    @unittest.skipUnless(dossier.IMPORT.is_dir(), 'Acervo local ausente no checkout publico')
    def test_real_local_integrity(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(dossier.main(['--mode', 'local']), 0)


if __name__ == '__main__':
    unittest.main()
