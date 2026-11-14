> Copia editorial neutralizada. Metricas e verificacoes abaixo sao historicas; originais exatos foram preservados em arquivo externo de auditoria. Links locais mostram recursos atuais, nao provam igualdade com o original.

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Historico anterior a este marco

# SpecFlow Framework — relatório consolidado de investigação

**Data:** 12/11/2026. **Origem:** Protótipo, revisão `2c48154cdc5e2abdeb65733eb47b920d89a3235f`. **Situação:** dossiê para aprovação humana; arquitetura e extração não autorizadas.

A metodologia tem mecanismos reutilizáveis e evidências de revisão/correção, mas ainda não possui independência executável comprovada. A direção solicitada é núcleo pequeno, memória por consumidor e CLI próprio com agente no editor. A implementação depende de SPEC aprovada.

## 1. Inventário completo da metodologia

O [inventário](inventario.md) relaciona 240 componentes existentes: 24 candidatos A, 102 B e 114 C, mais 12 lacunas D. O [manifesto](arquivos.md) cobre 1.385 arquivos textuais com proprietário, estado Git e SHA-256: 1.309 rastreados e 76 ignorados. Recursos de scripts/templates foram incluídos após auditoria de extensões; baseline inicial e suplemento são preservados separadamente.

Cobertura completa significa cobertura do corpus metodológico explicitamente delimitado, não auditoria semântica de todo o código/histórico do repositório. Há 426 arquivos excluídos por serem binários, backups ou material particular de referência/aplicação; lista em evidence/excluded-files.json. Nenhum conteúdo de credenciais externas ou logs operacionais foi copiado.

## 2. Mapa da estrutura atual

O [diagnóstico](diagnostico.md) apresenta raízes, 28 Changes em andamento e 55 arquivadas. O [mapa de dependências](dependencias.md) distingue vínculos normativos, referências documentais e dependências operacionais de ferramentas.

## 3. Classificação dos componentes

Core candidato: regras comuns de Change, gates, evidências, templates e modelos de planejamento. Extensões: convenções e skills de stack, validadores e integrações. Particularidades: estado, código, memória, contratos e decisões do Protótipo, inclusive scripts com configuração local. Lacunas D indicam mecanismos ausentes/incompletos. Categorias A/B não autorizam redistribuição e podem exigir divisão do arquivo misto.

## 4. Diagnóstico de maturidade

Há governança definida e evidência histórica de retorno por reprovação. O [diagnóstico por dimensão](diagnostico.md) evita nota global: memória automática, instalação, atualização e independência ainda não foram demonstradas. A Sprint 001 registra retificação de encerramento prematuro; testes estruturais não substituem execução da aplicação.

## 5. Lacunas identificadas

Doze lacunas estão ligadas às fontes: ordem divergente de archive/commit, contexto desatualizado, recursos transitivos ausentes, direitos desconhecidos, caminhos locais, gates textuais, rastreabilidade parcial, conhecimento disperso, instalação/upgrade ausentes, isolamento de memória, falsa equivalência entre estrutura e funcionamento e capacidades de extensões. Ver [diagnóstico](diagnostico.md) e [evidências](evidencias.md).

## 6. Direção autônoma

A [direção autônoma](direcao-autonoma.md) apresenta o caminho próprio. Fontes comparativas anteriores estão somente no arquivo externo de auditoria, fora da distribuição.

## 7. Arquitetura proposta

A [arquitetura candidata](arquitetura-proposta.md) reúne Core/Workflow, memória isolada, templates, validação e adaptadores de editor locais. As decisões de contrato continuam no [registro de decisões](../specs/changes/10028-investigar-specflow-framework/DECISOES-PENDENTES.md).

## 8. Estrutura do novo repositório

A árvore futura está na [proposta arquitetural](arquitetura-proposta.md). Nenhum repositório do framework foi criado. O diretório atual contém apenas a investigação, governança externa e ferramentas de conferência do dossiê.

## 9. Plano de extração

O [plano técnico](extracao-e-backlog.md) define X0–X8: decisão e direitos, contrato, laboratório, seleção, fechamento de dependências, MVP, extensões, piloto e release. Cada etapa tem pré-condições, evidência e reversibilidade. A origem nunca depende do resultado da extração.

## 10. Plano de evolução

Evoluir de contratos/memória/check para distribuição e atualização protegida, depois extensões e piloto humano. Aplicar SemVer, lock, matriz de compatibilidade e ownership de arquivos. Atualização de assets não deve substituir memória ou documentos autorais. Sem cronograma fictício sem equipe/capacidade definida.

## 11. Riscos técnicos

O [registro de riscos](extracao-e-backlog.md) prioriza direitos de redistribuição, gates não comprovados, dependências implícitas, vazamento de contexto, mudança do host e sobrescrita em upgrade. O nome é provisório; disponibilidade de marca não avaliada. Esses riscos bloqueiam prontidão do framework, não a apresentação deste diagnóstico.

## 12. Backlog inicial

BL-01–BL-15 possuem prioridade, dependências, resultado e aceite no [backlog](extracao-e-backlog.md). Publicação depende de licença/proveniência; MVP depende de política, configuração, fechamento de recursos e validação negativa. Importar todo o acervo não é prioridade inicial.

## 13. Proposta de MVP

Política/contratos versionados, templates, inicialização, nova Change em rascunho, recuperação de contexto, check de governança e plano de atualização. Memória local com fontes, decisões, lições e pendências; sem servidor ou banco vetorial. CLI próprio condicionado à prova de necessidade após laboratório de composição. Ver [MVP e limites](extracao-e-backlog.md).

## 14. Critérios de validação da extração

O [plano de testes futuro](extracao-e-backlog.md) exige consumidores independentes, isolamento de memória, gatilhos negativos, contrato alterado, dependência ausente, instalação repetida, upgrade com conflito, rollback, offline e compatibilidade do adaptador. Nada disso é declarado executado para um framework que ainda não existe.

A validação da presente entrega está em [validation.md](../specs/changes/10028-investigar-specflow-framework/validation.md): cobertura, referências, testes estruturais seguros e preservação de hashes/Git. Revisão pelo próprio executor, sem alegação de auditoria humana independente. A aceitação humana do diagnóstico, da arquitetura e da futura extração permanece separada.
