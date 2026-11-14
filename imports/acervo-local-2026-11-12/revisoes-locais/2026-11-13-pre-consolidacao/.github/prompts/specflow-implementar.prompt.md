---
description: "Implementar apenas tarefas autorizadas de uma Change SpecFlow com SPEC_APROVADA corrente e plano preparatorio."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-implementar

Fase: 3. Implementacao

Entrada: Change aprovada e implementation-plan existente.

Saida: Implementacao, testes e tarefas atualizados; IMPLEMENTADA ou BLOQUEADA com razao, sem aceite final.

## Procedimento

1. Confirme decisao humana de SPEC_APROVADA e validade da revisao, plano preparatorio e escopo de escrita.
2. Use a skill local spec-implement. Implemente por dependencia; execute testes pertinentes e registre evidencias reais.
3. Retorne a especificacao para mudanca de requisito; nao altere contrato para fazer uma falha desaparecer. Preserve pendencias de humano/ambiente.
4. Nao aprove, arquive, publique ou crie commits automaticamente. Finalize a fase com estado real e atualize a memoria.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
