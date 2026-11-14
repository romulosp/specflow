# SpecFlow

### Desenvolva com especificacoes, decisoes humanas e evidencias verificaveis.

O SpecFlow combina CLI local, templates e instrucoes para agentes de programacao em um processo Spec Driven. A CLI prepara o projeto e verifica pre-condicoes; o agente no editor executa o trabalho. `phaseExecuted=false` indica que preparar uma instrucao nao concluiu a fase.

## Comece aqui

Requisitos: Python 3.11 ou superior, [uv](https://docs.astral.sh/uv/) e agente no editor.

```shell
uv tool install specflow-cli
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor
specflow nova-change "Criar cadastro de clientes"
```

A distribuicao [specflow-cli 0.1.0 no PyPI](https://pypi.org/project/specflow-cli/0.1.0/) teve sua instalacao nominal verificada em ambiente isolado. Para instalar a partir deste checkout, use `uv tool install ./framework`. O runtime usa a biblioteca padrao do Python.

### Escolher ou atualizar a versao

Sem versao, o uv seleciona a versao mais recente compativel disponivel. Para escolher uma versao e conferir a instalada:

```shell
uv tool install "specflow-cli==0.1.0"
specflow --version
```

Para atualizar uma instalacao existente, use `uv tool upgrade specflow-cli`. O uv respeita a restricao definida na instalacao: se a versao estiver fixada, reinstale com a especificacao desejada para altera-la. Atualizar o CLI nao atualiza automaticamente projetos ja inicializados. Veja a [documentacao do uv](https://docs.astral.sh/uv/concepts/tools/).

Em projeto existente, use `specflow init .` com as integracoes desejadas. A inicializacao preserva arquivos existentes e cria `configuracao.properties` com valores `DEFINIR`; recursos incompletos ficam inativos e nenhum servico e iniciado automaticamente. Aplicacoes autorizadas ficam em `apps/`.

## Como funciona

1. **Especifique** o objetivo, criterios de aceite e tarefas de uma Change.
2. **Revise a SPEC** e registre a decisao humana da revisao correspondente.
3. **Planeje e implemente** com testes de comportamento e cobertura medida.
4. **Revise e valide** a implementacao, incluindo auditoria de seguranca aplicavel.
5. **Teste e decida** sobre o aceite humano; encerramento e publicacao sao acoes distintas.

O terminal verifica e prepara instrucoes. Execute as atividades com o agente no editor e confira os resultados. Testes verdes nao substituem decisoes humanas. Cobertura exige minimo de 80% por arquivo executavel e no agregado, com meta de 90%.

## Comandos principais

| Objetivo | Comando |
| --- | --- |
| Preparar projeto e verificar configuracao | `specflow init` e `specflow doctor` |
| Criar rascunho | `specflow nova-change "Descricao"` |
| Retomar contexto | `specflow contexto --change ID` |
| Conferir requisitos de um estado | `specflow check --change ID --target ESTADO` |
| Preparar instrucoes por fase | `specflow especificar --change ID`, `specflow planejar --change ID` e demais comandos de fase |
| Consultar opcoes | `specflow --help` ou `specflow COMANDO --help` |

As fases tem pre-condicoes proprias. A CLI nao chama modelos automaticamente nem transforma saida de comando em aprovacao. Consulte o [guia da CLI](framework/README.md) e o [catalogo de comandos](docs/comandos/COMANDOS.md).

## Estado e limites

A versao 0.1.0 e inicial e experimental. A publicacao e hashes foram verificados; a [evidencia de instalacao](docs/release/pypi-installation-smoke.json) registra 15 operacoes, e o CI executou Windows e Linux com Python 3.11 e 3.14. Descoberta e invocacao visual nos clientes e teste humano final do produto continuam pendentes e sao independentes da publicacao.

O acervo historico e recursos com direitos ou dependencias incompletos nao integram a distribuicao. O lock e cooperativo; verificacoes conferem consistencia, sem autenticar quem tomou uma decisao.

## Documentacao

- [Guia da CLI](framework/README.md) e [estado da publicacao](docs/release/README.md)
- [Fluxo SpecFlow](specs/shared/process/workflow.md) e [politica de cobertura](specs/shared/testing/coverage-policy.md)
- [Entrega e pendencias](docs/cli/ENTREGA-0.1.0.md)

## Licenca

Copyright (c) 2026 Rômulo Penha. Licenca MIT para o material autoral; consulte [LICENSE](LICENSE), [LICENSE-SCOPE](LICENSE-SCOPE.md) e [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md) para limites e direitos de terceiros.
