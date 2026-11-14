---
name: specflow-especificar
description: "Criar ou revisar proposta, SPEC, design e tarefas de uma Change SpecFlow, sem implementar."
license: MIT
metadata:
  author: "Rômulo Penha"
---

# specflow-especificar

Fase: 1. Especificacao

Entrada: Objetivo e restricoes; caminho da Change se ja existir.

Saida: proposal.md, spec.md, DESIGN.md e tasks.md em EM_REVISAO_SPEC, com requisitos e aceites verificaveis.

## Procedimento

1. Descubra a Change existente antes de criar outra; escolha ID livre sem renumerar o historico.
2. Use specs/templates e as convencoes locais. Defina escopo, exclusoes, riscos, dependencias, RF, CA e tarefas rastreaveis.
3. Registre alternativas e decisoes pendentes; use docs/adr/ADR-TEMPLATE.md quando necessario, mantendo PROPOSTO.
4. Identifique revisao e manifesto dos documentos. Nao herde aprovacoes de outra Change ou revisao. Pare em EM_REVISAO_SPEC; nao produza codigo do produto.

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
