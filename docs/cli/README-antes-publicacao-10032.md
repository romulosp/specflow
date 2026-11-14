# SpecFlow

Framework de processo Spec Driven próprio, com CLI local e agente no editor. O pacote **specflow-cli 0.1.0** está implementado em [framework/](framework/README.md), com os comandos `specflow` e `python -m specflow`.

Copyright (c) 2026 **Rômulo Penha**. [MIT](LICENSE) para o material autoral; componentes incorporados preservam seus autores e licenças em [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md) e [LICENSE-SCOPE](LICENSE-SCOPE.md). O pacote contém somente recursos autorais selecionados, sem as extensões incompletas do acervo.

As SPECs **10029 r6, 10030 r4 e 10031 r2 foram aprovadas expressamente**. [Fonte da decisão](docs/cli/aprovacao-humana-2026-11-13.json). Os documentos aprovados permanecem congelados; aprovação e progresso ficam em registros separados das Changes.

```powershell
uv tool install .\dist\specflow_cli-0.1.0-py3-none-any.whl
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor
specflow nova-change "Criar cadastro de clientes"
```

Python >=3.11; runtime sem dependências externas. Instalar o wheel é uma ação explícita do operador. A verificação local usou instalação isolada dentro do workspace. Nenhuma instalação pessoal ou publicação foi realizada.

O terminal prepara arquivos, verifica condições e mostra instruções para o agente. Preparar uma fase retorna `phaseExecuted=false`. A implementação de aplicações exige SPEC aprovada e plano; o código fica em `apps/`. `init` cria `configuracao.properties` com 25 valores `DEFINIR`, preserva arquivos existentes e não ativa serviços. Atualizar o pacote não modifica consumidores automaticamente.

Testes atuais: **51 casos, 50 aprovados e um pulado por permissão de symlink**; junction e hardlink reais passaram. Cobertura de linhas **96,68%**, acima de 80% em cada arquivo executável. Instalação/reinstalação isolada e fluxo Windows conferidos. [Entrega e evidências](docs/cli/ENTREGA-0.1.0.md), [guia e diagrama dos comandos](docs/cli/README.md), [pendências reais](PENDENCIAS.md).

Compatibilidade Linux, descoberta/invocação nos clientes Copilot/Codex e teste humano permanecem pendentes. Esses limites impedem declarar homologação completa, VALIDADA ou aceite final. A aprovação das SPECs autoriza o desenvolvimento; o aceite do build é outra decisão.

As [regras consolidadas](specs/shared/process/regras-consolidadas.md) exigem testes/cobertura, evidências atuais, segurança sem achados abertos e decisões humanas distintas. [AGENTS.md](AGENTS.md) orienta a continuidade. Recursos opcionais do acervo conservam suas limitações e não são capacidades certificadas do pacote.

O [relatório consolidado](relatorio/relatorio-consolidado.md) e a [memória da investigação](specs/changes/10028-investigar-specflow-framework/AGENTS-MEMORY.md) preservam o histórico. Nenhum checkout externo foi alterado; não houve extração definitiva, migração, commit ou publicação.# specflow
