# Continuidade — inicialização e configuração

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


## Revisão corrente r3 - 13/11/2026

Limpeza editorial e integração do plano de criação do CLI. Estado EM_REVISAO_SPEC; nenhuma aprovação humana inferida. Contrato corrente evidence/contract-r3.json. Originais anteriores preservados em auditoria externa; recibo docs/auditoria-limpeza-cli.json na raiz. Revisões anteriores abaixo são históricas e não identificam o contrato corrente.


## Estado corrente em 13/11/2026 - reconciliação de pendências

Estado corrente EM_REVISAO_SPEC r2. R1 preservada em evidence/HISTORICO-ARQUIVADO.md; manifesto contract-r2.json. Contratos de evidência/gates dependem da entrega validada do núcleo 10029 r4. Properties é fonte operacional única de endpoints/credenciais; NAO_APLICAVEL somente em campo dispensável declarado, nenhum DEFINIR ignorado. Template de 25 propriedades mantido, nenhum arquivo real de configuração ou apps criado. Parecer técnico r2 sem aprovação humana. Próximo: decisão da SPEC, depois núcleo validado/plano/implementação; não inferir funcionalidades de init/gerador.

Conferência incremental: docs/revisao-pendencias-2026-11-13.json na raiz. Resultados desta rodada: 36 checks de reconciliação, 36 checks do dossiê e 10 testes sintéticos do gate aprovados, zero falhas; não são runtime/cobertura/auditoria do núcleo. Entradas anteriores são históricas; não representam aprovação da revisão corrente.

Estado em 13/11/2026: EM_REVISAO_SPEC r1. Usuário determinou arquivo .properties criado sempre em init, campos inicialmente DEFINIR, zero uso do recurso enquanto houver marcador, e geração de aplicações em apps na raiz do consumidor.

Preparados proposta, SPEC, design, tarefas e exemplo, sem implementar parser/init/gerador. Nome configuracao.properties e NAO_APLICAVEL para campo opcional são decisões técnicas propostas, não eventos de aprovação. O contrato deve ser reconciliado com o núcleo antes de implementar. Nenhum SPEC_APROVADA foi inferido da autorização para registrar as regras.

Regras centrais SF-31..36 em specs/shared/process/regras-consolidadas.md. Credenciais locais não versionadas/logadas; configuração preenchida não autoriza executar recurso. DEFINIR em recurso obrigatório deixa o respectivo gate pendente, sem tentativa ou fallback de aprovação. apps é saída das aplicações consumidoras, não destino do código interno do framework.

Próxima ação: revisão do contrato e do catálogo de recursos/autenticação opcional; aprovação explícita antes de plano preparatório/código. Não criar apps ou arquivo real neste workspace para aparentar init já executado. Não tocar checkouts externos ou publicar.

Conferência documental concluída: manifesto r1 dos quatro documentos validado, 11 requisitos com aceites presentes e 25 propriedades com valor DEFINIR. Conferência consolidada com 14 checks aprovados, zero falhas. Evidências em evidence/document-check.json e docs/comandos/evidence/2026-11-13-regras-consolidadas.json. Nenhuma execução funcional, aferição de cobertura do produto ou aprovação humana ocorreu.
