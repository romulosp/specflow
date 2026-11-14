---
name: change-approve
description: 'Use when: consolidar revisão de SPEC, revisão de implementação e validação para aprovar ou reprovar uma mudança.'
argument-hint: 'Informe o caminho da mudança a aprovar.'
---

# Aprovação de mudança

1. Confirme `SPEC_APROVADA`, `IMPLEMENTADA`, `IMPLEMENTACAO_APROVADA` e `VALIDADA` sem pendências bloqueantes ou importantes.
2. Prepare `AAAA-MM-DD-approval.md` em `reviews/`, com pré-condições e evidências. Registre decisão `APR-001` e veredito `APROVADA` somente após manifestação humana explícita sobre a revisão entregue; sem ela, mantenha aprovação pendente. Não fabrique decisão por testes verdes.
3. A aprovação não corrige código, não executa testes e não cria requisitos.
4. Quando houver aprovação humana, registre o escopo e a revisão em `STATUS.md`. A Skill `git-commit` só pode ser acionada com autorização de commit/encerramento aplicável; não a execute automaticamente.
5. Não atualize `system/` nem mova para `archive/` antes da aprovação.
