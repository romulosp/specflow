---
name: implementation-review
description: 'Use when: comparar código implementado com uma SPEC aprovada e identificar divergências de implementação.'
argument-hint: 'Informe o caminho da mudança e do módulo implementado.'
---

# Revisão de implementação

1. Confirme que a mudança está `IMPLEMENTADA` e compare cada requisito e critério de aceite com o código, configurações e testes.
2. Verifique escopo indevido, segredos, dependências, convenções de arquitetura e aderência a `AGENTS.md`.
   Confira obrigatoriamente `specs/shared/testing/coverage-policy.md`: testes codificados e executados, suíte aprovada, relatório da revisão atual, inventário arquivo→teste e cobertura mínima de 80% por arquivo novo/alterado e agregado do escopo, com meta de 90%. Sem medição, abaixo do piso ou com relatório desatualizado, não registre IMPLEMENTACAO_APROVADA: relate achado bloqueante e retorne à implementação. Quantidade de testes, LLM e inspeção manual não substituem cobertura medida.
3. Registre divergências como `IMP-REV-001`, com severidade, evidência, impacto e ação necessária.
4. Salve `AAAA-MM-DD-implementation-review.md` em `reviews/`.
5. Conclua com `IMPLEMENTACAO_APROVADA` ou `REPROVADA`. Não altere código durante a revisão.
