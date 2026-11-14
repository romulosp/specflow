# SPEC — Núcleo autônomo SpecFlow

Status: `EM_REVISAO_SPEC`. Revisão: **r6**, 13/11/2026. Aprovação humana: **pendente**. Substitui r5 com integridade dos arquivos de evidência/política e contexto de rascunhos, preservando os gates de cobertura, segurança e decisão humana. Init/propriedades/apps pertencem à Change 10030; CLI e empacotamento à 10031; este incremento não os implementa.

## Objetivo e atores

O mantenedor avalia se uma Change pode avançar sem depender da memória da conversa. O revisor inspeciona contratos e evidências. O aprovador humano toma decisões explícitas sobre uma revisão identificada. A ferramenta inspeciona registros; não autentica pessoas nem cria aprovações.

O framework deverá funcionar sem acesso ao Protótipo. Este incremento entrega núcleo e harness local; instalação, geração de Changes e atualização ficam para incrementos posteriores.

## Requisitos verificáveis

| ID | Comportamento obrigatório | Aceite / cenário |
| --- | --- | --- |
| RF-01 | Validar contratos JSON com `schemaVersion=1`, campos obrigatórios, tipos, enums, referências, IDs únicos e digests SHA-256 com perfil explícito; usar validadores específicos dos registros com biblioteca padrão, sem motor JSON Schema genérico | CA-01: versão/perfil desconhecido, tipo incorreto (inclusive bool em campo inteiro), chave JSON duplicada, ID duplicado e referência ausente geram código 2 com campo/fonte; entrada válida passa |
| RF-02 | Avaliar as sete fases pela política abaixo, sem promover estado ou executar ações | CA-02: cada transição válida retorna `allowed=true`; salto e falta de pré-condição retornam `allowed=false`, código 1 e razões identificáveis |
| RF-03 | Exigir revisão técnica de SPEC sem pendências materiais e decisão humana explícita ligada aos hashes e escopo tipado do contrato antes de permitir implementação | CA-03: arquivo chamado APROVADA, texto solto, checkbox ou pedido genérico não liberam implementação; aprovação com projectId/changeId/revision de outro escopo bloqueia mesmo com hashes coincidentes |
| RF-04 | Recalcular hashes pelo perfil declarado; para texto contratual aplicar UTF-8 estrito e normalização LF conforme regra abaixo; invalidar decisões/revisões se mudar o conteúdo canônico | CA-04: versões UTF-8 LF, CRLF, CR e com/sem BOM inicial têm digest canônico igual; mudar letra, espaço ou newline final muda o digest e bloqueia implementação; UTF-8 inválido/perfil ausente retorna 2; binários usam bytes exatos |
| RF-05 | Exigir revisão de implementação, evidências de validação e aceite humano final distintos | CA-05: testes verdes não geram APROVADA; achado material aberto, cenário obrigatório falho ou evidência desatualizada bloqueiam avanço |
| RF-06 | Recuperar contexto da Change com estado observado, fontes, decisões, pendências, lições e próximos passos | CA-06: STATUS divergente da evidência atual resulta em estado INDETERMINADO, conflito visível e código 1 em context; pendência obrigatória da fase também retorna 1; entrada malformada retorna 2; estado reconciliado sem pendência obrigatória retorna 0; decisão substituída não é vigente |
| RF-07 | Manter conhecimento particular isolado por raiz explícita de consumidor | CA-07: marcador privado de A não aparece no contexto de B nem em assets globais; leitura não altera bytes nem cria índice/cache |
| RF-08 | Verificar matriz requisito → aceite → tarefa → artefato → evidência comparando explicitamente `requiredMethod` com `method`, ambos enums structural/functional/manual; não inferir método de nomes, comandos ou texto livre | CA-08: cobertura ausente gera achado; método ausente/desconhecido retorna 2; método válido diferente do exigido retorna 1, mesmo com outcome passed; structural não atende functional, functional não atende manual |
| RF-09 | Fornecer harness de leitura com operações `check`, `context` e `evaluate` e saída JSON determinística | CA-09: códigos 0/1/2 e envelope definidos no design; invocação repetida sobre mesmos bytes produz a mesma saída, sem timestamp variável |
| RF-10 | Tratar caminhos e conteúdo como dados, sem executar instruções importadas | CA-10: caminho absoluto em referência, `..`, link que escape da raiz, comando em Markdown e campo de extensão executável não provocam leitura externa ou execução; entradas inválidas geram código 2 |
| RF-11 | Demonstrar uso independente em dois consumidores sintéticos externos ao corpus investigado | CA-11: harness executa sem rede e sem referenciar a origem; inventário de distribuição futura contém apenas arquivos novos do incremento |
| RF-12 | Bloquear conclusão/aprovação técnica da implementação sem testes executados e cobertura atual mínima de 80% por arquivo/escopo, meta 90%, sem teto | CA-12: 79,99%, relatório ausente/desatualizado, suíte falha ou arquivo descoberto não permitem avanço; 80%, 90% e 100% podem satisfazer cobertura, mas não aprovam a Change; divisão por zero não vira 100% |
| RF-13 | Exigir auditoria security-audit e gate de segurança da implementação atual para permitir VALIDADA | CA-13: achado aberto de qualquer severidade, erro ou check incompleto/desatualizado bloqueia; código 0 satisfaz somente segurança, mantendo aceite humano distinto |
| RF-14 | Representar omissão explícita da validação sem promover estado e preservar a parada de teste humano | CA-14: prompt que exclui a fase gera não execução com fonte/motivo/revisão e bloqueia APROVADA; omitir só PDF não dispensa a fase; teste humano para em IMPLEMENTADA após cobertura e entrega reais |
| RF-15 | Vincular relatórios e arquivos de evidência por manifesto, verificar a política fixa da instalação e rejeitar evidência ou política local divergente | CA-15: mudar bytes de teste, log ou relatório referenciado invalida a evidência; faltante, hash/perfil ou escopo incorreto bloqueiam; copiar gate 0 sem vínculos atuais não libera validação; editar política do consumidor não reduz piso/gates |
| RF-16 | Reconhecer rascunho válido antes da primeira fase e permitir retomada sem inventar aprovação | CA-16: contexto de draft válido retorna RASCUNHO/código 0 com próximos passos; avaliar avanço exige contrato completo e retorna 1; draft e change simultâneos geram conflito 1; ambos ausentes ou entrada malformada retornam 2 |

## Política candidata das sete fases

Esta política será própria do novo framework. Não modifica retroativamente o workflow de `projeto-origem`. Os estados representam evidências reconciliadas, não uma sequência de palavras em Markdown.

| Fase | Entrada e verificação | Saída observável |
| --- | --- | --- |
| 1. Especificação | proposal, spec, design e tasks completos, com revisão e matriz de aceite | EM_REVISAO_SPEC |
| 2. Revisão da SPEC | relatório técnico atual sem achado material aberto + decisão humana explícita sobre o contrato | SPEC_APROVADA ou REPROVADA |
| 3. Implementação | SPEC_APROVADA vigente; plano; testes executados e cobertura mínima atual; escopo autorizado | IMPLEMENTADA somente após os checks; caso contrário em andamento/BLOQUEADA; avaliação não executa código |
| 4. Revisão da implementação | manifesto atual + revisão contra SPEC, testes e cobertura conferidos | IMPLEMENTACAO_APROVADA ou retorno à implementação |
| 5. Validação | implementação aprovada; specflow-validar padrão no fluxo autorizado; cenários e segurança atuais | VALIDADA somente com gates; problema de segurança/omissão mantém pendente e impede aprovação |
| 6. Aprovação | validação vigente, teste manual obrigatório aprovado, ausência de pendências materiais + decisão humana final sobre o mesmo manifesto | APROVADA ou REPROVADA |
| 7. Encerramento | APROVADA; system atualizado; candidato de archive preparado; autorização de commit quando exigido | ARQUIVADA somente com evidência do encerramento efetivo |

Encerramento proposto: preparar atualização de system e candidato de archive → validar candidato → efetivar movimentação e, quando a política exigir, commit do conjunto → registrar localização e hash do commit como recibo posterior. Não afirmar que esse recibo está contido no próprio commit. Sem Git, usar manifesto local e marcar commit não aplicável pela política aprovada. O incremento só avalia esses registros sintéticos, sem mover Changes ou criar commits. Essa escolha resolve a divergência para o novo framework e requer aprovação do contrato.

Falha de clareza retorna à especificação; divergência de implementação retorna à implementação. Corrigir contrato invalida decisões dependentes de seus hashes. REPROVADA/BLOQUEADA exigem motivo, fase de retorno e evidência nova; nenhum retorno apaga o histórico. Um pedido de implementar com contrato diferente não é uma transição válida.

## Gates adicionais da r6

RASCUNHO é condição anterior à fase 1, não uma oitava fase ou autorização de código. O contexto de rascunho informa a necessidade futura de completar/revisar o contrato; isso não constitui falha operacional da leitura do rascunho. A conversão para Change completa é operação explícita do agente após preencher o contrato: criar change.json e retirar somente draft.json gerenciado. Leitura nunca faz essa conversão. Ambos presentes deixam estado INDETERMINADO até reconciliação.

Cobertura segue specs/shared/testing/coverage-policy.md. O avaliador verifica contadores inteiros de linhas/instruções cobertas e totais por arquivo do escopo, relatório e teste atuais, sem arredondar valores inferiores ao piso. Branches obedecem à exigência técnica da stack/SPEC. Artefatos sem código executável precisam de justificativa rastreável de não aplicabilidade; código gerado pelo agente não é exclusão. Ausência de ferramenta, LLM, teste manual e pedido de omitir validação não substituem esse gate.

Segurança segue docs/security-audit/GATE-SEGURANCA.md: análise real e evidências referenciadas por manifesto atual, com qualquer achado aberto bloqueante. O núcleo avalia os registros e não executa scanner, scripts ou gerador PDF; o orquestrador conduz as operações autorizadas. A evidência deve conservar código original do script e método/limites; PDF não satisfaz o gate sozinho.

Ao alcançar validação em fluxo completo autorizado, chamar specflow-validar por padrão. Omissão só por fonte explícita do usuário, com motivo/revisão; não executada não é VALIDADA nem permite APROVADA/ARQUIVADA. Comando de fase única não vira fluxo completo. Teste humano registra entrega/revisão e cenários pendentes, sem substituir testes técnicos, segurança ou aceite final.

## Perfis de digest e portabilidade

Cada item do manifesto declara `digestProfile`. O perfil `sha256-utf8-lf-v1` é obrigatório para os quatro documentos contratuais: decodificar UTF-8 estrito, aceitar e remover somente BOM UTF-8 inicial, substituir CRLF por LF e depois CR restante por LF, recodificar UTF-8 sem BOM e calcular SHA-256. Não normalizar Unicode, remover espaços, reformatar JSON ou acrescentar/remover newline final. Arquivo inválido não recebe fallback de encoding.

O perfil `sha256-bytes-v1` cobre binários e artefatos de implementação que exijam integridade byte a byte. Perfil ausente/desconhecido é erro 2, nunca inferido pela extensão. Troca de perfil invalida o vínculo anterior mesmo se um digest coincidir. Aprovação compara caminho, papel, perfil e digest, e não só o hash isolado. Um `rawSha256` auxiliar pode registrar bytes originais do texto para auditoria; diferenças apenas de BOM/newline não invalidam aprovação canônica nem autorizam sobrescrever arquivos. Não migrar ou reinterpretar silenciosamente manifestos r1 de bytes exatos.

A equivalência canônica é limitada a representação de texto, não garante equivalência semântica e não fornece autenticação do aprovador.

Arquivos de evidência não são aceitos apenas por existir. Cada registro de evidência inclui artifactManifest com exatamente os artifactRefs citados; o vínculo exige caminho/papel/perfil/digest e comparação com bytes atuais. Relatórios de cobertura vinculam também manifesto dos testes executados e das fontes medidas. Segurança inclui binding próprio para todos os evidenceRefs do audit, além dos digests do audit/gate e do manifesto-alvo. Não incluir o próprio JSON no manifesto que ele contém. Mudar uma evidência exige repetir os checks/revisão aplicáveis; produzir JSON novo com hashes diferentes não preserva automaticamente um resultado aprovado antigo.

project.policyDigest deve corresponder à política versionada fixada no manifesto da instalação confiável. Cópia sob .specflow/policies é referência de leitura, nunca override. Divergência bloqueia com código 1; perfil/versão desconhecido ou estrutura inválida retorna 2. Esse vínculo verifica consistência, sem autenticar quem pode reescrever a instalação inteira.

## Requisitos não funcionais

- RNF-01: implementação nova em `framework/`, Python >=3.11, biblioteca padrão no runtime, sem instalação global, telemetria, rede ou subprocessos para as operações do núcleo. Validação customizada e fechada por tipo de registro, com regras explícitas e testes de entradas inválidas; não prometer suporte genérico a JSON Schema.
- RNF-02: política e formatos internos versionados; esquema desconhecido falha de forma fechada. Identidade declarada do aprovador não é assinatura ou autenticação forte.
- RNF-03: em erro, não imprimir corpos de documentos ou valores potencialmente sensíveis; usar IDs, caminhos relativos, códigos e razões.
- RNF-04: leituras não alteram consumidores; testes com arquivos temporários preservam o corpus de origem. Toda evidência declara comando, ambiente, código, método e limites.
- RNF-05: Windows deve ser exercitado neste ambiente. Linux deve ser executado antes de declarar compatibilidade; se indisponível, registrar pendência sem simular aprovação ou afirmar paridade.

## Prontidão do incremento

Todos os RF e cenários negativos têm implementação, testes pertinentes e evidências rastreáveis; contrato e implementação não divergem; harness real tem hash e roteiro manual; cenários manuais foram realizados para a mesma revisão; aceite humano final permanece explícito. A validação do dossiê 10028 não vale como execução destes testes.

## Exclusões

Não compõem a implementação do núcleo: migração do acervo, publicação, extensão técnica ou consumidor real. O suporte local incorporado e os comandos de agente foram autorizados separadamente pelo usuário; não são assets automaticamente redistribuídos do núcleo. Copyright Rômulo Penha e MIT para material autoral foram definidos pelo usuário, com direitos de terceiros preservados em LICENSE-SCOPE e THIRD_PARTY_NOTICES; disponibilidade de marca continua não verificada. O harness do núcleo não possui comando que fabrique aprovação, execute implementação ou aplique encerramento. Os comandos de agente `specflow-*` conduzem essas fases conforme gates/autorização, sem equivaler ao harness implementado. Futuras integrações não podem enfraquecer estes gates.
