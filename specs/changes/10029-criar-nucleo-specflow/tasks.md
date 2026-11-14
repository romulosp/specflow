# Tarefas — Change 10029

Estado: `EM_REVISAO_SPEC`. Nenhuma tarefa de implementação iniciada.

| ID | Estado | Entrega e caminho | Dependências | Verificação |
| --- | --- | --- | --- | --- |
| P01 | concluída | proposal, spec, DESIGN, tasks e roteiro r6 nesta Change; revisão técnica r1 tratada, suporte separado e identificadores neutralizados | pedido do usuário | revisão documental registrada em validation.md |
| G01 | pendente humana | Aceitação DEC-01, direção autônoma DEC-02 e memória local DEC-03; copyright/MIT autoral já determinados expressamente, direitos de terceiros separados | P01 | manifestação explícita com escopo; não aprova extração adicional/publicação |
| G02 | pendente humana | SPEC_APROVADA r6 e manifesto contratual | G01 | fonte da aprovação ligada aos hashes e perfis; nenhuma herança de 10028 ou do parecer condicionado de r1 |
| T01 | não iniciada | implementation-plan.md: impactos, estratégia, testes, segurança e ordem real | G02 | plano registrado antes de código, sem alterar contrato aprovado |
| T02 | não iniciada | framework/assets/policy-v1.json e schemas novos | T01 | RF-01/02/03/05; política cobre sete fases e retornos |
| T03 | não iniciada | framework/src/specflow/contracts/, validadores específicos com stdlib, perfis de digest, drafts e manifestos de evidência | T02 | CA-01/04/10/15/16; tipos estritos, duplicatas, UTF-8, normalização, hashes e confinamento |
| T04 | não iniciada | framework/src/specflow/workflow/ | T03 | CA-02..05; positivo e negativo por gate, contrato alterado |
| T05 | não iniciada | framework/src/specflow/memory/ | T03/04 | CA-06/07/16; rascunho, conflito draft/change, ausência, supersessão, isolamento |
| T06 | não iniciada | framework/src/specflow/validation/ | T03/04 | CA-08/15; rastreabilidade, métodos, manifestos de testes/logs/relatórios e política fixa |
| T07 | não iniciada | framework/src/specflow/__main__.py e configuração local | T04..06 | CA-06/09; JSON determinístico, INDETERMINADO retorna 1 em context, prioridade 2 > 1 > 0 e leitura sem escrita |
| T11 | não iniciada | Contratos/política de cobertura, segurança, omissão, entrega, integridade e rascunho (RF-12..16) | T02..T07 | CA-12..16; limites, evidência alterada, política adulterada, draft e omissão sem promoção |
| T08 | não iniciada | framework/tests/ com dois consumidores sintéticos | T07/T11 | CA-01..16; nenhum caminho runtime da origem ou rede |
| T09 | não iniciada | reviews/implementation-review.md | T08 | confronto com SPEC, achados e correções; não é aceite humano |
| T10 | não iniciada | evidências de execução, manifesto do build e quickstart real | T09 | testes pertinentes e smoke; limitações Windows/Linux explícitas |
| G03 | pendente futura | teste manual da revisão entregue | T10 | executar cenários M01..M12 do quickstart; registrar observado |
| G04 | pendente humana | aceite final desta revisão | G03 | decisão humana explícita após cenários aplicáveis passarem |

Planejamento de todos os demais incrementos em [ROADMAP-SPECFLOW](../../ROADMAP-SPECFLOW.md); tarefas futuras não representam implementação autorizada nem concluída.
