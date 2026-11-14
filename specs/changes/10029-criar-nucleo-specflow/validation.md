# Validação documental — Change 10029

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Evidencias atuais desta Change

Arquivos locais: acceptance-matrix.json; reviews/2026-11-14-implementation-review.md; evidence/implementation-manifest.json, test-suite.json, coverage-current.json, security-execution.json, security-binding.json, native-evaluation-input.json e native-evaluation-result.json. Relatorios compartilhados na raiz docs/cli/.

VAL-001: suite de comportamento/cobertura, CPython 3.14.6 no Windows, comando em docs/cli/tests-2026-11-14.json, codigo 0. Sem exclusoes de fonte; __init__.py contendo somente docstring e artefato sem instrucoes. VAL-002: build por python -m build --no-isolation --outdir ../dist a partir de framework/, codigo 0; wheel construido do sdist. VAL-003: instalacao/reinstalacao uv offline/no-index em UV_TOOL_DIR/UV_TOOL_BIN_DIR do workspace, 16 comandos com codigos esperados, sem mudar os 66 arquivos do consumidor.

VAL-004: skill security-audit aplicada, analise atual em docs/cli/SECURITY-REVIEW-2026-11-14.md. Comando obrigatorio: python -B docs/security-audit/verificar_seguranca.py --change <esta-Change>; resultado real codigo 0, status verificada. Somente esse helper nao vincula todos os logs; o binding nativo tambem foi validado, incluindo os bytes de todas as evidencias. Nao executar command do JSON. VAL-005: avaliacao direta da biblioteca com registros reais desta Change permite SPEC_APROVADA/IMPLEMENTADA/IMPLEMENTACAO_APROVADA e bloqueia VALIDADA/APROVADA com codigo 1 pela evidencia de homologacao not_run; nao houve transicao automatica ou bootstrap do repositorio autoral como consumidor.

VAL-006 PENDENTE: Linux e clientes reais nao exercitados; cenarios humanos not_run no human-handoff.json. Quickstart compartilhado em docs/cli/ENTREGA-0.1.0.md. Nao declarar criterio CLI-17, paridade Linux ou aceite final aprovados. A cobertura atual nao certifica todo o acervo historico.

## Historico anterior a este marco

## Conferência dos ajustes delegados - concluída documentalmente

13/11/2026. Resultado corrente: 52 verificações documentais aprovadas, zero falhas, em docs/cli/verificacao-ajustes-2026-11-13.json na raiz. Dossiê local: 36/0; helper de segurança inalterado: 10 testes sintéticos aprovados. Comparações textuais do auxiliar foram corrigidas para Unicode/ranges; snapshots exatos estão em ZIPs locais verificados, evitando links relativos relocados. A referência nova no índice ADR tem representação anterior preservada e hash local atualizado sem trocar o digest de origem.

Não há detalhe técnico a perguntar ao usuário: solução e tratamentos constam em AJUSTES-TECNICOS e ADR-001 PROPOSTO. Único gate antes de plano/código: decisão humana explícita dos contratos corrigidos 10029 r6, 10030 r4, 10031 r2, conforme o plano do usuário. Nenhum aceite foi inferido da delegação. Segurança/cobertura/compatibilidade reais do produto, wheel e homologação continuam não executados.


## Estado corrente - ajustes técnicos delegados e tratados

13/11/2026. O usuário respondeu "veja o melhor projeto e resolva"; portanto não aguardar nem perguntar quais detalhes técnicos corrigir. A revisão encontrou e tratou sete lacunas contratuais: draft/contexto, doctor com opcionais, init aditivo, escrita/rollback/links, gramática de properties, vínculo dos bytes de evidência/política e separação de plano/integração. Solução: uma distribuição Python, bibliotecas internas compartilhadas e agente no editor.

Contratos correntes: 10029 r6, 10030 r4, 10031 r2. Revisões anteriores exatas em evidence/revisions/r5, r3 e r1 nas Changes respectivas. Fonte da delegação em docs/cli/delegacao-tecnica-2026-11-13.json; tratamentos em docs/cli/AJUSTES-TECNICOS.md e ADR-001 proposto. Aprovação de SPEC permanece pendente; delegação técnica não é aceite. Sem código/pacote novo, cobertura de produto ou homologação simulada. Entradas anteriores de espera por detalhes e os 55 checks anteriores são históricos.


## Evidências da preparação do CLI - 13/11/2026

55 verificações documentais aprovadas, zero falhas, em docs/cli/verificacao-documental-2026-11-13.json na raiz. Incluem 12 hashes contratuais, arquivo externo de auditoria, papéis/IDs/rastreabilidade e links. O roteiro futuro ausente da 10030 foi acrescentado e reconferido; nenhum teste de runtime foi simulado. Dossiê: 36 checks aprovados; suporte de segurança: 10 testes sintéticos aprovados. Diagrama Mermaid parseado/renderizado e PNG final inspecionado; três avisos heurísticos de style não impediram o parser nem a renderização.

Decisão humana solicitada sobre 10029 r5, 10030 r3 e 10031 r1 em docs/cli/DECISAO-SPEC.md, conforme etapa de aprovação antes de código do plano recebido. Resposta ainda não registrada. Não iniciar implementation-plan/código por inferência nem promover gates. Não repetir escolhas de nome/estratégia já dadas. Produto, cobertura funcional, auditoria real, wheel e homologação continuam pendentes.


## Revisão corrente r5 - 13/11/2026

Limpeza editorial e integração do plano de criação do CLI. Estado EM_REVISAO_SPEC; nenhuma aprovação humana inferida. Contrato corrente evidence/contract-r5.json. Originais anteriores preservados em auditoria externa; recibo docs/auditoria-limpeza-cli.json na raiz. Revisões anteriores abaixo são históricas e não identificam o contrato corrente.


## Estado corrente — r4, 13/11/2026

EM_REVISAO_SPEC, sem aprovação humana e sem implementação do núcleo. Contrato corrente: evidence/contract-r4.json. R3 preservada em evidence/HISTORICO-ARQUIVADO.md. RF/CA-12..14, modelos de evidência, T11 e cenários M07..M10 incorporam cobertura, segurança, omissão e entrega humana. Integração com 10030 r2 separa propriedades/apps do harness de leitura.

Parecer documental em reviews/2026-11-13-spec-review-r4.md; conferência incremental em ../../../docs/revisao-pendencias-2026-11-13.json. Checks documentais, integridade e sintaxe não demonstram o comportamento especificado. Runtime, cobertura do núcleo, auditoria real e teste humano não executados. Evidências e números abaixo são históricos; não aprovam a r4. Decisões humanas no PENDENCIAS.md da raiz.

Resultado desta rodada: 36 checks de reconciliação e 36 checks do dossiê aprovados, zero falhas; 10 testes sintéticos do gate de segurança aprovados. Manifestos correntes e snapshots anteriores conferidos. Nenhuma cobertura funcional do núcleo foi medida porque seu código ainda não existe.

## Histórico até r3

Revisão r3, 2026-11-12. Estado: `EM_REVISAO_SPEC`; sem aprovação humana de SPEC e sem código do núcleo implementado. Ferramentas e comandos de suporte foram autorizados separadamente.

## Estado corrente

R3 preserva as regras técnicas da r2 e distingue suporte incorporado, comandos de agente e licença autoral. Os identificadores do ambiente anterior foram retirados da árvore local por pedido expresso; originais exatos permanecem em arquivo externo de auditoria. Manifestos r1/r2 agora identificam seus snapshots locais como derivados neutralizados e preservam separadamente os digests arquivados, sem aprovação inferida.

Contrato corrente em `evidence/contract-r3.json`; conferência atual em `evidence/document-check-r3.json`. Comandos, recursos documentais, neutralização e avisos de licença são conferidos separadamente em `docs/entrega-suporte.md`. Os resultados r1/r2 abaixo são históricos e não valem como teste do conteúdo editado ou do núcleo.

Resultado r3: 13 checks documentais aprovados, zero falhas. Suporte: 35 checks locais e 23 checks consolidados aprovados, sem falhas. Incluem materialização de 20 arquivos de comando, caminhos de documentação, identidade do contrato, entradas positiva/negativas do gerador e ausência do identificador retirado em 11.619 arquivos. Parser Mermaid confirmou a fonte sem avisos; SVG renderizado e PNG inspecionado visualmente. Origem preservada por hashes do corpus e complemento e por HEAD/status Git. Não incluem teste de integração dos clientes Codex/Copilot, auditoria real de aplicação ou runtime do núcleo.

## Tratamento da revisão recebida

Parecer técnico r1 e tratamento REV-01..05 em [revisão](reviews/2026-11-12-spec-review-r1.md). Os quatro documentos r1 foram preservados e seus hashes conferidos antes das alterações. A r2 substitui digest contratual de bytes exatos por perfil explícito UTF-8/LF, mantém digest binário exato, limita validação customizada ao domínio conhecido e explicita saída de conflito e método de evidência. Aprovação técnica condicionada não foi promovida a aprovação humana do contrato r2.

Manifesto r2: `evidence/contract-r2.json`; conferência documental desta revisão: `evidence/document-check-r2.json`, **20 verificações aprovadas, zero falhas**, código 0. Cobertura: referências locais, IDs RF/CA, tarefas pendentes, presença das regras revistas e preservação dos quatro snapshots r1 por seus digests originais. São verificações limitadas de documentos, não prova semântica completa dos contratos. O manifesto r1 e a evidência anterior continuam históricos e não representam o conteúdo corrente. Nenhum teste de runtime do novo perfil executado; a geração do manifesto é ferramenta documental, não implementação do núcleo.

## Revisão preparatória pelo executor

Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.
- RF-01..11 possuem critérios CA-01..11 e tarefas T02..T08. Cenários de gates, revisão alterada, conflito, isolamento e entradas malformadas estão definidos.
- O design distingue avaliação de execução e limita a capacidade de verificar identidade; nenhum comando de aprovação automática foi proposto.
- O primeiro incremento foi separado do MVP completo e das operações que exigem autorização específica.
- Plano preparatório será produzido após SPEC_APROVADA, conforme workflow canônico; não está sendo apresentado como plano já executado.

## Evidências e limites

Na r1, verificação documental local de referências, presença dos 11 pares RF/CA, tarefas não iniciadas e gate pendente: **15 verificações aprovadas, zero falhas**, código 0, em `evidence/document-check.json`. O primeiro auxiliar de conferência falhou ao comparar texto acentuado transmitido pelo PowerShell; o comparador foi corrigido e a checagem repetida sem alterar o estado das tarefas. Esta é verificação documental limitada, não revisão semântica automatizada completa. Manifesto histórico dos quatro documentos contratuais em `evidence/contract-r1.json`. Hashes identificam conteúdo revisável, não aprovação. Revisão pelo próprio executor, sem independência humana.

Reconferência do dossiê existente após as atualizações de continuidade: `python -B tools/verificar_dossie.py`, código 0, **23 verificações aprovadas, zero falhas**. Hashes do corpus e HEAD/status da origem preservados. Não foram repetidos a investigação, Pester ou pesquisa externa.

Nenhum teste de runtime do framework realizado; nenhum build existente. Resultados do dossiê 10028 não contam como teste deste incremento. Aprovação do contrato e aceite final do produto são gates distintos.
