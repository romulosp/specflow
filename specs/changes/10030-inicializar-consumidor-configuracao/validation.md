# Validação preparatória — Change 10030

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


## Revisão corrente r3 - 13/11/2026

Limpeza editorial e integração do plano de criação do CLI. Estado EM_REVISAO_SPEC; nenhuma aprovação humana inferida. Contrato corrente evidence/contract-r3.json. Originais anteriores preservados em auditoria externa; recibo docs/auditoria-limpeza-cli.json na raiz. Revisões anteriores abaixo são históricas e não identificam o contrato corrente.


## Estado corrente — r2, 13/11/2026

EM_REVISAO_SPEC; aprovação humana e implementação pendentes. Contrato em evidence/contract-r2.json; quatro documentos r1 preservados em evidence/HISTORICO-ARQUIVADO.md. Parecer em reviews/2026-11-13-spec-review-r2.md. R2 reconcilia dependência de 10029 r4, fonte operacional única de endpoints/credenciais e NAO_APLICAVEL estritamente opcional. Template continua com 25 propriedades em DEFINIR. Conferência incremental na raiz em docs/revisao-pendencias-2026-11-13.json.

Não executados init, parser, geração, integração, cobertura ou segurança real. Nenhum arquivo de configuração real ou apps criado para simular conclusão. Resultados abaixo são históricos da r1, sem efeito de aprovação da r2.

Resultado desta rodada: 36 checks de reconciliação e 36 checks do dossiê aprovados, zero falhas; template com 25 propriedades em DEFINIR e os quatro digests correntes conferidos. Os 10 testes sintéticos do gate de segurança passaram separadamente, sem certificar este produto.

## Histórico r1

13/11/2026. Revisão r1, EM_REVISAO_SPEC. Aprovação humana e implementação pendentes.

Conferidos os quatro documentos contratuais e seus hashes, os 11 pares de requisitos/aceites e o template com 25 propriedades, todas em DEFINIR. Manifesto em evidence/contract-r1.json e conferência documental em evidence/document-check.json. A consolidação geral passou em 14 checks documentais, zero falhas, conforme docs/comandos/evidence/2026-11-13-regras-consolidadas.json. Esses checks não executam init, geração de aplicações ou conexões.

Não há biblioteca, CLI, apps ou configuracao.properties real criados por esta Change. O exemplo não contém credenciais reais. Não declarar idempotência, ausência de conexões ou cobertura funcional como já testadas; são critérios futuros. Compatibilidade de autenticação e a representação proposta NAO_APLICAVEL continuam sujeitas à revisão do contrato.
