# Entrega local — SpecFlow CLI 0.1.0

14/11/2026. Copyright (c) 2026 Rômulo Penha. Licença MIT para o pacote autoral.

SPECs 10029 r6, 10030 r4 e 10031 r2 aprovadas expressamente pelo usuário. Implementação em [framework](../../framework/README.md), sem alterar os quatro documentos contratuais aprovados. Aceite final, homologação completa e publicação continuam separados.

## Pacote e instalação

- [Wheel](../../dist/specflow_cli-0.1.0-py3-none-any.whl)
- [Distribuição de fontes](../../dist/specflow_cli-0.1.0.tar.gz)
- [SHA-256](../../dist/SHA256SUMS) e [inventário completo](package-inventory-2026-11-14.json)

Na raiz deste projeto, para instalação explicitamente escolhida pelo operador:

```powershell
uv tool install .\dist\specflow_cli-0.1.0-py3-none-any.whl
specflow --version
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor --json
specflow nova-change "Criar cadastro de clientes" --json
```

Use o `changeId` devolvido nos próximos comandos. `specflow contexto --change ID --json` deve informar RASCUNHO. `specflow implementar --change ID --json` deve bloquear com código 1 enquanto não houver contrato aprovado e plano. Isso demonstra o gate; não é erro de instalação.

Sem uv, instale o mesmo wheel com `python -m pip install <wheel>` em um venv escolhido. Runtime Python >=3.11, sem dependências externas. Apenas Python 3.14.6/Windows foi exercitado nesta entrega. `python -m specflow` usa o interpretador onde o pacote está instalado; o ambiente isolado criado por uv não equivale ao Python global.

Para testar sem instalação pessoal, já existe o executável isolado:

```powershell
.\framework\.test-output\delivery-r2-20261114\bin\specflow.exe --version
.\framework\.test-output\delivery-r2-20261114\bin\specflow.exe --project .\framework\.test-output\delivery-r2-20261114\consumer doctor --json
```

Esse consumidor é um sandbox de teste. Contém rascunho sintético, arquivos gerenciados e integrações; não é aplicação ou projeto do usuário. A reinstalação do pacote preservou seu snapshot de 66 arquivos. [16 operações e códigos reais](installation-smoke-2026-11-14.json).

## O que está disponível

Núcleo de contratos fechados, política fixa, hashes normalizados para texto contratual, memória isolada, matriz de evidências, gates de cobertura/segurança e sete estados avaliados sem transição automática. Inicialização preserva arquivos/configuração, acrescenta integrações na mesma versão e usa lock/rollback conservador. Aplicações autorizadas são gravadas pela API `generate_application` abaixo de `apps/`; `init` não cria aplicações.

O CLI entrega instruções ao agente no editor. Não chama modelos, implementa código ou autentica o aprovador automaticamente. A geração, revisão e manutenção dos registros são trabalho explícito do agente, com revisão humana quando exigida. [Comandos e diagrama](README.md).

`configuracao.properties` começa com 25 valores DEFINIR. Qualquer campo nesse estado mantém o recurso inteiro inativo. Os perfis de configuração não são adaptadores operacionais de Sonar ou outros serviços; nenhum serviço, scanner, download ou login foi iniciado. Auditoria real e gate local são diferentes de gerar PDF; o gerador PDF do acervo continua opcional e fora do wheel inicial.

## Verificações executadas

| Evidência | Resultado |
| --- | --- |
| [Suíte funcional/negativa](tests-2026-11-14.log) | 51 testes, 50 passaram, um skip por permissão de symlink; junction/hardlink reais passaram |
| [Cobertura](coverage-2026-11-14.json) | 1.280/1.324 linhas, 96,68%; branches 341/368, 92,66%; todos os arquivos executáveis acima de 80%, sem exclusões |
| [Build](build-2026-11-14.log) | sdist e wheel construído a partir do sdist, código 0 |
| [Instalação isolada](installation-smoke-2026-11-14.json) | uv offline/no-index, versão console/módulo igual, init/doctor/rascunho e bloqueios reais; reinstalação sem alterar consumidor |
| [Pacote e recursos](package-inventory-2026-11-14.json) | 26 arquivos no wheel e 30 no sdist; sem dependência de runtime, extensões incompletas ou identidades removidas; links Markdown do consumidor fechados |
| [Auditoria local](SECURITY-REVIEW-2026-11-14.md) | Análise atual e testes de segurança; gate por Change, com vínculos dos bytes das evidências |

Testes com decisões sintéticas verificam o mecanismo; não constituem decisão humana sobre o produto. A aprovação humana real das SPECs tem fonte própria. Não há Git local, histórico a inspecionar ou revisão independente por outro auditor nesta execução.

## Roteiro humano pendente

Todos os resultados abaixo começam em `not_run`. Registre ator, data/offset, versão do cliente/Python, hash do wheel, comando, saída/código observado e cenário. Não altere as SPECs congeladas para marcar progresso.

| Cenário | Execução e resultado esperado |
| --- | --- |
| H01 | Instalar wheel em ambiente escolhido; `specflow --version` mostra 0.1.0 e `--help` lista os comandos |
| H02 | Inicializar diretório vazio com a integração escolhida; conferir propriedades DEFINIR, `.gitignore` e ausência de `apps/` |
| H03 | Em consumidor descartável existente, preservar AGENTS/configuração/arquivo de aplicação; repetir init e acrescentar outra integração sem alteração desses bytes |
| H04 | Executar doctor; opcionais DEFINIR inativos, código 0, nenhum serviço iniciado |
| H05 | Criar Change e consultar contexto; RASCUNHO/0; implementar e teste-humano bloqueados sem aprovação/plano |
| H06 | Abrir consumidor no Copilot; demonstrar descoberta e invocação de `/specflow-especificar`, registrando versão e resultado |
| H07 | Abrir consumidor no Codex; demonstrar descoberta e invocação de `$specflow-especificar`, registrando versão e resultado |
| H08 | Conduzir uma Change descartável com o agente, contrato e aprovação reais; testar parada de teste-humano, cobertura e bloqueio de segurança pendente, sem aprovação/encerramento automático |
| H09 | Repetir suíte e instalação/fluxo básico em Linux; guardar evidências daquele ambiente antes de homologar CLI-17 |

Compatibilidade Linux e descoberta nos clientes permanecem **não executadas**. Falta de ambiente não é resultado positivo. A validação global continua pendente; nenhum registro APROVADA, archive, commit ou publicação foi produzido. Após estes testes, o aceite final deve identificar o mesmo build e permanecer separado da aprovação das SPECs.
