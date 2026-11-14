"""Importacao local autorizada, por allowlist do corpus ja inventariado.

Nao executa arquivos importados, nao sobrescreve destino e nunca escreve na origem.
Uso: python -B tools/importar_recursos.py --origem <checkout-autorizado> --aplicar
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'specs/changes/10028-investigar-specflow-framework/evidence'
OUTPUT = ROOT / 'imports/acervo-local-2026-11-12'
PREFIXES = ('.agents/skills/', '.github/agents/', '.github/prompts/',
            'specs/shared/', 'specs/templates/', 'specs/sprint/', 'scripts/sonar/')
EXCLUDED = {'specs/sprint/SPRINT-001-Produto-Base.md'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(source, *args):
    result = subprocess.run(['git', *args], cwd=source, capture_output=True,
                            encoding='utf-8', errors='strict')
    if result.returncode:
        raise RuntimeError('Falha na leitura de metadados Git da origem')
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--aplicar', action='store_true')
    parser.add_argument('--origem', type=Path, required=True,
                        help='checkout autorizado explicitamente; nao ha caminho padrao')
    args = parser.parse_args()
    baseline = json.loads((EVIDENCE / 'baseline.json').read_text(encoding='utf-8'))
    source = args.origem.resolve(strict=True)
    if source == ROOT or ROOT.is_relative_to(source) or source.is_relative_to(ROOT):
        raise RuntimeError('Origem e destino devem ser independentes')
    head = git(source, 'rev-parse', 'HEAD')
    status = git(source, 'status', '--porcelain=v1')
    if head != baseline['head'] or status != baseline['status']:
        raise RuntimeError('Origem diverge do baseline; nao importar silenciosamente')
    selected = [f for f in baseline['files']
                if f['path'].startswith(PREFIXES) and f['path'] not in EXCLUDED]
    pending = []
    # Verificar todo o corpus e todos os destinos antes da primeira escrita.
    for f in baseline['files']:
        path = (source / f['path']).resolve(strict=True)
        if not path.is_relative_to(source) or digest(path.read_bytes()) != f['sha256']:
            raise RuntimeError('Corpus alterado ou caminho fora da origem: ' + f['path'])
    for f in selected:
        target = (ROOT / f['path']).resolve()
        if not target.is_relative_to(ROOT):
            raise RuntimeError('Destino fora do workspace')
        if target.exists():
            raise RuntimeError('Destino existente; revisar sem sobrescrever: ' + f['path'])
        pending.append((f, target))
    print(json.dumps({'selected': len(selected), 'bytes': sum(f['bytes'] for f in selected),
                      'apply': args.aplicar}))
    if not args.aplicar:
        return
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records = []
    for f, target in pending:
        data = (source / f['path']).read_bytes()
        if digest(data) != f['sha256']:
            raise RuntimeError('Origem mudou durante a copia: ' + f['path'])
        target.parent.mkdir(parents=True, exist_ok=True)
        # xb impede sobrescrever arquivo criado depois do preflight.
        with target.open('xb') as stream:
            stream.write(data)
        records.append({'path': f['path'], 'bytes': len(data),
                        'sourceSha256': f['sha256'], 'localSha256': digest(data),
                        'adaptation': None})
    changes = [f['path'] for f in baseline['files']
               if digest((source / f['path']).read_bytes()) != f['sha256']]
    preservation = {'examined': len(baseline['files']), 'changed': changes,
                    'headBefore': head, 'headAfter': git(source, 'rev-parse', 'HEAD'),
                    'statusBefore': status,
                    'statusAfter': git(source, 'status', '--porcelain=v1')}
    manifest = {'schemaVersion': 1, 'date': '2026-11-12', 'source': str(source),
                'sourceHead': head, 'authorization': 'Pedido expresso do usuario nesta conversa: importar recursos necessarios sem alterar projeto-origem',
                'scope': 'Copia local privada de suporte; nao e release ou implementacao do nucleo',
                'license': 'Direitos originais preservados; redistribuicao nao liberada',
                'sourcePreservation': preservation, 'files': records}
    (OUTPUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if changes or preservation['headAfter'] != head or preservation['statusAfter'] != status:
        raise RuntimeError('Preservacao da origem nao confirmada; consultar manifesto')
    print(json.dumps({'copied': len(records), 'sourcePreserved': True}))


if __name__ == '__main__':
    main()
