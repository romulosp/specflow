# Design — Núcleo autônomo SpecFlow

Revisão r6; candidato sujeito à aprovação da [SPEC](spec.md). Perfis de digest mantidos; modelos de cobertura, segurança e execução de fases reconciliados. Comandos de agente, gerador documental e futura inicialização 10030 são fronteiras separadas, não implementação existente do núcleo.

## Fronteiras e destino

Implementação futura em `framework/src/specflow/`: `contracts` valida formatos; `workflow` avalia pré-condições; `memory` reconcilia fontes; `validation` verifica matriz e evidências; `__main__` fornece harness fino. Testes em `framework/tests/`, assets novos em `framework/assets/`, consumidores sintéticos em diretórios temporários criados pelos testes. Nada existe ainda nesses caminhos.

Fluxo: harness → leitura confinada → contratos → reconciliação → avaliação/verificação → JSON. Nenhum módulo faz chamadas ao Protótipo. O núcleo não lê `AGENTS.md` como comando, não importa código do consumidor e não executa extensões. Não será criada engine genérica, servidor ou integração de agente neste incremento.

## Modelo mínimo de dados

Todos os JSON têm `schemaVersion: 1`; campos desconhecidos são rejeitados para evitar aceitação silenciosa de semântica não suportada. IDs são únicos no tipo e projeto. Caminhos de referência são relativos à raiz explicitamente selecionada e precisam resolver dentro dela, inclusive após symlinks/junctions. Arquivos textuais de entrada são UTF-8 estrito, com BOM UTF-8 inicial opcional. Digest segue o perfil explícito da SPEC; não depende de newline do sistema operacional.

### Validação com biblioteca padrão

Usar `json` para parsing com detecção de chaves duplicadas e rejeição de NaN/Infinity, e validadores específicos por tipo de registro para estrutura, campos, tipos, enums e referências. Inteiros exigem `type(value) is int`, evitando aceitar booleanos como inteiros. Erros usam campo e fonte relativos, sem ecoar valores. As definições de contrato são tabelas/descritores restritos compartilhados com documentação e testes; não construir interpretador genérico de JSON Schema. Regras de referência e ciclos são validação de domínio, separadas do parsing. Esse trabalho pertence explicitamente à T03.

| Registro | Campos obrigatórios e invariantes |
| --- | --- |
| project.json | projectId, policyId, policyVersion, policyDigest, changesPath, knowledgePath; caminhos locais confinados e distintos dos assets globais; política deve corresponder à versão/digest fixados pela instalação |
| draft.json | schemaVersion=1, changeId, revision, objective, documentRefs; rascunho anterior à fase 1, sem decisão/review/manifesto de implementação aprovado; documentRefs contém proposal/spec/design/tasks/validation/memory existentes e confinados |
| change.json | changeId, revision, claimedState, contractManifest, implementationManifest, reviewRefs, evidenceRefs, decisionRefs, traceabilityRef; manifestos de implementação podem ser vazios antes de implementar |
| Manifesto | lista de path, sha256, digestProfile e role; rawSha256 opcional de auditoria; sem duplicata; contrato contém proposal/spec/design/tasks com sha256-utf8-lf-v1; identidade compara caminho, papel, perfil e digest |
| Revisão | id, kind (spec/implementation), reviewer, targetManifest, findings; findings com id, severity (info/minor/material), status (open/resolved) e fonte |
| Decisão | id, kind (spec/final), actor, occurredAt com offset, scope, targetManifest, outcome (approved/rejected), rationale, sourceRef, supersedes opcional; registro real exige fonte humana, fixture deve declarar natureza sintética |
| Evidência | id, targetManifest, criterionIds, method (enum obrigatório structural/functional/manual), command, cwd relativo, environment, expectedCode, actualCode, outcome (passed/failed/not_run), artifactRefs e artifactManifest; manifesto cobre exatamente as referências, com digests atuais; códigos negativos esperados podem passar, not_run nunca passa |
| Conhecimento | id, kind (decision/lesson/pending), sourceRefs; decisão tem alternativas, motivo, status e supersedes; lição tem incidente, ação e aplicabilidade; pendência tem impacto e próxima ação |
| Rastreabilidade | lista de requirementId, acceptanceId, taskIds, artifactRefs, evidenceIds, requiredMethod (enum obrigatório structural/functional/manual); comparação de método por igualdade, sem hierarquia implícita; ausência antes de implementar é reportada para a fase pretendida, sem fingir conclusão |

### Digests

`sha256-utf8-lf-v1`: ler bytes, `decode('utf-8-sig', errors='strict')`, substituir `\r\n` por `\n` e então `\r` por `\n`, codificar UTF-8 e calcular SHA-256. Não chamar strip, normalização Unicode ou serialização JSON. O BOM removido é somente o inicial; U+FEFF interno é conteúdo. `sha256-bytes-v1`: SHA-256 direto dos bytes. O perfil faz parte do vínculo da aprovação; não trocar automaticamente em upgrades.

Nos quatro documentos contratuais só o perfil textual é permitido. `rawSha256` registra integridade do transporte, mas não integra a igualdade de aprovação canônica; divergência nele pode ser informada como diagnóstico sem bloquear por mera mudança de representação. Manifestos r1 continuam históricos, com sua semântica de bytes exatos, e não são convertidos em aprovações r2. Testes devem cobrir LF/CRLF/CR/BOM, UTF-8 inválido, newline final, espaço, caractere e alteração de binário.

Uma decisão `spec` vincula os quatro documentos contratuais. A decisão `final` vincula contrato e manifesto de implementação validado. Não incluir o próprio registro de aprovação no manifesto que ele aprova, evitando hash circular. Evidências e revisões apontam esses mesmos manifestos. Datas servem para proveniência, nunca para decidir sozinhas o estado. Ciclos em supersessão são erro de entrada.

scope da decisão é objeto fechado com projectId, changeId e revision, comparados ao consumidor/Change/revisão selecionados; não é texto livre interpretado por heurística. Escopo malformado retorna 2; escopo válido de outro consumidor ou revisão retorna 1, mesmo se os quatro hashes coincidirem. Isso previne reaproveitamento acidental de decisão sem alegar autenticação de quem pode reescrever registros.

Fontes autoritativas: política selecionada, arquivos atuais, revisões, evidências e decisões referenciadas. STATUS/memória narrativa fornecem alegações a reconciliar. Uma alegação contraditória não substitui a fonte: gera conflito, estado INDETERMINADO e bloqueio de avanço. Ausência de decisão é pendência, não decisão negativa inventada. Não pesquisar recursivamente fora das pastas configuradas.

## Interfaces propostas do harness

Invocações após implementação, a partir de `framework/`, com pacote local instalado em ambiente isolado ou `PYTHONPATH=src`:

```text
python -B -m specflow check --project <raiz> --change <id> --target <estado>
python -B -m specflow context --project <raiz> --change <id>
python -B -m specflow evaluate --project <raiz> --change <id> --target <estado>
```

IDs aceitos: `[A-Za-z0-9][A-Za-z0-9_-]{0,79}`. `--project` é a única raiz externa explicitamente fornecida; as referências internas não podem ser absolutas nem conter segmentos `..`. Estado desconhecido, arquivo malformado/inacessível ou quebra de confinamento: erro 2. Violação de política ou conflito em entrada válida: 1. Avaliação/checagem satisfeita no escopo: 0. `context` usa 1 se há conflito ou pendência obrigatória da fase, 0 quando reconciliado.

Prioridade de saída: 2 para erro de entrada/execução, depois 1 para violação/conflito/pendência obrigatória e por último 0. INDETERMINADO por divergência de fontes válidas é sempre 1, nunca sucesso parcial. Método ausente/desconhecido é erro 2 de contrato; método conhecido mas diferente do exigido é violação 1. O campo method é declaração estruturada inspecionável, não heurística de linguagem natural nem prova independente de execução.

Referência ausente no schema/grafo de IDs, arquivo obrigatório de projeto/contrato ausente e erro de leitura de arquivo presente são erros 2. Arquivo de evidência declarado por um registro estruturalmente válido, mas ainda não produzido, é pendência 1; hash divergente também é 1. Essa distinção evita tratar falta esperada de prova como JSON malformado, sem aceitar um contrato inválido. Aplicar sempre o escopo e a fase solicitados; não exigir evidência futura para uma leitura válida de rascunho.

Envelope: `schemaVersion`, `operation`, `projectId`, `changeId`, `observedState`, `requestedState` (null para context), `allowed` (null para context), `findings`, `sources`, `decisions`, `lessons`, `pending`, `nextSteps`, `limitations`, `exitCode`. Findings contêm id, severity, source, method e reason, sem corpo dos documentos. Saída JSON com chaves ordenadas e listas ordenadas por ID/caminho; sem relógio de execução ou caminho absoluto dependente da máquina. Diagnóstico de erro também usa esse envelope, com campos indisponíveis em null.

`evaluate` responde se a transição pode ocorrer, mas não a aplica. `check` verifica integridade e rastreabilidade necessárias ao alvo informado. `context` reconcilia sem alvo. A política deve ser carregada exclusivamente dos assets fixados do núcleo; consumidor não pode trocar política no meio da avaliação por texto narrativo.

Reconhecer draft.json antes de exigir change.json. Draft válido sozinho: context retorna observedState=RASCUNHO, allowed=null e código 0; próximos passos indicam completar/revisar o contrato. check/evaluate de avanço retornam 1/DRAFT_CONTRACT_INCOMPLETE, sem inventar decisão. RASCUNHO não é alvo de promoção nem uma fase adicional. Se os dois registros válidos coexistirem, retornar INDETERMINADO/código 1; JSON inválido mantém prioridade 2. Se nenhum existir, erro 2. Especificação concluída substitui somente os metadados de rascunho por change.json mediante ação explícita do agente, nunca por leitura.

## Integridade, aprovação e segurança

Não confiar apenas no campo approved: verificar tipo de decisão, ator não vazio, escopo, fonte, manifesto, ausência de supersessão e relatórios dependentes. O produto apenas verifica consistência do registro; um operador com escrita pode falsificar registros. Autenticação e assinatura ficam fora do incremento, limitação exibida no relatório.

Sem indexação persistente neste incremento. Ler memória não executa shell nem inicia adaptador. Testes de confinamento incluem symlink/junction quando suportado; indisponibilidade deve ficar explícita. Nenhum teste precisa acessar conteúdo real de credenciais, logs ou pagamentos.

## Registros adicionais da r6

Todos incluem schemaVersion=1, ID, targetManifest atual e referências relativas confinadas. Contratos específicos do domínio não são JSON Schema genérico.

| Registro | Campos e verificação |
| --- | --- |
| Cobertura | scope com todos os arquivos implementados, metric (lines/statements), files com path/covered/total, reportRefs, testEvidenceRefs e exclusions com justificativa/fonte contratual. covered/total inteiros exatos, 0 <= covered <= total; comparar 100*covered >= 80*total por arquivo e agregado; total zero requer não aplicabilidade, não passa como 100%. Excluir testes/dependências do denominador sem excluir código autoral |
| Segurança | auditRef, gateRef, auditDigest/gateDigest, targetManifest, exitCode, status e findingRefs. Referências atuais, relatório e gate coerentes, qualquer finding aberto bloqueia; nenhum processo é executado pela leitura. Alteração dos artefatos exige novas evidências, mesmo se o JSON antigo disser verificada |
| Execução de fase | phase, outcome (completed/failed/not_run), sourceRef, reason e targetManifest. not_run de validação requer solicitação explícita do usuário e nunca satisfaz pré-condição de aprovação |
| Entrega humana | artifactManifest, quickstartRef, scenarioIds e outcomes (passed/failed/not_run), actor/sourceRef quando realizado. Preparar roteiro não converte not_run em passed; entrega utilizável/IMPLEMENTADA requer gate técnico antes da parada |

Vinculação das evidências: Cobertura recebe testManifest com todos os arquivos de teste usados e artifactManifest para reportRefs/testEvidenceRefs. Segurança recebe evidenceManifest com todos os evidenceRefs de checks/findings do audit, sem lacunas ou extras; audit/gate e manifesto-alvo são verificados separadamente para evitar autorreferência. Artefatos de evidência usam sha256-bytes-v1; documentos contratuais conservam o perfil textual. O núcleo compara caminho/papel/perfil/digest com os bytes atuais. Exclusões do escopo de segurança precisam de justificativa rastreável na matriz; código novo/alterado não some do escopo por editar o audit.

Papéis nesses manifestos especializados: test para cada item de testManifest; report para reportRefs; evidence para testEvidenceRefs e para cada item de evidenceManifest da segurança. Não inferir papel pela extensão ou nome. A mesma referência citada em mais de um finding/check aparece uma única vez no manifesto, sem perder a correspondência com todos os IDs citantes. Manifesto de evidência não inclui audit/gate/binding autorreferentes; o registro de segurança liga esses digests separadamente. Perfil/papel malformado retorna 2; arquivo ausente ou digest desatualizado em registro válido retorna 1.

O verificador de suporte v1 confere presença e hashes de fontes declaradas, mas não vincula os bytes de todos os logs/testes citados. Portanto seu código 0 é necessário e insuficiente: o core/CLI precisa conferir os novos manifestos antes de considerar os registros atuais. Não alegar que esse endurecimento já está implementado no helper existente.

`change.json` recebe coverageRefs, securityRefs, phaseExecutionRefs e handoffRefs (listas vazias nos estágios anteriores); validadores rejeitam campos desconhecidos. A matriz requirement/acceptance/task/artifact/evidence confere escopo exato da cobertura; escopo declarado incompleto não pode liberar arquivo implementado. Sem Git, o manifesto de escopo de implementação é obrigatório, sem presumir descoberta de diff inexistente.

Init/recursos/.properties e geração em apps são implementados pela Change 10030, que consome estes contratos e nunca torna recurso DEFINIR executável. Recurso obrigatório inativo é pendência, não evidência de sucesso. O núcleo continua sem executar infraestrutura, sem novas credenciais em registros/lock e sem promover estados apenas pelo nome do arquivo.

## Estratégia de entrega

Primeiro biblioteca e testes de contrato/gates; depois harness e dois consumidores independentes; por fim validação e manual. Gerar manifesto do código/fixtures entregues para vincular o teste manual a uma revisão real. Um zip/wheel e instalador de produto pertencem ao incremento seguinte; não criar distribuição própria além do necessário ao harness antes de comprovar o núcleo.
