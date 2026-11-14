# Finalizar Sprint

Avalie o encerramento de uma Sprint sem alterar o workflow 01-06 das Changes.

## Objetivo

Confirmar se a Sprint pode ser concluída com base no estado e nas evidências de suas Changes referenciadas.

## Regras

1. Verifique todas as Changes da Sprint conforme `specs/sprint/README.md` e confirme o gate real de cada uma.
2. Para cada item candidato a `DONE`, confirme integralmente a Definition of Done do template e a documentação de cada marco: contrato, revisão da SPEC, plano técnico, implementação, revisão, validação, aprovação, atualização de `system/`, arquivamento, commit e evidências exigidas pela SPEC.
3. Antes de aceitar uma Change com código como DONE, exija testes codificados/executados e relatório atual de cobertura mínima de 80% por arquivo/escopo implementado, meta de 90%, conforme specs/shared/testing/coverage-policy.md. Confirme documentação de código, qualidade e evidências exigidas. Ausência de Sonar pode exigir auditoria por LLM de qualidade, mas ela não substitui a cobertura medida; falta de ferramenta/relatório de cobertura mantém bloqueado. Falha de build/scanner/Quality Gate disponível não é fallback.
4. Confirme validação formal por specflow-validar, auditoria security-audit e script de gate com evidências atuais. Categorias não aplicáveis devem estar justificadas, sem dispensa silenciosa do gate. Omissão de validação por prompt explícito mantém o marco não executado e não libera DONE/aceite/encerramento.
5. PDF de segurança só é exigido quando solicitado; então deve refletir a auditoria atual, sem segredos, com inspeção visual. PDF ausente sem solicitação não é bloqueio, mas auditoria/gate atual ausente ou com pendência é. Não reutilizar relatório histórico nem tratar o gerador como scanner.
6. Se a auditoria confirmar um achado de segurança, não aceite a Change como `DONE`: corrija-o autonomamente dentro do escopo aprovado, repita revisões e validações necessárias e execute a auditoria novamente. Somente uma auditoria atual sem achados confirmados permite prosseguir.
7. Se a correção exigir alteração da SPEC, ação externa ou decisão fora do escopo aprovado, registre a Change como `BLOCKED`; não solicite uma autorização para ignorar o achado e não marque `DONE`.
8. Não aceite DONE com teste ausente/falho, medição ausente/desatualizada ou cobertura abaixo de 80% no escopo implementado, inclusive quando a ferramenta estiver indisponível. Não usar exclusões artificiais, estimativas ou LLM para dispensar o piso. Problemas de qualidade, segurança, documentação e gates restantes continuam bloqueantes conforme políticas locais. Artefato sem código executável exige não aplicabilidade justificada, sem percentual fictício.
9. Registre pendências, itens `REMOVED` e bloqueios, com suas justificativas objetivas, risco e impacto de segurança ou de negócio e condição objetiva de resolução.
10. Antes de marcar a Sprint como `COMPLETED`, execute a Sprint Review:
   1. verifique as Changes e suas evidências;
   2. confirme a Definition of Done;
   3. mapeie as mudanças entregues;
   4. verifique se o README da raiz precisa ser atualizado;
   5. atualize o README somente quando houver impacto relevante e a Sprint for concreta.
11. Registre em Decisões importantes somente decisões relevantes, com data, contexto e impacto.
12. Antes de marcar a Sprint como `COMPLETED`, registre a retrospectiva com pontos positivos, problemas, lições aprendidas e ações objetivas para a próxima Sprint. Evite observações genéricas ou sem ação prática.
13. Marque a Sprint como `COMPLETED` somente depois de concluir a Review e a Retrospectiva, quando todos os itens estiverem `DONE` ou `REMOVED` com decisão registrada e quando não houver pendência.
14. Permita o status `CANCELLED` somente quando houver motivo registrado em Eventos e decisões, situação documentada de cada Change e retorno dos itens não concluídos ao backlog elegível.
15. Não crie requisitos, critérios de aceite, detalhes técnicos ou uma etapa adicional ao workflow 01-06.

## Resultado esperado

Informe se a Sprint está `COMPLETED`, permanece pendente ou está `CANCELLED`, indicando as evidências verificadas e qualquer pendência, remoção ou bloqueio registrado.
