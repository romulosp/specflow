---
name: specflow-implementar
description: "Implementar apenas tarefas autorizadas de uma Change SpecFlow com SPEC_APROVADA corrente e plano preparatorio."
license: MIT
metadata:
  author: "Rômulo Penha"
---

# specflow-implementar

Fase: 3. Implementacao

Entrada: Change aprovada e implementation-plan existente.

Saida: Codigo e testes executados com cobertura atual minima de 80%, meta 90%, tarefas e evidencias; IMPLEMENTADA somente com gate atendido, ou em andamento/BLOQUEADA com razao.

## Procedimento

1. Confirme decisao humana de SPEC_APROVADA e validade da revisao, plano preparatorio e escopo de escrita.
2. Use o guia local specs/shared/process/helpers/spec-implement.md. Para todo codigo implementado, codifique e execute testes de comportamento e meca cobertura conforme specs/shared/testing/coverage-policy.md: minimo 80% por arquivo novo/alterado e agregado do escopo, meta 90%, aceitando valores superiores. Inclua codigo gerado pelo agente. Registre inventario arquivo-teste-aceite, revisao/hashes, comando/cwd, ferramenta/versao, metricas e relatorio. Suíte falha, medicao ausente/desatualizada ou valor abaixo do piso impede IMPLEMENTADA e IMPLEMENTACAO_APROVADA. LLM ou falta de Sonar nao dispensam cobertura.
3. Retorne a especificacao para mudanca de requisito; nao altere contrato para fazer uma falha desaparecer. Preserve pendencias de humano/ambiente. Omitir a validacao formal por prompt nao dispensa testes/cobertura da implementacao.
4. Nao aprove, arquive, publique ou crie commits automaticamente. Sem satisfazer o gate de testes/cobertura, mantenha em andamento/bloqueada e registre a condicao de desbloqueio; finalize IMPLEMENTADA apenas com evidencia atual suficiente. Atualize a memoria.

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
