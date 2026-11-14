---
name: implementation-validate
description: 'Use when: validar uma implementação aprovada em revisão, executar testes e registrar evidências contra validation.md.'
argument-hint: 'Informe o caminho da mudança a validar.'
---

# Validação de implementação

Este é o procedimento técnico da fase cujo comando padrão é `specflow-validar`. Em fluxo autorizado que alcance essa fase, execute a validação por padrão, sem exigir pedido separado. Se o prompt do usuário explicitamente excluir a fase ou determinar parada anterior, não execute seus checks; registre solicitação, motivo, revisão e não execução em validation.md e na memória, mantendo aprovação e encerramento pendentes, sem VALIDADA. Não interpretar ausência de ferramenta, falha ou pedido de omitir apenas PDF como dispensa. Não invocar specflow-validar de volta quando ele já estiver conduzindo este procedimento.

1. Confirme `IMPLEMENTACAO_APROVADA`, leia os critérios de aceite e a estratégia de testes.
   Reconcilie os relatórios de cobertura com a revisão atual conforme `specs/shared/testing/coverage-policy.md`: mínimo 80%, meta 90%, sem teto. Se faltarem testes/medição ou a evidência estiver abaixo do piso/desatualizada, não mantenha o gate técnico como satisfeito; registre a pendência e retorne à implementação, sem criar testes ou corrigir código nesta fase.
2. Execute os testes e verificações aplicáveis sem ocultar falhas ou avisos relevantes.
3. Registre em `validation.md`: ambiente, versões, comandos, código de saída, cenários, resultado e evidências `VAL-001`.
4. Antes de concluir VALIDADA, chame obrigatoriamente a skill local security-audit e execute `python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>` conforme `docs/security-audit/GATE-SEGURANCA.md`. Qualquer achado aberto, check falho/não executado, auditoria ausente/incompleta/desatualizada ou erro do script mantém a validação pendente, sem VALIDADA nem avanço para aprovação. Registre as razões em validation.md e retorne à implementação para correções; após revisão técnica atual, repita auditoria e gate. O gerador de PDF não substitui essa verificação.
5. Não altere código durante a validação; retorne à implementação ou à SPEC conforme a causa da falha.
