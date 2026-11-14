"""Confere somente os recursos locais, sem acesso a checkout externo."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IMPORT = ROOT / 'imports/acervo-local-2026-11-12'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    manifest = json.loads((IMPORT / 'manifest.json').read_text(encoding='utf-8'))
    dependencies = json.loads((IMPORT / 'dependencias.json').read_text(encoding='utf-8'))
    checks = []
    commands = []

    def check(name, passed, details):
        checks.append({'name': name, 'passed': bool(passed), 'details': details})

    def run(arguments):
        result = subprocess.run(arguments, cwd=ROOT, capture_output=True,
                                encoding='utf-8', errors='replace')
        record = {'command': subprocess.list2cmdline([str(a) for a in arguments]),
                  'code': result.returncode, 'stdout': result.stdout.strip(),
                  'stderr': result.stderr.strip()}
        commands.append(record)
        return result.returncode

    changed = []
    unsafe = []
    for f in manifest['files']:
        path = (ROOT / f['path']).resolve()
        if not path.is_relative_to(ROOT):
            unsafe.append(f['path'])
            continue
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != f['localSha256']:
            changed.append(f['path'])
    check('confinamento do manifesto', not unsafe, unsafe)
    check('integridade das copias locais', not changed,
          {'examined': len(manifest['files']), 'changed': changed})
    originals = []
    for f in manifest['files']:
        if f['adaptation'] and f.get('localSnapshotSha256'):
            original = IMPORT / 'originais' / f['path']
            if not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest() != f['localSnapshotSha256']:
                originals.append(f['path'])
    check('snapshots locais das adaptacoes identificados', not originals, originals)

    critical = ['AGENTS.md', 'specs/shared/process/workflow.md',
                'specs/shared/process/evidence-conventions.md']
    critical += [f'.agents/skills/{name}/SKILL.md' for name in
                 ['spec-review', 'spec-implement', 'implementation-review',
                  'implementation-validate', 'change-approve', 'git-commit']]
    critical += [f'specs/templates/{name}-template.md' for name in
                 ['proposal', 'spec', 'design', 'tasks', 'validation']]
    check('recursos de processo locais', all((ROOT / p).is_file() for p in critical), critical)
    skill_count = sum(1 for _ in (ROOT / '.agents/skills').rglob('SKILL.md'))
    command_catalog = json.loads((ROOT / 'docs/comandos/comandos.json').read_text(encoding='utf-8'))
    aliases = sum(len(command.get('aliases', [])) for command in command_catalog['commands'])
    check('catalogo de skills locais', skill_count == 92 + len(command_catalog['commands']) + aliases, skill_count)
    check('comandos materializados', run([sys.executable, '-B', str(ROOT / 'tools/gerar_comandos_specflow.py'), '--check']) == 0, 'Skills e prompts conferidos; fases nao executadas')
    check('suporte local de auditoria e ADR', all((ROOT / p).is_file() for p in
          ['docs/security-audit/gerar_relatorio.py', 'docs/security-audit/README.md',
           'docs/adr/README.md', 'docs/adr/ADR-TEMPLATE.md',
           'docs/adr/exemplos/ADR-001-java-17-quarkus-3.md']), 'recursos locais presentes')
    check('licenca e avisos separados', all((ROOT / p).is_file() for p in
          ['LICENSE', 'LICENSE-SCOPE.md', 'THIRD_PARTY_NOTICES.md']), 'escopo autoral distinto de terceiros')

    known_missing = {(r['source'], r['target']) for r in dependencies['missingInSource']}
    missing_new = []
    external = []
    for f in manifest['files']:
        path = ROOT / f['path']
        if path.suffix.lower() not in {'.md', '.txt'}:
            continue
        content = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if re.match(r'^(?:https?://|mailto:|#)', target):
                continue
            decoded = unquote(target.strip('<>').split('#', 1)[0])
            if not decoded:
                continue
            if re.match(r'^(?:[A-Za-z]:|file:|/|\\)', decoded):
                external.append({'source': f['path'], 'target': target})
                continue
            resolved = (path.parent / decoded).resolve()
            if not resolved.is_relative_to(ROOT):
                external.append({'source': f['path'], 'target': target})
            elif not resolved.exists() and (f['path'], target) not in known_missing:
                missing_new.append({'source': f['path'], 'target': target})
    check('sem links operacionais para fora do projeto', not external, external)
    check('sem lacunas novas de links na copia', not missing_new, missing_new)

    # Executar apenas o validador de leitura ja inspecionado, sobre fixtures sintéticos.
    validator = ROOT / '.agents/skills/android-native-engineering/scripts/validate_android_project.py'
    for name, wrapper, local_properties, expected in [
        ('valid', True, False, 0), ('missing-wrapper', False, False, 1),
        ('local-properties', True, True, 1),
    ]:
        folder = IMPORT / 'fixtures' / name
        for relative in ['settings.gradle.kts', 'app/build.gradle.kts', 'app/src/main/AndroidManifest.xml']:
            target = folder / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('', encoding='utf-8')
        if wrapper:
            (folder / 'gradlew.bat').write_text('@echo off\n', encoding='utf-8')
        if local_properties:
            (folder / 'local.properties').write_text('# synthetic; no credentials\n', encoding='utf-8')
        check('fixture Android local: ' + name,
              run([sys.executable, '-B', str(validator), str(folder)]) == expected,
              {'expectedCode': expected, 'method': 'structural'})

    node = shutil.which('node')
    for f in manifest['files']:
        if f['path'].endswith('.mjs'):
            check('sintaxe MJS local: ' + f['path'],
                  node is not None and run([node, '--check', str(ROOT / f['path'])]) == 0,
                  'syntax only; no imports or runtime execution')
    python_files = sorted((ROOT / 'tools').glob('*.py')) + sorted((ROOT / '.agents').rglob('*.py'))
    python_files += sorted((ROOT / 'docs/security-audit').glob('*.py'))
    python_files += sorted((ROOT / 'tools/diagramas').glob('*.py'))
    for path in python_files:
        try:
            compile(path.read_text(encoding='utf-8-sig'), str(path), 'exec')
            check('sintaxe Python: ' + path.relative_to(ROOT).as_posix(), True, 'compile in memory')
        except (SyntaxError, UnicodeError) as error:
            check('sintaxe Python: ' + path.relative_to(ROOT).as_posix(), False, type(error).__name__)

    result = {'date': '2026-11-12', 'scope': 'local-only', 'sourceRead': False,
              'passed': sum(c['passed'] for c in checks),
              'failed': sum(not c['passed'] for c in checks), 'checks': checks,
              'commands': commands,
              'inheritedMissingReferences': len(known_missing),
              'limitations': ['Optional skills may lack resources already absent in source',
                              'Syntax and Android structural checks do not prove application runtime',
                              'No Sonar, Docker, hardware, publication or framework implementation']}
    (IMPORT / 'local-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': result['passed'], 'failed': result['failed'],
                      'sourceRead': False, 'inheritedMissingReferences': len(known_missing),
                      'failures': [c for c in checks if not c['passed']]}, ensure_ascii=False))
    return 1 if result['failed'] else 0


if __name__ == '__main__':
    sys.exit(main())
