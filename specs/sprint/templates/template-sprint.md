# Sprint: <identificacao>-<nome>

## Identificação

- **Nome:** <nome da Sprint>
- **Status:** `PLANNED`
- **Período (opcional):** <data inicial> a <data final>
- **Critério de sucesso do Sprint Goal:** <evidência objetiva de que o resultado foi atingido>

## Sprint Goal

<resultado objetivo que a Sprint pretende alcançar>

## Itens da Sprint

| Ordem | Referência da Change | Prioridade | Risco | Fase/gate atual | Status | Dependência | Evidência | Observação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `<id>-<nome>` | <alta/media/baixa> | <segurança/negócio/técnico e impacto> | <gate do workflow> | `PLANNED` | <nenhuma ou referência> | <documento ou evidência atual> | <observação operacional> |

> Requisitos e critérios de aceite pertencem exclusivamente às Changes e SPECs referenciadas. Esta Sprint registra somente planejamento e acompanhamento operacional.

## Estados

### Estados da Sprint

- `PLANNED`
- `ACTIVE`
- `COMPLETED`
- `CANCELLED`

### Estados da Change na Sprint

- `PLANNED`
- `READY`
- `IN_PROGRESS`
- `DONE`
- `BLOCKED`
- `REMOVED`

## Governança e evidências por fase

| Marco da Change | Documentação ou evidência obrigatória | Condição para avançar |
| --- | --- | --- |
| Especificação | `proposal.md`, `spec.md`, `DESIGN.md` e `tasks.md` | contrato completo para revisão |
| Revisão da SPEC | relatório `REV-*` e estado `SPEC_APROVADA` | Change pode receber plano técnico e ficar `READY` |
| Planejamento técnico | `implementation-plan.md` com impactos, testes, segurança, riscos e decisões | implementação preparada sem alterar a SPEC |
| Implementação | código, configuração, testes e `tasks.md` atualizados | revisão da implementação possível |
| Revisão e validação | relatório `IMP-REV-*`, `validation.md`, comandos, resultados e evidências | não há falha ou pendência material |
| Segurança | evidências da Skill `security-audit` e relatório atual | não há achado confirmado em aberto |
| Aprovação e encerramento | aprovação final, atualização de `system/`, arquivamento e hash do commit | Change pode ficar `DONE` |

## Definition of Ready

Uma Change fica `READY` quando:

- possui objetivo claro;
- possui `proposal.md`, `spec.md`, `DESIGN.md` e `tasks.md` completos;
- possui `proposal.md` e `spec.md` em `SPEC_APROVADA`;
- possui `implementation-plan.md` rastreável;
- dependências estão concluídas ou explicitamente resolvidas;
- critérios de aceite são verificáveis;
- riscos de segurança e de negócio conhecidos estão registrados e possuem tratamento ou decisão;
- não há bloqueio conhecido.

## Definition of Done

Uma Change fica `DONE` na Sprint somente quando:

- a implementação está concluída;
- a revisão de implementação está concluída;
- a validação está concluída;
- a aprovação final está registrada;
- o encerramento tem recibo e evidências da política aprovada; se commit for exigido/aplicável, ele foi autorizado e realizado após o aceite final, sem inventar Git ou commit;
- `system/` foi atualizado e a Change foi arquivada;
- as evidências exigidas pela SPEC estão registradas.

### Testes unitários

- Todo código de produção possui testes unitários quando aplicável.
- Para código Java, toda classe `.java` de produção possui classe de teste correspondente, inclusive quando tiver comportamento simples.
- A classe de teste segue a convenção de nomenclatura adotada no projeto e, quando disponível, a Skill `java-unit-test` é usada para criar, revisar ou validar os testes Java.
- Para front-end, componentes, serviços, hooks, utilitários e regras de negócio possuem testes unitários quando aplicáveis.
- Se não houver estrutura de testes de front-end, a ausência é registrada como impedimento ou decisão necessária para a Change; não se cria essa estrutura automaticamente.

### Testes de integração

- Todo comportamento que dependa de API, persistência, autenticação, autorização, integração externa, configuração ou ciclo de vida do framework possui teste de integração quando aplicável.
- A estratégia e os resultados dos testes de integração são registrados em `implementation-plan.md` e `validation.md`.
- Falha de teste de integração ou cenário aplicável sem evidência impede o status `DONE`.

### Cobertura

- Toda implementação de código exige testes codificados/executados e cobertura medida mínima de 80% por arquivo/escopo implementado; meta de 90%, permitindo valores superiores, conforme specs/shared/testing/coverage-policy.md. Código gerado pelo agente está incluído.
- A validação respeita as métricas efetivamente configuradas no Sonar e na ferramenta de cobertura do projeto.
- Percentual exige medição reproduzível da revisão atual. Sem ferramenta/relatório atual ou abaixo do piso, manter a implementação bloqueada; auditoria por LLM ou teste manual não substitui cobertura. Não concluir IMPLEMENTADA, IMPLEMENTACAO_APROVADA ou DONE sem esse gate. Artefato sem código executável exige não aplicabilidade justificada, sem percentual fictício.
- Não são usados testes artificiais, exclusões indevidas ou alterações de configuração apenas para elevar a cobertura.

### Documentação de código

- Código Java novo ou alterado possui JavaDoc adequado, especialmente em classes, interfaces, métodos públicos e elementos de propósito não evidente.
- Código de front-end novo ou alterado possui documentação conforme o padrão do projeto, principalmente em componentes públicos, hooks, serviços, integrações, contratos e regras de negócio relevantes.
- Comentários explicam intenção, regra ou decisão, sem apenas repetir o código.
- README ou documentação de uso são atualizados quando a Change alterar funcionalidade, integração, execução, contrato de API ou arquitetura relevante.

### Qualidade e Sonar

- Quando Sonar e cobertura estiverem configurados e operacionalmente disponíveis no módulo, suas verificações de qualidade são aprovadas.
- Quando não houver Sonar ou cobertura configurados no módulo, ou quando Docker, Sonar, scanner, token ou dependência necessária ao Sonar estiverem operacionalmente indisponíveis, execute a Auditoria de Qualidade Assistida por LLM. Rode build, tipo, lint e testes disponíveis; relacione os artefatos alterados aos testes unitários e de integração aplicáveis; e revise bugs, vulnerabilidades e hotspots de segurança, tratamento de erro, duplicação, código morto, complexidade desnecessária e documentação.
- A auditoria assistida registra em `validation.md` o motivo do fallback, o módulo, os arquivos analisados, os comandos, resultados, mapeamento de testes, achados e correções. Ela não declara percentual de cobertura nem afirma que o Sonar foi executado; a Skill `security-audit`, quando aplicável, continua obrigatória.
- Quando o Sonar exigir uma classe de teste correspondente para cada classe Java, o requisito é obrigatório, inclusive para classes simples.
- Problemas de qualidade, testes ausentes/falhos, cobertura abaixo de 80%, medição ausente/desatualizada ou ferramenta de cobertura indisponível impedem DONE para implementação de código. Fallback de qualidade por LLM não dispensa esse gate.
- Exceções são permitidas somente quando registradas explicitamente como decisão, com justificativa e aprovação definida pelo processo do projeto.

### Auditoria de segurança

- Na validação formal, specflow-validar executa obrigatoriamente a skill security-audit e o script do gate local, conforme specs/shared/process/workflow.md. Qualquer achado aberto ou evidência incompleta deixa a fase pendente; omissão de fase só por prompt explícito, registrada sem VALIDADA/aceite.
- A auditoria cobre todos os artefatos de frontend e backend presentes no escopo da Change e avalia, quando aplicáveis, autenticação, autorização, isolamento, IDOR, segredos, entradas, XSS e injeção conforme a Skill.
- O resultado registra auditoria atual, security-gate.json e evidências em validation.md. PDF somente se solicitado, com dados atuais e inspeção visual de todas as páginas; não substitui análise/gate nem autoriza reutilizar conclusões antigas.
- Se o gerador não puder representar os resultados atuais da auditoria, a Change fica `BLOCKED` até que exista relatório verificável; não se usa um PDF histórico para liberar o status `DONE`.
- Todo achado de segurança confirmado impede o status `DONE`. Categorias não aplicáveis e limitações precisam estar justificadas por evidência; ausência de análise não prova conformidade.
- Achado confirmado deve ser corrigido autonomamente dentro do escopo da Change, sem aguardar nova instrução. Após a correção, a Change retorna às revisões e validações necessárias e a auditoria de segurança é executada novamente.
- Se a correção exigir alteração da SPEC, ação externa ou decisão fora do escopo aprovado, a Change fica `BLOCKED` e não pode ser marcada como `DONE`.
- Para Change exclusivamente documental, registre em `validation.md` a não aplicabilidade e os artefatos inspecionados; não gere nem reutilize PDF histórico de segurança.

## Eventos e decisões

Registre aqui somente eventos operacionais. Decisões com impacto duradouro pertencem à seção **Decisões importantes**.

| Data | Tipo | Registro |
| --- | --- | --- |
| <aaaa-mm-dd> | <evento ou decisão> | <descrição objetiva> |

## Sprint Review

- **Objetivo original da Sprint:** <Sprint Goal planejado>
- **Critério de sucesso e resultado observado:** <critério definido no início e evidência do resultado>
- **Changes planejadas e resultado de cada uma:** <referência e resultado>
- **Entregas concluídas:** <lista objetiva>
- **Itens removidos, bloqueados ou pendentes:** <lista e justificativa>
- **Evidências relevantes:** <referências a evidências>
- **Auditoria de segurança:** <escopo, resultado, relatório atual e achados resolvidos ou bloqueios>
- **Documentação atualizada:** <documentos atualizados>
- **README da raiz:** <avaliar atualização quando a entrega alterar uso, execução, arquitetura, API ou funcionalidade visível>
- **Principais mudanças entregues:** <mapeamento objetivo>

## Decisões importantes

| Data | Decisão | Contexto | Impacto |
| --- | --- | --- | --- |
| <aaaa-mm-dd> | <decisão relevante> | <contexto> | <impacto> |

## Retrospectiva e ações para a próxima Sprint

> Esta retrospectiva é a memória ativa do processo e deve ser lida durante o planejamento da próxima Sprint.

| Categoria | Registro | Ação para a próxima Sprint |
| --- | --- | --- |
| <o que funcionou bem / o que pode melhorar / lição aprendida> | <registro objetivo> | <ação objetiva> |
