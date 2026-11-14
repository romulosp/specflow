---
description: "Criar ou revisar proposta, SPEC, design e tarefas de uma Change SpecFlow, sem implementar."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-especificar

Fase: 1. Especificacao

Entrada: Objetivo e restricoes; caminho da Change se ja existir.

Saida: proposal.md, spec.md, DESIGN.md e tasks.md em EM_REVISAO_SPEC, com requisitos e aceites verificaveis.

## Procedimento

1. Descubra a Change existente antes de criar outra; escolha ID livre sem renumerar o historico.
2. Use specs/templates e as convencoes locais. Defina escopo, exclusoes, riscos, dependencias, RF, CA e tarefas rastreaveis. Para codigo, inclua testes obrigatorios e cobertura minima medida de 80%, meta 90%, conforme specs/shared/testing/coverage-policy.md; codigo gerado pelo agente nao e exclusao.
3. Registre alternativas e decisoes pendentes; use docs/adr/ADR-TEMPLATE.md quando necessario, mantendo PROPOSTO.
4. Identifique revisao e manifesto dos documentos. Nao herde aprovacoes de outra Change ou revisao. Pare em EM_REVISAO_SPEC; nao produza codigo do produto.
5. Divida spec.md em secoes por modelo de dominio com responsabilidade, conceitos, regras/invariantes e criterios de aceite; no DESIGN.md registre limites, ownership dos dados, contratos e dependencias. Justifique dominio unico ou demanda tecnica sem dominio de negocio, sem criar divisao artificial. Consulte docs/modelagem/GUIA.md.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
