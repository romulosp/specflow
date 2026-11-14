"""Gerador documental local; nao executa auditoria nem reutiliza conclusoes antigas."""
from pathlib import Path
import argparse
import json
import sys
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]


def load_report(path):
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict) or type(data.get('schemaVersion')) is not int or data['schemaVersion'] != 1:
        raise ValueError('schemaVersion deve ser inteiro 1')
    allowed = {'schemaVersion', 'changeId', 'revision', 'title', 'scope',
               'conclusion', 'limitations', 'findings', 'evidence'}
    if set(data) != allowed:
        raise ValueError('Campos do relatorio ausentes ou desconhecidos')
    for key in ['changeId', 'revision', 'title', 'scope', 'conclusion']:
        if not isinstance(data[key], str) or not data[key].strip():
            raise ValueError('Campo textual obrigatorio: ' + key)
    if not isinstance(data['limitations'], list) or not all(isinstance(v, str) for v in data['limitations']):
        raise ValueError('limitations deve ser lista de textos')
    for name, fields in [('findings', {'id', 'severity', 'description', 'recommendation'}),
                         ('evidence', {'id', 'command', 'outcome', 'reference'})]:
        if not isinstance(data[name], list):
            raise ValueError('Campo deve ser lista: ' + name)
        ids = set()
        for row in data[name]:
            if not isinstance(row, dict) or set(row) != fields or not all(isinstance(v, str) and v.strip() for v in row.values()):
                raise ValueError('Registro invalido em ' + name)
            if row['id'] in ids:
                raise ValueError('ID duplicado em ' + name)
            ids.add(row['id'])
            if name == 'evidence' and row['outcome'] not in {'passed', 'failed', 'not_run'}:
                raise ValueError('outcome invalido em evidence')
    return data


def build_pdf(data, output):
    # Dependencia opcional apenas do gerador PDF; nao faz parte do nucleo.
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

    base = getSampleStyleSheet()
    title = ParagraphStyle('audit-title', parent=base['Title'], fontSize=24,
                           leading=29, alignment=TA_CENTER,
                           textColor=colors.HexColor('#173B3F'))
    body = ParagraphStyle('audit-body', parent=base['BodyText'], fontSize=10,
                          leading=15, spaceAfter=8)
    story = []

    def p(text, style=body):
        # Dados nao sao markup ReportLab. Isso preserva caracteres especiais
        # e impede inserir imagens/links/comandos pelo texto do relatorio.
        story.append(Paragraph(escape(text).replace('\n', '<br/>'), style))

    p(data['title'], title)
    story.append(Spacer(1, .4 * cm))
    p('Change: ' + data['changeId'] + ' | Revisao: ' + data['revision'])
    p('Documento gerado a partir de dados declarados. Nao executa testes nem atesta seguranca por si so.')
    for heading, value in [('Escopo', data['scope']), ('Conclusao declarada', data['conclusion'])]:
        p(heading, base['Heading1']); p(value)
    p('Limitacoes', base['Heading1'])
    for item in data['limitations']:
        p(item)
    p('Achados declarados', base['Heading1'])
    if not data['findings']:
        p('Nenhum achado informado. Isso nao comprova ausencia de vulnerabilidades.')
    for row in data['findings']:
        p(row['id'] + ' — ' + row['severity'], base['Heading2'])
        p(row['description']); p('Recomendacao: ' + row['recommendation'])
    p('Evidencias declaradas', base['Heading1'])
    for row in data['evidence']:
        p(row['id'] + ' — ' + row['outcome'], base['Heading2'])
        p('Comando: ' + row['command']); p('Referencia: ' + row['reference'])
    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(output), pagesize=A4,
                                leftMargin=2 * cm, rightMargin=2 * cm,
                                topMargin=1.7 * cm, bottomMargin=1.8 * cm,
                                title=data['title'], author='Rômulo Penha')
    document.build(story)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--validate-only', action='store_true')
    args = parser.parse_args()
    try:
        data = load_report(args.input)
        if args.validate_only:
            print('Dados validos; nenhum PDF foi gerado e nenhuma auditoria executada.')
            return 0
        if args.output is None:
            parser.error('--output e obrigatorio para gerar PDF')
        output = args.output.resolve()
        if not output.is_relative_to(ROOT) or output.suffix.lower() != '.pdf':
            raise ValueError('Destino deve ser PDF dentro deste projeto')
        if output.exists():
            raise ValueError('Destino existente; escolha outro nome, sem sobrescrever')
        build_pdf(data, output)
        print(output.relative_to(ROOT))
        return 0
    except (ValueError, OSError, ImportError):
        print('Falha: confira o formato, arquivos, destino e dependencia opcional reportlab. Nenhum resultado de auditoria foi inferido.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
