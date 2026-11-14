"""Verificacao autoral do checkout publico, sem depender do acervo local."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def evaluate(root, runner=subprocess.run):
    root = Path(root).resolve()
    result = {'mode': 'public', 'exitCode': 0, 'checks': [],
              'localCorpus': 'not_run', 'history': 'not_checked',
              'limitations': ['Nao verifica direitos upstream ou remove historico publico.']}

    def check(name, passed):
        result['checks'].append({'id': name, 'passed': bool(passed)})

    def path(ref):
        if not isinstance(ref, str) or not ref or any(x in ref for x in ('\\', ':')):
            raise ValueError('path invalid')
        parts = ref.split('/')
        if any(x in {'', '.', '..'} for x in parts):
            raise ValueError('path invalid')
        target = root.joinpath(*parts)
        cursor = root
        for part in parts:
            cursor = cursor / part
            if cursor.is_symlink() or getattr(cursor, 'is_junction', lambda: False)():
                raise ValueError('link invalid')
        if not target.resolve().is_relative_to(root):
            raise ValueError('path escape')
        return target

    try:
        inventory = json.loads(path('docs/release/inventario-retirada-acervo.json').read_text(encoding='utf-8'))
        if not isinstance(inventory['files'], list) or not inventory['files']:
            raise ValueError('inventory empty')
        seen = set()
        for row in inventory['files']:
            ref = row['path']
            if ref in seen:
                raise ValueError('duplicate path')
            seen.add(ref)
            target = path(ref)
            replacement = row.get('replacementSha256')
            check('excluded:' + ref, not target.exists() if replacement is None else
                  target.is_file() and hashlib.sha256(target.read_text(encoding='utf-8-sig').encode('utf-8')).hexdigest() == replacement)
        for ref in ('LICENSE', 'LICENSE-SCOPE.md', 'THIRD_PARTY_NOTICES.md',
                    'specs/shared/process/workflow.md', 'specs/shared/process/evidence-conventions.md',
                    'docs/comandos/comandos.json', 'docs/modelagem/GUIA.md'):
            check('required:' + ref, path(ref).is_file())
        run = runner([sys.executable, '-B', str(path('tools/gerar_comandos_specflow.py')), '--check'],
                     cwd=root, capture_output=True, text=True)
        check('authorial-commands', run.returncode == 0)
        result['exitCode'] = 0 if all(x['passed'] for x in result['checks']) else 1
    except (OSError, ValueError, KeyError, TypeError) as error:
        result.update(exitCode=2, reason=type(error).__name__)
    return result
