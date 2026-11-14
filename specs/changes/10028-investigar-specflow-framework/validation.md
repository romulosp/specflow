> Derivado editorial de 13/11/2026. Aprovações e resultados históricos pertencem aos originais arquivados; não aprovam estes bytes editados.

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

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


# Validação da investigação documental

## Estado
`VALIDADA` tecnicamente para apresentação humana. Não consta APROVADA ou ARQUIVADA. Diagnóstico, arquitetura e extração têm decisões humanas distintas pendentes.

## Ambiente

Data de referência: 2026-11-12, America/Sao_Paulo. Sistema: Microsoft Windows NT 10.0.19045.0. PowerShell 5.1.19041.6456; Python Python 3.14.6; git version 2.54.0.windows.1; Pester 3.4.0. Versões capturadas em [environment.json](evidence/environment.json). A revisão documental anterior concluiu IMPLEMENTACAO_APROVADA; mesmo executor em ambas as fases, sem revisão humana independente.

## Comandos, códigos e resultados

| ID | Ambiente / comando ou procedimento | Código | Resultado |
| --- | --- | --- | --- |
| VAL-001 | Git na origem: `git rev-parse HEAD`, `git status --porcelain=v1`, `git ls-files` | 0 | Revisão e alteração local prévia registradas; baseline inicial de 1.371 arquivos e suplemento de 14 recursos |
| VAL-002 | Leitura/indexação Python por pathlib nas raízes metodológicas; hash via hashlib.sha256; estado via git check-ignore | 0 no coletor | Manifesto de 1.385 arquivos, 240 componentes, 92 SKILL.md; 426 exclusões explícitas; git check-ignore retorna 0 para ignorado e 1 para não ignorado |
| VAL-003 | PowerShell Parser.ParseFile sobre os cinco PS1 de scripts/ | 0 | Cinco scripts sem erro sintático; nenhuma execução do script operacional |
| VAL-004 | `Invoke-Pester -Script origem-externa/scripts/sonar/tests/validar-codigo.Tests.ps1 -PassThru` | 0 | Quatro aprovados, zero falhas; teste estrutural, sem Sonar/Docker |
| VAL-005 | `python -B tools/verificar_dossie.py` na raiz externa | 0 | 23 verificações aprovadas, zero falhas; relatório estruturado em qa-result.json |
| VAL-006 | Python -B, validador Android original, fixture externo valid | 0 | Estrutura mínima aceita; não prova aplicativo Android compilável |
| VAL-007 | Mesmo comando, fixture externo missing-wrapper | 1 esperado | Wrapper ausente diagnosticado; cenário negativo aprovado |
| VAL-008 | Mesmo comando, fixture externo local-properties | 1 esperado | Arquivo local potencialmente sensível diagnosticado; conteúdo sintético |
| VAL-009 | `node --check <arquivo>` sobre seis MJS do acervo | 0 em cada | Somente sintaxe; dependências e runtime não carregados |
| VAL-010 | compile() em memória da ferramenta Python externa | 0 | Sintaxe válida; sem pyc na origem |
| VAL-011 | Resolução de referências Markdown autorais e cobertura do contrato | 0 | 22 documentos e 1725 links locais válidos na rodada registrada; 14 seções, 18 áreas e 12 lacunas presentes |
| VAL-012 | SHA-256 dos 1.385 arquivos, Git antes/depois dos cenários | 0 | Nenhum arquivo examinado alterado/ausente; HEAD e estado Git idênticos ao baseline |
Registro editorial: processo Spec Driven próprio; fonte histórica anterior preservada no arquivo externo de auditoria. Não reutilizar seus resultados como aprovação dos contratos correntes.

Comandos literais dos cenários, cwd, stdout, stderr e códigos originais constam em [qa-result.json](evidence/qa-result.json). O sucesso do verificador externo exige também os códigos negativos esperados. A última rodada pode incluir esta atualização documental; consultar o JSON para a contagem final de links/documentos.

## Procedimentos reproduzíveis

**Atualização posterior por autorização de importação local:** o comando padrão foi desacoplado da origem e agora confere as cópias locais em `.agents/skills/` e demais recursos importados. As instruções históricas abaixo descrevem a rodada original. Para repetir aquela comparação com o checkout, usar `python -B tools/verificar_dossie.py --conferir-origem`; a implementação original está em `tools/verificar_dossie_origem.py`. Manifesto e resultado local em `imports/acervo-local-2026-11-12/`. Isso não altera o veredito histórico nem aprova o núcleo.

Na raiz externa, executar `python -B tools/verificar_dossie.py`. O script verifica cobertura e ownership, índices, campos, referências locais, estrutura do relatório e SHA-256/Git; cria fixtures sintéticos somente em evidence/fixtures; chama o validador de leitura e node --check. Não depende de Docker, Java, Android SDK ou rede.

Para repetir sintaxe PowerShell, usar `[System.Management.Automation.Language.Parser]::ParseFile($arquivo, [ref]$tokens, [ref]$erros)` para cada `.ps1` em scripts/, sem invocar seus corpos. Resultados atuais em [powershell-syntax.json](evidence/powershell-syntax.json). Resultado Pester em [pester-result.json](evidence/pester-result.json).

## Segurança e não aplicabilidades

Mudança exclusivamente documental; conforme specs/sprint/README.md, auditoria de aplicação e PDF de segurança não aplicáveis. Foram inspecionados os documentos autorais, metadados/índices e ferramentas externas: nenhum corpo de credencial externa, protocolo, dado de cartão ou log operacional foi adotado. Não se declara busca integral no histórico por segredos nem ausência de vulnerabilidades em aplicações.

Nenhum Java/Kotlin/Go de produção foi criado ou alterado. JUnit, Maven/Gradle build, cobertura, Sonar real, rede operacional, hardware e testes de UI não se aplicam a este dossiê. Shell SH não executado; bash localizado era do subsistema Windows. Renderização Mermaid não executada; mapa também disponível em tabela. Licenças/direitos incompletos e decisão de arquitetura bloqueiam extração/publicação futura, não foram tratados como testes aprovados de um framework inexistente.

## Preservação e limites da prova

Hashes cobrem o corpus examinado, não todos os arquivos do computador. Baseline inicial e suplemento foram capturados em momentos diferentes e são identificados. Git preserva a mesma alteração prévia em `.idea/misc.xml`; não se afirma que o status Git por si só detecta mudanças em conteúdo ignorado fora do manifesto. Todas as operações de escrita desta investigação tiveram destino externo.

## Veredito

`VALIDADA` para cobertura, integridade documental, verificações seguras e apresentação dos resultados. Nenhuma aprovação humana do diagnóstico ou arquitetura foi inferida. Sem commit, archive, publicação, instalação de framework ou migração.
