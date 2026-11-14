# Continuidade — Change 10029

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


## Revisão corrente r5 - 13/11/2026

Limpeza editorial e integração do plano de criação do CLI. Estado EM_REVISAO_SPEC; nenhuma aprovação humana inferida. Contrato corrente evidence/contract-r5.json. Originais anteriores preservados em auditoria externa; recibo docs/auditoria-limpeza-cli.json na raiz. Revisões anteriores abaixo são históricas e não identificam o contrato corrente.


## Estado corrente em 13/11/2026 - reconciliação de pendências

Estado corrente EM_REVISAO_SPEC r4. R3 preservada em evidence/HISTORICO-ARQUIVADO.md. Manifesto contract-r4.json identifica proposal/spec/DESIGN/tasks; nenhuma decisão humana aprovada. RF/CA-12..14 + T11 e M07..M10 integram cobertura mínima por arquivo/agregado, segurança atual, omissão explícita e entrega humana. Parecer técnico r4 não é aprovação. Properties/apps delegados à 10030 r2. Próximo passo dependente: decisão humana sobre diagnóstico, autonomia/memória e SPEC r4; depois plano e implementação. Não há framework, runtime, cobertura ou auditoria real do núcleo.

Conferência incremental: docs/revisao-pendencias-2026-11-13.json na raiz. Resultados desta rodada: 36 checks de reconciliação, 36 checks do dossiê e 10 testes sintéticos do gate aprovados, zero falhas; não são runtime/cobertura/auditoria do núcleo. Entradas anteriores são históricas; não representam aprovação da revisão corrente.

## Estado em 2026-11-13

Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.

Documentos criados: proposal, spec, DESIGN, tasks, quickstart e validation. Artefatos executáveis ainda inexistentes. implementation-plan será elaborado depois de SPEC_APROVADA. Contrato desta Change não herda aprovação da investigação 10028.

Histórico r1: conferência documental com 15 verificações aprovadas, zero falhas, em evidence/document-check.json; manifesto dos quatro documentos contratuais em evidence/contract-r1.json. Dossiê 10028 reconferido naquela etapa: 23 verificações aprovadas, zero falhas; hashes e estado Git da origem preservados. Nenhum resultado é teste funcional do framework.

## Limites persistentes

Nunca escrever em origem-externa. Não realizar extração definitiva, publicação, licença para material de terceiros ou encerramento automático. Implementação depende de aprovação explícita desta SPEC. O pedido geral não foi registrado como aprovação de documentos que ainda não existiam.

## Próxima ação

Apresentar contrato r3 concreto para decisão humana de SPEC_APROVADA do núcleo. Copyright/MIT autoral já determinados; suporte/ADRs/auditoria/comandos já autorizados e entregues separadamente. Não inferir aprovação de arquitetura/SPEC nem publicação. Se aprovado, registrar fonte, escopo e hashes/perfis e produzir implementation-plan antes de criar framework/. Nova mudança contratual exige nova revisão identificada.

Depois implementar T02..T10, entregar harness identificado e registrar teste manual real antes do aceite final. Demais incrementos em specs/ROADMAP-SPECFLOW.md. Não declarar todo o framework pronto por concluir apenas o núcleo.

## Revisão técnica tratada

Achados REV-01..05 em reviews/2026-11-12-spec-review-r1.md. Contrato r1 preservado em evidence/HISTORICO-ARQUIVADO.md, com hashes originais verificados. Contrato r2 usa sha256-utf8-lf-v1 em texto contratual (UTF-8 estrito, BOM inicial opcional, LF/CRLF/CR equivalentes, sem trim) e sha256-bytes-v1 em binários; perfil é obrigatório e integra vínculo de aprovação. rawSha256 é auditoria, não igualdade canônica. Nunca reinterpretar r1 silenciosamente.

Validadores customizados por registro com stdlib, sem engine JSON Schema. Context INDETERMINADO retorna 1; erro de entrada 2 tem prioridade. method/requiredMethod são enums obrigatórios, comparados por igualdade sem heurística. Alterações são documentais, sem implementação. Manifesto e conferência correntes em evidence/contract-r2.json e evidence/document-check-r2.json.

Conferência r2: 20 verificações documentais aprovadas, zero falhas, código 0. Manifesto contém quatro documentos com digest canônico e rawSha256 auxiliar. Histórico r1 preservado, não convertido. Não foi necessário repetir investigação ou testes da origem neste tratamento documental.

## Recursos de suporte agora locais

Pedido posterior do usuário autorizou expressamente copiar os arquivos necessários de projeto-origem para este projeto, sem apagar ou modificar a origem. Importados 357 arquivos, incluindo 92 skills em .agents/skills, shared/templates/sprint, prompts/agente e dois auxiliares Sonar opcionais. Registro em imports/acervo-local-2026-11-12/manifest.json. Não houve importação de apps, Changes antigas, credenciais ou dados operacionais. Quatro adaptações locais com originais preservados; AGENTS e STATUS próprios criados. Usar skills e regras daqui, não do checkout projeto-origem.

Esta cópia privada autorizada é preparação do ambiente, não implementação do núcleo ou execução de T02..T10; contrato r2 e seu manifesto permanecem intactos. G01/G02 continuam pendentes. As exclusões do incremento continuam valendo para o código/pacote do núcleo: skills importadas são suporte local, não assets redistribuídos do produto.

Verificador padrão agora local: python -B tools/verificar_dossie.py; 30 verificações aprovadas, zero falhas, sem leitura da origem. Auditoria histórica é opcional via --conferir-origem. 149 links já ausentes na origem em 30 skills opcionais constam de imports/acervo-local-2026-11-12/dependencias.json; não presumir essas extensões completas. Nenhum script operacional Sonar/Docker iniciado. Origem preservada por hashes do corpus e estado Git no manifesto.

Conferência local repetida com audit hook negando paths da origem no processo verificador: código 0, nenhuma tentativa de acesso bloqueada; limites do hook registrados em imports/acervo-local-2026-11-12/source-access-denied-check.json. Comparação final dos 1.385 arquivos, HEAD e status Git confirmou preservação em source-preservation-final.json. Hashes canônico e bruto dos quatro documentos r2 continuam iguais a contract-r2.json; nenhuma nova revisão contratual foi necessária para a preparação do ambiente.

## Pedidos posteriores executados — revisão r3

Esta seção sucede os estados e comandos históricos anteriores. O usuário pediu retirar todos os identificadores do ambiente anterior, adotar copyright Rômulo Penha/MIT e completar auditoria/ADR. Um ZIP externo preserva os originais exatos; evidências locais alteradas são derivados neutralizados, não prova de igualdade byte a byte. Os manifestos r1/r2 foram marcados históricos, com digests de representação e dos originais separados; contrato corrente em evidence/contract-r3.json.

Acervo: 360 recursos com proveniência (357 iniciais + gerador e dois registros ADR). Gerador local exige JSON atual; validação de entrada não gera PDF nem atesta auditoria. ADR Java é exemplo histórico; template e índice local não adotam aquela stack. Licença MIT autoral na raiz; atribuições MIT/Apache/CC-BY e direitos desconhecidos preservados em THIRD_PARTY_NOTICES. Não publicar sem autorização.

Usuário solicitou comandos para cada fase e diagrama. Criados dez comandos autorais specflow-*, cada um como Skill Codex e prompt Copilot: contexto, especificar, esclarecer, revisar-spec, planejar, implementar, revisar-implementacao, validar, aprovar e encerrar. Catálogo em docs/comandos/comandos.json; guia em COMANDOS.md; diagrama em fluxo-comandos.mmd/svg/png. São instruções para agente, não CLI nem implementação do núcleo. SPEC e aceite final dependem de decisão humana; comandos não criam subagentes, commits ou publicação implicitamente.

Renderização local usa dependências opcionais fixadas em tools/diagramas, sem instalação global. Corrigidos imports ESM Windows no renderizador/validador copiados; parser Mermaid validou sem avisos, SVG foi exportado sem fontes remotas e PNG inspecionado visualmente. Não houve geração de PDF de auditoria, teste humano dos comandos nos clientes ou implementação de T02..T10.

## Resultado final da preparação

35 checks do verificador local aprovados, zero falhas; 23 checks consolidados em imports/acervo-local-2026-11-12/delivery-check.json aprovados, zero falhas. Varredura de 11.619 arquivos (incluindo dependências locais de diagrama) não encontrou o identificador de ambiente retirado em nomes ou conteúdo. Corpus de 1.385 arquivos e três recursos complementares preservados, com HEAD/status Git externo idênticos ao baseline; somente leitura.

Contrato r3 possui 13 checks documentais aprovados em evidence/document-check-r3.json. Manifesto r3 corrente continua sem aprovação humana. O guia explica invocação com $ no Codex e / no Copilot; se os comandos não forem descobertos, recarregar a sessão. Nenhum binário specflow foi instalado. A próxima ação sobre o núcleo é revisão/aceite humano da r3, não execução automática de implementar. Manter avisos de terceiros e não publicar componentes com direitos desconhecidos.

## Composto de teste humano e gate de segurança — 2026-11-13

Usuário pediu comando que conduza até implementação e pare para ele testar. Criado specflow-teste-humano e alias exato speckflow-teste-humano, em Skill/prompt, respeitando SPEC_APROVADA humana, preparando plano, implementando com checks técnicos e entregando build/harness real, revisão/hash e quickstart. Para em IMPLEMENTADA com teste humano pendente; não chama revisão/validação formais, aprovação ou encerramento. Sem artefato real utilizável, registrar bloqueio em vez de afirmar pronto. Agora são 11 comandos canônicos + um alias, 24 arquivos gerados e 104 Skills locais.

Usuário também determinou segurança obrigatória em specflow-validar, com pendência se houver problema. Catálogo, prompt/Skill gerados, security-audit, implementation-validate e workflow local agora exigem análise real da skill e execução de docs/security-audit/verificar_seguranca.py. O script verifica auditoria estruturada atual, cobertura declarada, digests e referências; não executa scanner/commandos do JSON nem autentica o auditor. Gerador PDF não o substitui. Qualquer achado aberto, em qualquer severidade, check falho/não executado, auditoria ausente/incompleta/desatualizada ou erro mantém pendente, validationAllowed=false, sem VALIDADA/APROVADA. Correções voltam à implementação e exigem revisão/auditoria/gate atuais.

Foram executados 10 testes unitários do gate e três cenários de CLI com dados sintéticos (0 completo, 1 achado aberto, 2 malformado), todos nos resultados esperados. Verificador local: 36 checks aprovados, zero falhas. Guia e diagramas principal/teste-humano atualizados; fontes Mermaid validadas e PNGs inspecionados. Evidência corrente da atualização em docs/comandos/evidence/2026-11-13-comandos-e-seguranca.json. Não houve auditoria real do produto, execução do comando composto, aprovação da SPEC r3 ou implementação do núcleo. Manifesto r3 preservado.

## Validação como fase padrão — 2026-11-13

Por determinação expressa do usuário, quando um fluxo autorizado alcançar a fase de validação da implementação, chamar specflow-validar por padrão, sem exigir nova instrução rotineira. Só omitir se o prompt do usuário explicitamente pedir não executar a fase ou limitar o fluxo antes dela. Registrar referência da solicitação, motivo, revisão e não execução em validation.md e na memória; não promover VALIDADA/APROVADA/ARQUIVADA por dispensa. Omissão de PDF/ferramenta, falha ou ausência de recurso não autorizam pular a fase ou o gate de segurança.

Regra aplicada em AGENTS, workflow canônico, catálogo e Skill/prompt de specflow-validar, procedimento implementation-validate e prompt legado de fluxo completo. Evitada recursão: implementation-validate é procedimento técnico do comando, não o chama de volta. Comandos de fase única não viram fluxo completo por esta regra. A parada explícita de teste-humano continua em IMPLEMENTADA. Se a fase de validação for executada, skill security-audit e script de gate continuam obrigatórios.

Conferência: 24 arquivos gerados correspondem ao catálogo; 36 checks locais aprovados, zero falhas. Mudança de instruções, sem execução real de fase, novos testes de segurança ou alteração do contrato r3. Evidência em docs/comandos/evidence/2026-11-13-validacao-padrao.json.

## Conferência de cobertura — 2026-11-13

Usuário perguntou se todo o acervo de regras/ferramentas de teste foi trazido. Reutilizados inventário e manifesto; conferida somente presença/caminhos nos diretórios de suporte externos, sem nova investigação semântica ou escrita na origem. Todos os 324 arquivos das 92 skills e quatro de integração, além do gerador de auditoria e dois registros ADR, estão cobertos. Dos 126 componentes A/B, 125 têm todos os arquivos incorporados; AGENTS original foi substituído por instruções locais adaptadas.

Não declarar prontidão total: 149 referências transitivas já ausentes em 30 skills opcionais; oito arquivos particulares de scripts excluídos (3 geradores, 3 templates BAT, SQL de aplicação e fixture de configuração); runtime das extensões/clientes e geração/QA de PDF atual ainda não homologados; direitos de terceiros e marca pendentes. Núcleo, distribuição/upgrade/piloto continuam no roadmap. Nenhuma implementação foi iniciada ou aprovação registrada.

Estado detalhado em docs/estado-acervo.md; evidência em imports/acervo-local-2026-11-12/coverage-check-2026-11-13.json. Próxima revisão do contrato deve reconciliar as regras de comandos/segurança adicionadas após a r3 antes de pedir aceite. Não copiar launchers particulares ou executar ferramentas de infraestrutura como efeito desta conferência.

## Cobertura obrigatória e consolidação — 2026-11-13

Usuário determinou testes codificados e cobertura de 80% a 90% como condição de aprovação da implementação. Operacionalização declarada: piso obrigatório 80%, meta 90%, valores superiores válidos, por arquivo/escopo implementado e agregado, com teste executado e relatório atual. Não concluir IMPLEMENTADA/IMPLEMENTACAO_APROVADA sem evidência suficiente. Código gerado pelo agente está incluído; artefato sem linhas executáveis exige justificativa de não aplicabilidade, sem percentual fictício. LLM, teste manual, falta de Sonar ou omissão da validação formal não substituem medição. Fonte detalhada: specs/shared/testing/coverage-policy.md.

Usuário pediu reunir todas as regras anteriores. Registro de 40 itens SF-01..40 em specs/shared/process/regras-consolidadas.md distingue determinações U, operacionalização O e propostas P, com fontes e gates. Comandos gerados, workflow, Skills de processo, planejamento/Sprint, templates e orquestrador legado foram reconciliados para remover aprovação/commit implícitos e fallback de cobertura. Revisões locais pré-consolidação preservadas em imports/acervo-local-2026-11-12/revisoes-locais/2026-11-13-pre-consolidacao. Contrato r3 do núcleo permanece inalterado e sem aprovação; nova revisão deverá reconciliar os requisitos posteriores antes de implementação.

## Inicialização e apps — requisitos registrados em 2026-11-13

Usuário determinou criar sempre .properties na inicialização, campos inicialmente DEFINIR, sem tentar usar o recurso enquanto houver esse valor; também determinou gerar aplicações em apps/ na raiz do consumidor. Preparada Change 10030-inicializar-consumidor-configuracao r1, EM_REVISAO_SPEC, com proposta/SPEC/design/tarefas e exemplo sem credenciais. Nome configuracao.properties, UTF-8, catálogo por recurso e NAO_APLICAVEL para campo opcional são propostas técnicas para revisão, sem implementação ou aprovação inferida.

Preenchimento não dispara execução; recurso inativo obrigatório mantém seu gate pendente. Reinit/geração devem preservar valores/apps autorais e não escrever fora da raiz. O consumidor é distinto do código interno do framework. Não foram criados apps/ ou configuracao.properties reais neste workspace. Não tocar origem ou publicar. Esta consolidação é documental: não mediu cobertura dos helpers existentes nem declarou 80%/90% já atingidos.

Verificação final da consolidação: 14 checks documentais aprovados (40 regras, propostas separadas, propagação de cobertura a seis comandos, 25 valores DEFINIR, requisitos novos, contratos sem aprovação e links locais); 24 arquivos gerados correspondem ao catálogo e 36 checks de suporte aprovados. Contrato r3 permanece byte a byte/canonicamente idêntico ao manifesto, sem aprovação ou implementação do núcleo. Evidência corrente: docs/comandos/evidence/2026-11-13-regras-consolidadas.json. Artefatos da Change 10030 estão em revisão r1, sem herança de gates.
