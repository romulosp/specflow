# Decisões humanas pendentes

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Historico anterior a este marco

A aprovação do plano de investigação e a SPEC documental não aprovam as decisões abaixo. Revisão técnica e validação do dossiê não equivalem à aceitação humana.

| ID | Decisão | Alternativas / recomendação | Pré-condição |
| --- | --- | --- | --- |
| DEC-01 | Aceitar o diagnóstico | Aceitar ou pedir correções, confrontando evidências e limites | Relatório e anexos revisados |
| DEC-02 | Arquitetura/distribuição | Autônoma, preset/extensão ou híbrida; recomendação corrente: autônoma na 10029 r5, seguindo a direção solicitada; exige manter contratos/harness próprios | DEC-01; a recomendação híbrida da investigação é histórica |
| DEC-03 | Contratos e memória | Local com proveniência/índice derivado recomendado; serviço central adiado | DEC-02 e riscos de dados avaliados |
| DEC-04 | Direitos/nome público | Copyright Rômulo Penha e MIT autoral definidos expressamente pelo usuário; direitos de terceiros e marca permanecem pendentes | Preservar avisos por componente e excluir direitos desconhecidos da distribuição |
| DEC-05 | Executar futura extração | Não autorizada; requer nova Change com SPEC aprovada e destino independente | DEC-01..04 e critérios de prontidão |

Nome SpecFlow Framework permanece provisório; disponibilidade de nome/marca não pesquisada. A escolha autoral de copyright/MIT foi determinada pelo usuário e executada sem substituir licenças de terceiros. Diagnóstico, arquitetura e SPEC de implementação continuam sem aprovação humana formal; não inferir direitos sobre terceiros ou publicação.

## Pacote corrente — 13/11/2026

As opções, consequências e condições atuais estão em [PENDENCIAS](../../../PENDENCIAS.md). Contratos correntes: núcleo 10029 r5 e inicialização 10030 r3, ambos EM_REVISAO_SPEC. Revisões técnicas favoráveis não aprovam esses contratos. Importação delimitada soma 360 recursos; os números e revisões abaixo descrevem momentos anteriores.

## Histórico — continuação em 2026-11-12

O usuário solicitou direção autônoma e CLI com agente no editor. A Change 10029 propõe o núcleo, a 10030 inicialização e a 10031 o CLI. Aprovação dos contratos continua separada do pedido de executar o plano.

DEC-01..04 e SPEC r1 da nova Change serão submetidas em conjunto, com decisões explícitas sobre diagnóstico, autonomia, memória local e uso privado provisório. DEC-05 continua não autorizada. O pedido geral de criar o framework não foi usado para registrar aprovação retroativa do diagnóstico, arquitetura ou de um contrato ainda inexistente.

## Histórico — autorização posterior de cópia local

Após a revisão técnica da Change 10029 (atualmente r2), o usuário autorizou expressamente importar os arquivos necessários de `projeto-origem` para este projeto sem apagar ou modificar a origem. Essa autorização foi executada como cópia local privada de 357 recursos de suporte, com manifesto em [imports](../../../imports/acervo-local-2026-11-12/README.md). Ela sucede a proibição anterior de copiar esses recursos neste escopo delimitado. DEC-05 continua pendente para extração definitiva, migração de consumidores ou redistribuição; não foi registrada aprovação arquitetural, de SPEC ou de publicação por consequência da cópia.

## Pacote corrente do CLI

Contratos 10029 r5, 10030 r3 e 10031 r1 apresentados para decisão em [DECISAO-SPEC](../../../docs/cli/DECISAO-SPEC.md). Nome, estratégia CLI + editor e instalação local já definidos. Aprovação dos contratos concreta e aceite final permanecem distintos; não registrar manifestação humana a partir do próprio texto deste pacote.
