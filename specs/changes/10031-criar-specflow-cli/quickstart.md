# Roteiro futuro de instalação e teste humano

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Roteiro executavel atual

Use docs/cli/ENTREGA-0.1.0.md na raiz para instalar o wheel ou executar o CLI isolado existente. SHA-256 em dist/SHA256SUMS. Cenarios H01..H09 permanecem not_run para o usuario; a tabela antiga abaixo e planejamento historico. Registre build, ambiente, ator, esperado/observado e codigos; nao marque resultado humano a partir de teste automatizado.

## Historico anterior a este marco

Estado: não executado; CLI e wheel ainda não existem. Estes comandos definem o cenário de aceite após implementação e geração do build.

```powershell
uv tool install .\dist\specflow_cli-0.1.0-py3-none-any.whl
specflow --version
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor
specflow nova-change "Criar cadastro de clientes"
specflow contexto --change <id-retornado>
specflow especificar --change <id-retornado>
```

Repetir init e confirmar preservação; conferir propriedades em DEFINIR sem ativação; invocar comandos nos dois editores; tentar planejar/implementar sem aprovação e observar bloqueio. Após contratos/código reais, medir cobertura, revisar e validar com auditoria atual. Teste humano recebe build/hash e cenários observados; instrução impressa pelo terminal não prova trabalho do agente.

R2: init íntegro com opcionais em DEFINIR deve permitir doctor/0; nova-change seguida de contexto deve retornar RASCUNHO/0 e avanço bloqueado. Fazer init . --integration codex depois de uma inicialização só com Copilot e conferir preservação. Alterar log/teste referenciado após auditoria: validar continua pendente mesmo se o gate v1 isolado retornar 0. Lock ocupado, rollback com editor concorrente e erro de argumentos sem eco de valores integram o roteiro, todos ainda não executados.

Instalação de smoke deve usar ambiente/perfil temporário e preservar o ambiente pessoal. Registrar comandos literais reais, versões, códigos, hash do wheel/sdist, plataformas e evidências. Após autorização futura de publicação e reserva do nome, poderá ser documentado uv tool install specflow-cli; isso não é operação desta entrega.
