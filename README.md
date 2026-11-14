# SpecFlow

Processo Spec Driven proprio, com CLI local e agente no editor. Copyright (c) 2026 Rômulo Penha. Licenca MIT para este codigo autoral.

## Instalacao

A publicacao inicial no PyPI esta em preparacao. Quando confirmada, a instalacao sera:

```powershell
uv tool install specflow-cli
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor
```

Enquanto o pacote nao estiver publicado, a partir deste checkout use `uv tool install ./framework`. Python >=3.11; runtime sem dependencias externas. [Guia do CLI](framework/README.md) e [estado da publicacao](docs/release/README.md).

Versao inicial experimental. O terminal prepara arquivos, verifica gates e entrega instrucoes ao agente no editor; nao chama modelos automaticamente. Especificacao humana aprovada e plano precedem codigo; testes/cobertura e auditoria de seguranca precedem os gates tecnicos. Testes verdes nao fabricam aceite humano.

Init preserva configuracoes e arquivos autorais, cria configuracao.properties com valores DEFINIR e nao inicia servicos. Geracao de aplicacoes autorizada fica em apps/. Recursos incompletos e acervo historico nao fazem parte desta distribuicao.

Descoberta/invocacao nos clientes e teste humano permanecem pendentes ate serem demonstrados. CI multiplataforma registra os resultados reais de cada execucao; nao alegar homologacao a partir de arquivos presentes.
