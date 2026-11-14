# Memória operacional — investigação SpecFlow

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

Ultimo marco: IMP-REV-001 resolvido apos retorno da validacao a implementacao. Catalogo/CLI/24 Skills-prompts agora usam os mesmos guias autorais locais, com teste de regressao. Suite final 51 testes (50 passaram, um skip); pacote reconstruido e reinstalado em framework/.test-output/delivery-r2-20261114; auditoria e bindings repetidos sobre hashes atuais. Relatorio final docs/cli/final-verification-2026-11-14.json. Nao reutilizar candidatos de wheel/instalacoes de smoke anteriores.

## Historico anterior a este marco

## Conferência dos ajustes delegados - concluída documentalmente

13/11/2026. Resultado corrente: 52 verificações documentais aprovadas, zero falhas, em docs/cli/verificacao-ajustes-2026-11-13.json na raiz. Dossiê local: 36/0; helper de segurança inalterado: 10 testes sintéticos aprovados. Comparações textuais do auxiliar foram corrigidas para Unicode/ranges; snapshots exatos estão em ZIPs locais verificados, evitando links relativos relocados. A referência nova no índice ADR tem representação anterior preservada e hash local atualizado sem trocar o digest de origem.

Não há detalhe técnico a perguntar ao usuário: solução e tratamentos constam em AJUSTES-TECNICOS e ADR-001 PROPOSTO. Único gate antes de plano/código: decisão humana explícita dos contratos corrigidos 10029 r6, 10030 r4, 10031 r2, conforme o plano do usuário. Nenhum aceite foi inferido da delegação. Segurança/cobertura/compatibilidade reais do produto, wheel e homologação continuam não executados.


## Estado corrente - ajustes técnicos delegados e tratados

13/11/2026. O usuário respondeu "veja o melhor projeto e resolva"; portanto não aguardar nem perguntar quais detalhes técnicos corrigir. A revisão encontrou e tratou sete lacunas contratuais: draft/contexto, doctor com opcionais, init aditivo, escrita/rollback/links, gramática de properties, vínculo dos bytes de evidência/política e separação de plano/integração. Solução: uma distribuição Python, bibliotecas internas compartilhadas e agente no editor.

Contratos correntes: 10029 r6, 10030 r4, 10031 r2. Revisões anteriores exatas em evidence/revisions/r5, r3 e r1 nas Changes respectivas. Fonte da delegação em docs/cli/delegacao-tecnica-2026-11-13.json; tratamentos em docs/cli/AJUSTES-TECNICOS.md e ADR-001 proposto. Aprovação de SPEC permanece pendente; delegação técnica não é aceite. Sem código/pacote novo, cobertura de produto ou homologação simulada. Entradas anteriores de espera por detalhes e os 55 checks anteriores são históricos.


## Resposta humana corrente - ajustes antes de aprovar

13/11/2026. O usuário respondeu expressamente: "Quero corrigir os contratos antes de aprovar". Nenhuma SPEC foi aprovada. Os três contratos continuam EM_REVISAO_SPEC e seus manifestos não foram alterados. Detalhes das correções ainda não informados; pergunta de esclarecimento enviada. Próxima ação: receber os ajustes, revisar somente o escopo indicado com nova revisão/manifesto quando necessário e reapresentar para decisão. Não iniciar código, presumir quais requisitos mudar ou registrar REPROVADA formal por inferência. Fonte estruturada: docs/cli/feedback-humano-2026-11-13.json na raiz. Entradas anteriores de espera por decisão são históricas.


## Evidências da preparação do CLI - 13/11/2026

55 verificações documentais aprovadas, zero falhas, em docs/cli/verificacao-documental-2026-11-13.json na raiz. Incluem 12 hashes contratuais, arquivo externo de auditoria, papéis/IDs/rastreabilidade e links. O roteiro futuro ausente da 10030 foi acrescentado e reconferido; nenhum teste de runtime foi simulado. Dossiê: 36 checks aprovados; suporte de segurança: 10 testes sintéticos aprovados. Diagrama Mermaid parseado/renderizado e PNG final inspecionado; três avisos heurísticos de style não impediram o parser nem a renderização.

Decisão humana solicitada sobre 10029 r5, 10030 r3 e 10031 r1 em docs/cli/DECISAO-SPEC.md, conforme etapa de aprovação antes de código do plano recebido. Resposta ainda não registrada. Não iniciar implementation-plan/código por inferência nem promover gates. Não repetir escolhas de nome/estratégia já dadas. Produto, cobertura funcional, auditoria real, wheel e homologação continuam pendentes.


## Marco corrente - execução documental do plano do CLI

13/11/2026. Limpeza de identidades externas concluída; 30 arquivos históricos retirados da árvore somente depois de preservar e verificar originais no ZIP externo. Recibo docs/auditoria-limpeza-cli.json. O contrato da investigação editado é derivado editorial histórico, não recebe aprovação dos bytes originais.

Contratos correntes apresentados: núcleo 10029 r5, consumidor 10030 r3 e CLI 10031 r1. Nome specflow-cli/specflow e CLI + agente no editor escolhidos; não reabrir essas escolhas. Pedido de implementar o plano não foi registrado como SPEC_APROVADA de contratos ainda não apresentados. Pacote de decisão em docs/cli/DECISAO-SPEC.md. Nenhum código, wheel, instalação, homologação ou publicação do produto efetuado. Próximo passo dependente: decisão humana dos contratos concretos; depois planos preparatórios e implementação na ordem aprovada. Entradas anteriores são históricas.


## Estado corrente em 13/11/2026 - reconciliação de pendências

Contratos correntes 10029 r4 e 10030 r2 reconciliados, sem aprovação humana. DECISOES-PENDENTES atualiza recomendação autônoma e preserva opção híbrida como histórica. Registro de todas as classes de pendência em PENDENCIAS.md na raiz; não repetir investigação. Três links corrigidos; 146 pares ainda ausentes em 30 diretórios opcionais, limitados por notas locais. Gerador PDF exercitado com exemplo sintético e uma página inspecionada. Nenhuma extração definitiva, escrita em checkout externo ou publicação.

Conferência incremental: docs/revisao-pendencias-2026-11-13.json na raiz. Resultados desta rodada: 36 checks de reconciliação, 36 checks do dossiê e 10 testes sintéticos do gate aprovados, zero falhas; não são runtime/cobertura/auditoria do núcleo. Entradas anteriores são históricas; não representam aprovação da revisão corrente.

## Estado em 2026-11-12

Change externa autorizada. Contrato: SPEC_APROVADA. Documentos revisados em IMPLEMENTACAO_APROVADA e tecnicamente VALIDADA; aprovação humana pendente. Nenhuma arquitetura ou extração aprovada por humano.

Origem: origem-externa, HEAD 2c48154cdc5e2abdeb65733eb47b920d89a3235f. Git inicialmente modificado apenas em apps/frontend/smartphone/sistema-prototipo-android/.idea/misc.xml. Nunca escrever na origem nesta missão.

## Evidências e entregas

- Relatório: [consolidado](../../../relatorio/relatorio-consolidado.md).
- Manifesto: evidence/baseline.json, com 1.385 arquivos; baseline-initial.json tem 1.371, suplemento tem 14.
- Componentes: 240 existentes, 24 A/102 B/114 C, mais 12 lacunas D; 92 skills.
- Principais achados: referências de recursos ausentes, ordem archive/commit divergente, índices desatualizados e encerramento histórico prematuro retificado.
Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.
- Pester: quatro testes estruturais aprovados; sintaxe cinco PS1 aprovada. Sem Sonar/Docker/apps/hardware.

## Decisões, limites e próximos passos

Recomendação híbrida é candidata; decisões humanas em DECISOES-PENDENTES.md. Manter conhecimento global separado do consumidor. Direitos e nome público ainda pendentes; não publicar ou importar o acervo.

Revisão e validação concluídas. Para reconferir, executar `python -B tools/verificar_dossie.py` na raiz externa. Próximo passo: revisão humana de DEC-01..05; não iniciar extração. Não usar change-approve/git-commit para encerrar automaticamente. Testes futuros de extração estão no backlog; não confundir com QA do dossiê.

Não copiar credenciais, logs, protocolo ou dados de pagamento. Ferramentas auxiliares e fixtures externos existem apenas para verificar a investigação.

## Marco final

23 verificações de QA aprovadas; hashes dos 1.385 arquivos e estado Git preservados. Fixtures Android válido/sem wrapper/com local.properties responderam 0/1/1; seis MJS têm sintaxe válida. Sem comprovação de runtime dessas extensões. Evidência corrente em evidence/qa-result.json e validation.md.

## Retomada para decisões humanas — 2026-11-12

- Lidos README, esta memória, DECISOES-PENDENTES, validation e relatório consolidado; conferidos arquitetura, comparação, backlog e contrato existente. Investigação concluída não foi refeita.
- Executado novamente `python -B tools/verificar_dossie.py`: código 0, 23 verificações aprovadas, zero falhas. `evidence/qa-result.json` atualizado pelo verificador; hashes do corpus e HEAD/status Git da origem coincidem com o baseline. Não foram repetidos Pester ou pesquisa externa.
- DEC-01..05 continuam pendentes, sem aprovação inferida. Apresentar primeiro aceitação do diagnóstico e escolha arquitetural; depois contratos/memória, direitos/nome e autorização separada de extração.
- Recomendação para delimitar o primeiro incremento, ainda sem aceite: política canônica e contratos mínimos, preparando laboratório de composição com consumidores sintéticos. Resolver a ordem archive/commit e a vinculação de aprovação à revisão antes de testar equivalência de gates. Não antecipar CLI completo, importação do acervo ou distribuição pública.
- Após decisão humana sobre direção e escopo, preparar nova Change neste workspace externo com proposta, SPEC, design, tarefas e critérios verificáveis; estado inicial de rascunho, sem herdar SPEC_APROVADA da investigação. Não criar implementação antes de SPEC_APROVADA da nova Change.
- Nenhuma nova Change criada nesta retomada, pois o primeiro incremento ainda depende da escolha humana. Nenhum repositório do framework, extração definitiva, publicação ou escrita no Protótipo autorizados. Workspace externo continua sem repositório Git.

## Nova solicitação e correção de direção — 2026-11-12

Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.
- Foi preparada a Change 10029-criar-nucleo-specflow, revisão r1, em EM_REVISAO_SPEC, com proposta autônoma, SPEC, design, tarefas, quickstart futuro e validação documental. Roteiro completo em specs/ROADMAP-SPECFLOW.md. Esta entrada sucede a anotação anterior de que nenhuma nova Change existia.
- Direção autônoma é proposta concreta para decisão humana; nenhum DEC foi marcado aprovado. SPEC_APROVADA da investigação não se transfere. Não há implementação, build ou teste funcional do framework.
Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.
- Próximo passo: aprovação explícita do contrato r1 e decisões associadas; em seguida plano preparatório e implementação autorizada do núcleo, sem novo ciclo de investigação. Memória operacional do incremento em specs/changes/10029-criar-nucleo-specflow/AGENTS-MEMORY.md.

## Revisão técnica do núcleo — 2026-11-12

Recebido parecer técnico favorável condicionado sobre r1 da Change 10029. Preparada r2 para resolver digest textual UTF-8/LF, validação com stdlib, context indeterminado e tipos de evidência explícitos. A anotação anterior de próxima aprovação r1 é sucedida pela revisão r2. Aprovação humana de SPEC continua pendente; não houve implementação ou alteração da origem. Referência corrente: memória da Change 10029 e evidence/contract-r2.json dessa Change.

## Importação local autorizada — 2026-11-12

O usuário autorizou expressamente importar os recursos necessários de projeto-origem para este projeto, sem modificar/apagar a origem. Copiados 357 arquivos de suporte, incluindo 92 skills; paths, autorização e hashes em imports/acervo-local-2026-11-12/manifest.json. Quatro adaptações locais têm originais preservados. AGENTS e STATUS locais foram criados para este contexto, sem copiar memória operacional do consumidor. Essa autorização sucede o limite anterior de não copiar recursos, apenas para esta importação privada; não aprova SPEC, extração definitiva ou publicação.

O padrão `python -B tools/verificar_dossie.py` passou a verificar somente cópias locais: 30 verificações aprovadas, zero falhas, sourceRead=false. Para a auditoria histórica comparativa, usar explicitamente `--conferir-origem`; implementação anterior em tools/verificar_dossie_origem.py. QA anterior preservado em imports/acervo-local-2026-11-12/qa-result-before-import.json. Não interpretar as antigas instruções de que o comando padrão sempre lê a origem como atuais.

149 pares de links ausentes já na origem, em 30 skills opcionais, registrados em imports/acervo-local-2026-11-12/dependencias.json. Processo básico e templates estão locais; não inventar transitivas faltantes. Sonar e demais stacks permanecem opcionais e não foram executados. Próximo passo continua sendo decisão humana sobre SPEC r2, sem dependência de skills do checkout projeto-origem.

## Estado corrente após pedidos de autoria e comandos

Esta seção sucede instruções históricas de auditoria externa e revisão r2 acima. Identificadores do ambiente anterior foram removidos da árvore distribuída; originais exatos estão em arquivo externo de auditoria, e documentos/evidências locais editados são derivados neutralizados. O verificador é apenas local; o modo antigo de origem foi removido. A SPEC corrente da Change 10029 é r3, EM_REVISAO_SPEC, sem aprovação humana de implementação.

Usuário determinou copyright Rômulo Penha/MIT para material autoral; LICENSE-SCOPE e THIRD_PARTY_NOTICES preservam titulares/licenças de terceiros e pendências de direitos. Complemento autorizado de gerador e ADR totaliza 360 recursos incorporados; não reutilizar conclusões de auditorias antigas ou adotar ADR de exemplo como decisão atual.

Dez comandos autorais specflow-* foram criados em Skills e prompts, com guia, Mermaid, SVG e PNG em docs/comandos/. Não são CLI implementado nem aprovação implícita. Checks finais: 35 locais e 23 consolidados aprovados, zero falhas; 11.619 arquivos sem identificador retirado. Corpus examinado e complemento continuam intactos na origem. Nenhuma publicação, commit, archive, instalação global ou implementação do núcleo executados.

## Atualização de suporte — 2026-11-13

Acrescentados specflow-teste-humano e alias speckflow-teste-humano: 11 comandos canônicos + alias, 24 arquivos de Skills/prompts, 104 Skills locais. O composto respeita SPEC_APROVADA e para em IMPLEMENTADA com artefato e roteiro para o usuário testar, sem fases formais posteriores.

specflow-validar agora exige skill security-audit e script local de verificação das evidências atuais. Qualquer achado aberto, check incompleto/falho, auditoria ausente/desatualizada ou erro deixa a validação pendente. Não confundir gate de evidências com scanner automático ou com gerador de PDF. Dez testes do gate e três cenários CLI sintéticos passaram; verificador local tem 36 checks aprovados. Diagramas e memórias atualizados; contrato r3 do núcleo continua pendente de aprovação humana, sem implementação. Evidência em docs/comandos/evidence/2026-11-13-comandos-e-seguranca.json.

Pedido posterior em 13/11/2026: specflow-validar passa a ser o comando padrão quando o fluxo autorizado chega à validação da implementação; só omitir por prompt explícito do usuário, registrando solicitação, revisão, motivo e não execução, sem VALIDADA ou gates posteriores. Limite explícito teste-humano preservado; pedidos de não gerar PDF não dispensam validação/segurança. Regra refletida nas instruções locais, workflow, catálogo, Skills/prompts e fluxo completo legado. 24 arquivos gerados conferidos e 36 checks locais aprovados; nenhuma fase do produto ou aprovação humana executada.

Conferência incremental de cobertura em 13/11/2026, por pergunta do usuário: 324 arquivos de skills e quatro de integração presentes na origem têm cópias locais; complemento de auditoria/ADR coberto. Dos 126 candidatos A/B, 125 incorporados integralmente por paths; AGENTS recebeu versão local adaptada. 360 digests locais conferidos, sem divergências. Oito scripts/templates particulares de aplicações ficaram fora; 149 referências já ausentes na origem continuam pendentes. Não confundir cobertura com prontidão: núcleo, consolidação normativa, testes de runtime/piloto, distribuição e direitos ainda têm etapas abertas. Detalhes em docs/estado-acervo.md e imports/acervo-local-2026-11-12/coverage-check-2026-11-13.json. Sem nova investigação semântica, execução de infraestrutura, cópia adicional ou escrita na origem.

Determinações posteriores de 13/11/2026 consolidadas em specs/shared/process/regras-consolidadas.md: 40 regras com origem/tipo e propostas pendentes separados. Cobertura mínima medida 80%, meta 90%, testes executados e relatório atual condicionam conclusão/aprovação da implementação; sem fallback LLM/manual. Material de processo e comandos reconciliados, incluindo orquestrador sem aceite/commit automáticos. Contrato r3 do núcleo continua sem aprovação e precisa incorporar regras posteriores na próxima revisão.

Nova Change 10030 r1 prepara init/configuracao.properties sempre com valores DEFINIR, guarda de não uso de recursos incompletos e geração de aplicações em apps/ do consumidor. Nenhuma implementação, arquivo real de credenciais, apps real, execução de integração ou publicação. Detalhes técnicos de autenticação opcional continuam propostos. Memórias das Changes 10029 e 10030 são as fontes de continuidade correntes.
