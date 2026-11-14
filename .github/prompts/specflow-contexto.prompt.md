---
description: "Retomar uma Change SpecFlow lendo estado, contrato, decisoes e pendencias sem promover gates."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-contexto

Fase: Retomada auxiliar

Entrada: Caminho da Change existente.

Saida: Resumo com fase observada, fontes, conflitos, pendencias e proxima acao permitida.

## Procedimento

1. Leia README, AGENTS, a memoria da Change, contrato, tarefas, reviews e validation.
2. Reconcilie alegacoes com evidencias; diferenca produz conflito, nao promocao automatica.
3. Informe o gate pendente e preserve o trabalho existente. Nao implemente ou registre aprovacao por este comando.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
