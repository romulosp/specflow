---
description: "Consolidar evidencias e registrar aceite humano final da revisao SpecFlow testada, sem fabricar aprovacao."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-aprovar

Fase: 6. Aprovacao humana

Entrada: Revisao validada, cenarios manuais aplicaveis aprovados e ausencia de pendencias materiais.

Saida: Decisao APR ligada a fonte humana, escopo e manifesto; APROVADA somente apos aceite explicito.

## Procedimento

1. Use o guia local specs/shared/process/helpers/change-approve.md. Confira relatorios, revisao validada e resultado manual da mesma entrega.
2. Se faltar evidencia ou teste, informe a condicao e mantenha pendente. Invocar este comando pede a fase de aprovacao, nao significa por si so que o usuario aprovou o produto.
3. Apresente o resultado concreto e obtenha decisao humana explicita, aproveitando aceite ja dado para a mesma revisao. Registre fonte, escopo, motivo e hashes.
4. Nao execute commit, archive, push, deploy ou publicacao como efeito do aceite.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
