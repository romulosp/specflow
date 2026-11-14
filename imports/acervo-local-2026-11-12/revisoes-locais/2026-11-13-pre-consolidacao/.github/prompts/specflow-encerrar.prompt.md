---
description: "Preparar encerramento de Change SpecFlow aceita e efetivar archive ou commit apenas com autorizacao aplicavel."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-encerrar

Fase: 7. Encerramento

Entrada: APROVADA humana da revisao corrente e autorizacao delimitada das acoes de encerramento.

Saida: System atualizado, candidato de archive verificado e recibo de encerramento; ARQUIVADA apenas apos acoes efetivas autorizadas.

## Procedimento

1. Confirme aprovacao humana e politica de encerramento da Change. Prepare atualizacao de system e candidato de archive; nao mova automaticamente.
2. Verifique Git real sem inicializa-lo como efeito colateral. Neste workspace sem Git, nao execute git-commit nem afirme commit existente.
3. A skill git-commit so se aplica se houver repositorio e autorizacao explicita para commit/encerramento. A politica da Change e AGENTS prevalecem sobre sequencias legadas de prompts.
4. Apos acoes autorizadas, registre recibo posterior com localizacao e hash quando aplicavel, sem circularidade. Sem autorizacao ou acao efetiva, mantenha APROVADA com encerramento pendente. Publicacao nunca e implicita.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
