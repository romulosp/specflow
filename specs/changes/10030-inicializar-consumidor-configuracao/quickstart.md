# Roteiro futuro — inicialização e configuração r3

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Roteiro executavel atual

Use docs/cli/ENTREGA-0.1.0.md na raiz para instalar o wheel ou executar o CLI isolado existente. SHA-256 em dist/SHA256SUMS. Cenarios H01..H09 permanecem not_run para o usuario; a tabela antiga abaixo e planejamento historico. Registre build, ambiente, ator, esperado/observado e codigos; nao marque resultado humano a partir de teste automatizado.

## Historico anterior a este marco

Estado: não executado. Não há init/parser/gerador implementados. Interfaces do design e CLI da 10031 são futuras; substituir este roteiro por comandos e build/hash reais antes de solicitar teste humano.

| Cenário | Preparação e ação após implementar | Resultado esperado | Observado |
| --- | --- | --- | --- |
| I01 | Inicializar consumidor limpo, sem integrações configuradas | properties criado, 25 valores DEFINIR e proteção no ignore; zero chamadas externas | não executado |
| I02 | Preencher somente URL de um recurso e consultar disponibilidade | recurso inteiro inativo; nenhum login, probe, download ou --version | não executado |
| I03 | Declarar modo permitido e NAO_APLICAVEL em campo opcional; repetir em URL/credencial obrigatória | opcional dispensado somente por contrato; uso indevido permanece inativo | não executado |
| I04 | Preencher configuração e criar arquivos autorais; repetir init | bytes preservados, sem reset/sobrescrita, ignore idempotente | não executado |
| I05 | Usar campo faltante/vazio/inválido/duplicado e inserir sentinela de segredo sintético | inativo/diagnóstico seguro, sem valores nos logs/metadados | não executado |
| I06 | Gerar aplicação primeiro sem e depois com SPEC corrente aprovada | sem gate não cria código; geração autorizada cria apps e escreve só no escopo permitido | não executado |
| I07 | Tentar travessia, link fora da raiz, apps como arquivo e destino existente | recusa antes de escrever fora do destino ou apagar conteúdo autoral | não executado |
| I08 | Deixar coletor obrigatório em DEFINIR; depois executar suíte/cobertura real | recurso não executado e gate pendente; medição atual >=80% por arquivo/agregado é necessária | não executado |

Entrega humana precisa de build e relatórios atuais, cobertura medida, revisão, auditoria real e gate de segurança nas fases aplicáveis. Testar Windows/Linux e integrações selecionadas sem credenciais reais. Evidências de presença de templates ou documentos não satisfazem esses cenários. Aprovação final e publicação continuam separadas.

Cenários adicionais r4, não executados: I09 (INIT-07), valor literal com =, backslash e espaços; LF/CRLF/BOM, duplicata/chave desconhecida e marcador; I10 (INIT-08), iniciar Copilot e depois acrescentar Codex sem mudar bytes autorais; I11 (INIT-08), dois escritores, lock ocupado, falha de commit e rollback com alteração concorrente; I12 (APP-03), nomes reservados, colisão por caixa, symlink/junction e hardlink de metadado com replace. Registrar casos realmente exercitados e limitações do ambiente, sem simular resultados.
