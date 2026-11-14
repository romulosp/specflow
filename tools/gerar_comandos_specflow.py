"""Materializa Skills Codex e prompts Copilot a partir do catalogo local."""
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'docs/comandos/comandos.json'


def artifacts(command):
    name = command['name']
    if not re.fullmatch(r'(?:specflow|speckflow)-[a-z]+(?:-[a-z]+)*', name):
        raise ValueError('Nome de comando invalido')
    desc = json.dumps(command['description'], ensure_ascii=False)
    common = ('# ' + name + '\n\nFase: ' + command['phase'] + '\n\n'
              'Entrada: ' + command['input'] + '\n\n'
              'Saida: ' + command['output'] + '\n\n'
              '## Procedimento\n\n' + '\n'.join(str(i) + '. ' + step for i, step in enumerate(command['steps'], 1)) + '\n')
    boundary = command.get('boundary', 'Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.')
    rules = ('\n## Regras locais\n\nLeia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. '
             'Trabalhe somente neste workspace e mantenha a memoria da Change. '
             'Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. '
             + boundary + '\n')
    skill = ('---\nname: ' + name + '\ndescription: ' + desc + '\nlicense: MIT\nmetadata:\n  author: "Rômulo Penha"\n---\n\n' + common + rules)
    prompt = ('---\ndescription: ' + desc + '\nargument-hint: "Informe objetivo ou caminho da Change"\nagent: agent\n---\n\n' + common
              + '\nArgumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}\n' + rules)
    return [(ROOT / '.agents/skills' / name / 'SKILL.md', skill),
            (ROOT / '.github/prompts' / (name + '.prompt.md'), prompt)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verifica sem escrever')
    args = parser.parse_args()
    data = json.loads(CATALOG.read_text(encoding='utf-8'))
    expanded = []
    for command in data['commands']:
        expanded.append(command)
        for alias in command.get('aliases', []):
            expanded.append(dict(command, name=alias,
                                 description='Alias de ' + command['name'] + ': ' + command['description']))
    names = [c['name'] for c in expanded]
    if data['schemaVersion'] != 1 or len(set(names)) != len(names):
        raise ValueError('Catalogo invalido ou nome duplicado')
    mismatch = []
    for command in expanded:
        for path, content in artifacts(command):
            if args.check:
                if not path.exists() or path.read_text(encoding='utf-8') != content:
                    mismatch.append(path.relative_to(ROOT).as_posix())
            else:
                if path.exists() and path.read_text(encoding='utf-8') != content:
                    raise ValueError('Arquivo divergente; revisar antes de sobrescrever: ' + path.relative_to(ROOT).as_posix())
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8', newline='\n')
    print(json.dumps({'commands': len(data['commands']), 'aliases': len(expanded) - len(data['commands']), 'artifacts': len(names) * 2, 'mismatch': mismatch}, ensure_ascii=False))
    return 1 if mismatch else 0


if __name__ == '__main__':
    sys.exit(main())
