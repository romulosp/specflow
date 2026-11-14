# Importação local de suporte

Data: 12/11/2026. Pedidos expressos do usuário autorizaram suporte local, neutralização de identificadores, recursos de auditoria/ADR e comandos por fase. Este acervo não é release, migração de aplicação ou implementação do núcleo.

## Recursos trazidos

Lote inicial: 357 arquivos, 2.797.954 bytes no registro original:

- `.agents/skills/`: 324 arquivos, incluindo 92 SKILL.md e recursos existentes.
- `.github/agents/` e `.github/prompts/`: quatro arquivos de integração textual.
- `specs/shared/`: 15 regras/convenções de processo e stacks.
- `specs/templates/`: seis templates.
- `specs/sprint/`: seis arquivos reutilizáveis; Sprint concreta excluída.
- `scripts/sonar/`: dois arquivos opcionais, copiados sem execução de Sonar ou infraestrutura.

Complemento posterior: gerador de relatório de segurança e dois registros de ADR, totalizando **360 recursos com proveniência** no manifesto. Gerador e índice ADR foram adaptados; ADR Java está em `docs/adr/exemplos/` e não é decisão vigente. Template ADR e JSON sintético são documentos locais adicionais. Onze comandos autorais e o alias `speckflow-teste-humano` foram criados separadamente, somando **104 skills locais**; suas Skills/prompts totalizam 24 arquivos.

O processo básico usa as skills locais spec-review, spec-implement, implementation-review, implementation-validate, change-approve e git-commit. `AGENTS.md` local preserva os gates humanos e impede execução automática de commit/archive/publicação. Importar uma skill não autoriza executar suas ferramentas ou aplicar suas convenções a qualquer stack.

## Proveniência e adaptações

O [manifesto](manifest.json) separa digests do acervo e da representação local atual. Identificadores do ambiente anterior foram retirados de nomes, caminhos, conteúdo e evidências. O arquivo externo de auditoria preserva os originais exatos; snapshots em `originais/` podem ser derivados neutralizados e têm digest local próprio. Não comparar o conteúdo editado com o hash antigo como se fosse idêntico. Consulte [neutralizacao.json](neutralizacao.json) e [complemento-originais.json](complemento-originais.json).

`AGENTS.md` e `STATUS.md` descrevem este projeto. O contrato atual é r3; r1/r2 foram preservados externamente e suas cópias neutralizadas foram marcadas como históricas. A mudança editorial não foi registrada como aprovação do núcleo.

Não foram importados aplicações, Changes/archives antigos, memórias de consumidores, launchers, chaves, logs ou dados reais de pagamento/protocolo. Material autoral usa copyright Rômulo Penha/MIT; componentes incorporados conservam licenças/autores próprios e direitos desconhecidos não foram liberados por inferência. Consulte LICENSE-SCOPE e THIRD_PARTY_NOTICES na raiz.

## Dependências e limites

[dependencias.json](dependencias.json) registra **149 pares únicos documento/destino ausente**, já ausentes na origem, em 30 skills opcionais. A contagem é de links Markdown fora de blocos de código, não auditoria exaustiva de referências em texto, âncoras ou dependências de runtime. O catálogo em [CATALOGO.md](CATALOGO.md) distingue as skills com lacunas identificadas. Não foram criados placeholders para fingir completude. Nenhum recurso existente alcançado por esses links ficou para trás.

Os diretórios locais bastam para ler o processo e seus templates; não tornam Sonar, Docker, Maven, Android SDK, Nx ou provedores externos dependências embutidas. `scripts/sonar/validar-codigo.ps1` conserva configurações de infraestrutura do acervo e permanece opcional/inativo. Usá-lo requer parametrização e escopo próprios; não deve ser executado como etapa automática do núcleo Python.

O corpus histórico não é estado deste projeto. Os relatórios distribuídos são derivados neutralizados com indicação de proveniência; dados de auditoria antigos não comprovam segurança ou funcionamento do SpecFlow.

## Conferência

Na raiz: `python -B tools/verificar_dossie.py`. Verifica apenas recursos locais, hashes, links, materialização dos comandos, sintaxe e fixtures Android sintéticos, sem ler outro checkout. Resultado em [local-verification.json](local-verification.json), com 36 verificações aprovadas e zero falhas na última rodada registrada. São checks de suporte, não testes do núcleo ainda não implementado. A [conferência de cobertura](../../docs/estado-acervo.md) distingue o material incorporado das pendências funcionais e dos recursos particulares excluídos.

A evidência anterior de execução local com bloqueio de acesso externo continua identificada como histórica em [source-access-denied-check.json](source-access-denied-check.json). Preservação do corpus examinado e Git é registrada em [source-preservation-final.json](source-preservation-final.json); não equivale a auditoria integral do filesystem.

O modo antigo de acesso à origem foi removido do verificador. [qa-result-before-import.json](qa-result-before-import.json) é evidência histórica neutralizada, não resultado de um comando disponível atualmente. Originais exatos estão fora desta árvore.

`tools/importar_recursos.py` é coletor de incorporação com `--origem` obrigatório, sem checkout padrão; recusa sobrescrever destinos. Não é instalador nem ferramenta de atualização e não é necessário para usar os recursos locais.
