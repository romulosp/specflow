# Workflow Spec Driven

## Fonte oficial

Este documento é a regra canônica de processo. `AGENTS.md` impõe as regras gerais; Skills descrevem a execução de cada etapa; documentos em `changes/` mantêm a evidência de uma mudança específica.

[Regras consolidadas](regras-consolidadas.md) registra as determinações e sua precedência, incluindo cobertura, segurança, teste humano e requisitos futuros de configuração/apps. Sua consolidação não aprova SPEC, arquitetura ou publicação.

Comandos locais e diagrama: [docs/comandos/COMANDOS.md](../../../docs/comandos/COMANDOS.md). Revisão técnica favorável recomenda aceite; SPEC_APROVADA e APROVADA humanas exigem decisão explícita sobre a revisão corrente. Planejamento preparatório sucede SPEC_APROVADA. Encerramento segue a política da Change; não executa commit ou archive por mera invocação do comando.

Na validação formal, security-audit e o [gate local de segurança](../../../docs/security-audit/GATE-SEGURANCA.md) são obrigatórios. Achado aberto ou evidência insuficiente mantém a fase pendente, sem promover VALIDADA ou aprovação. Checks técnicos durante implementação não substituem esse gate. O fluxo composto specflow-teste-humano para em IMPLEMENTADA antes das fases formais posteriores, entregando artefato utilizável e roteiro para o usuário testar.

`specflow-validar` é o comando padrão da fase de validação da implementação. Quando um fluxo autorizado alcançar essa fase, execute-o sem nova instrução rotineira. A única exceção é solicitação explícita do prompt do usuário para não executar a fase, inclusive um limite explícito de parada anterior. Nesse caso, registre a revisão, a referência da solicitação e a não execução em validation.md e na memória, mantendo os gates posteriores pendentes. Não promover VALIDADA, APROVADA ou ARQUIVADA por dispensa. Falha de teste/segurança ou ausência de ferramenta não autoriza omissão; pedir apenas que não seja gerado PDF também não dispensa a validação. A regra não estende o escopo de comandos de fase única.

## Ciclo de vida e gates

| Fase | Entrada obrigatória | Saída obrigatória | Próximo status |
| --- | --- | --- | --- |
| Especificação | `proposal.md`, `spec.md`, `DESIGN.md`, `tasks.md` | contrato completo | `EM_REVISAO_SPEC` |
| Revisão da SPEC | contrato completo | relatório `REV-*` | `SPEC_APROVADA` ou `REPROVADA` |
| Implementação | `SPEC_APROVADA` | código, configuração e testes previstos | `IMPLEMENTADA` ou `BLOQUEADA` |
| Revisão da implementação | implementação e SPEC | relatório `IMP-REV-*` | `IMPLEMENTACAO_APROVADA` ou `REPROVADA` |
| Validação | implementação aprovada; chamar `specflow-validar` por padrão | evidências `VAL-*` e gate de segurança; omissão só por prompt explícito, registrada como não executada | `VALIDADA` somente com gates satisfeitos; omissão mantém pendente |
| Aprovação | relatórios sem pendências materiais | decisão formal | `APROVADA` ou `REPROVADA` |
| Encerramento | mudança aprovada | atualização de `system/`, mudança pronta em `archive/`, commit | `ARQUIVADA` |

## Gate obrigatório da implementação

Após gerar código, codificar e executar os testes de comportamento e medir cobertura conforme [coverage-policy.md](../testing/coverage-policy.md): mínimo de 80%, meta de 90%, permitindo valores superiores. Exigir evidência por arquivo novo/alterado e agregado do escopo. Sem testes/cobertura atuais, não concluir IMPLEMENTADA ou aprovar IMPLEMENTACAO_APROVADA; retornar à implementação ou registrar bloqueio. O fluxo teste-humano também cumpre esse gate antes da entrega. Omitir validação formal por prompt não dispensa cobertura da implementação, e fallback por LLM não substitui medição.

## Planejamento técnico preparatório

Após a Change ficar `SPEC_APROVADA` e antes da implementação, registre `implementation-plan.md` na pasta da Change. Esse artefato descreve impactos prováveis, estratégia, testes unitários e de integração, qualidade, segurança, riscos e decisões técnicas. Ele não cria uma nova fase, não altera os gates acima e não modifica `proposal.md`, `spec.md` ou `DESIGN.md`.

## Regras de retorno

- Falha de clareza retorna para especificação.
- Divergência de código retorna para implementação.
- Falha de teste retorna para implementação ou para a SPEC, conforme a causa.
- A aprovação e o commit nunca corrigem código ou requisitos.

## Estrutura obrigatória de uma mudança

```text
specs/changes/<id>-<nome>/
├── proposal.md
├── spec.md
├── DESIGN.md
├── tasks.md
├── implementation-plan.md
├── validation.md
└── reviews/
```

`proposal.md` registra objetivo e escopo. `spec.md` define comportamento verificável. `DESIGN.md` registra como a solução será estruturada. `tasks.md` permite acompanhar a execução. `implementation-plan.md` registra o plano técnico preparatório sem alterar o contrato aprovado. `validation.md` contém evidências objetivas.
