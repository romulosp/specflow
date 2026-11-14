---
name: spec-implement
description: 'Use when: implementar uma mudança Spec Driven cuja SPEC foi aprovada, seguindo DESIGN.md e tasks.md.'
argument-hint: 'Informe o caminho da mudança aprovada.'
---

# Implementação orientada a SPEC

1. Confirme `SPEC_APROVADA` em `proposal.md` e `spec.md` antes de editar código.
2. Leia `spec.md`, `DESIGN.md`, `tasks.md`, `AGENTS.md` e `specs/shared/process/workflow.md`.
3. Implemente somente os itens aprovados; alterações novas exigem outra mudança ou revisão da SPEC.
4. Para todo código implementado, crie/atualize e execute testes de comportamento, incluindo erros e limites. Meça a cobertura conforme `specs/shared/testing/coverage-policy.md`: mínimo de 80% por arquivo no escopo implementado e agregado; meta de 90%, podendo superar. Código gerado pelo agente não é exclusão. Registre revisão/hashes, inventário, testes, comando, ferramenta/versão, métricas e relatório atual em validation.md. Não estime percentual nem use fallback por LLM para dispensá-lo.
5. Só finalize `IMPLEMENTADA` após suíte aprovada e evidência atual do piso de cobertura. Relatório ausente/desatualizado, cobertura insuficiente ou ferramenta indisponível mantém em andamento/bloqueada; registre motivo e condição de desbloqueio. Não revise, valide ou aprove a própria entrega nesta fase. Pedido de não executar validação formal não dispensa este gate técnico.
