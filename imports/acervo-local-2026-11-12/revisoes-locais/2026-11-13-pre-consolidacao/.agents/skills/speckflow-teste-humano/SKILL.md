---
name: speckflow-teste-humano
description: "Alias de specflow-teste-humano: Conduzir uma Change ate IMPLEMENTADA com entrega executavel e roteiro para teste humano, respeitando SPEC_APROVADA e parando antes de revisao formal, validacao e aceite final."
license: MIT
metadata:
  author: "Rômulo Penha"
---

# speckflow-teste-humano

Fase: Fluxo composto ate a entrega para teste humano

Entrada: Objetivo de uma nova Change ou caminho de Change existente; escopo autorizado e aprovacoes ja registradas.

Saida: Change IMPLEMENTADA, artefato executavel identificado, checks tecnicos registrados e quickstart com teste humano pendente; sem revisao formal, VALIDADA, APROVADA ou encerramento.

## Procedimento

1. Retome a Change com specflow-contexto. Se nao existir contrato, conduza specflow-especificar e specflow-esclarecer apenas para lacunas materiais. Reutilize a mesma Change e preserve suas evidencias.
2. Conduza specflow-revisar-spec. Confirme decisao humana explicita de SPEC_APROVADA sobre a revisao corrente; parecer tecnico e invocacao deste comando nao aprovam o contrato. Se faltar aceite, apresente contrato, revisao e condicao de avanco, e pare antes do codigo. Nao repita pedido de aprovacao ja valido para a mesma revisao.
3. Com SPEC_APROVADA vigente, conduza specflow-planejar e depois specflow-implementar apenas no escopo autorizado. Este e um fluxo composto: essa sequencia e permitida dentro dele, mas nao libera fases posteriores ao limite de parada.
4. Durante a implementacao, execute build, testes, lint e smoke aplicaveis e corrija falhas dentro do contrato. Sao checks tecnicos da implementacao, nao a fase formal specflow-validar. Registre comandos, codigos, ambiente, resultados e limites reais. Se corrigir requisito, volte a SPEC e obtenha aceite da nova revisao antes de continuar.
5. Prepare resultado real utilizavel: build, pacote, harness ou ambiente local autorizado, com revisao/hash e comandos de execucao verificados. Nao basta apresentar codigo ou roteiro. Nao suba infraestrutura fora do escopo; se faltar recurso indispensavel, registre BLOQUEADA, impacto e proxima acao, sem afirmar pronto para teste.
6. Crie ou atualize quickstart.md com prerequisitos, caminhos relativos, diretorio de execucao, comandos, endereco quando aplicavel, roteiro manual por criterio de aceite e resultados esperados. Registre checks tecnicos separados dos cenarios humanos, cujo observado e resultado permanecem pendentes.
7. Pare obrigatoriamente em IMPLEMENTADA quando a entrega estiver utilizavel. Informe artefato/revisao, como executar e quais cenarios o usuario deve testar; aguarde o relato humano. Nao execute specflow-revisar-implementacao, specflow-validar, specflow-aprovar, specflow-encerrar ou seus equivalentes, nem marque testes humanos aprovados por ter escrito o roteiro.
8. Ao receber falha humana, registre o observado na mesma Change, corrija dentro do escopo aprovado, execute os checks afetados e entregue nova revisao para reteste. Um relato positivo tambem nao autoriza automaticamente aprovacao, system, archive, commit, push ou publicacao; fases seguintes dependem de pedido proprio. Atualize memoria e tasks com o estado real.

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Este fluxo composto pode conduzir contexto, especificacao/esclarecimento, revisao da SPEC, plano e implementacao, sempre respeitando SPEC_APROVADA humana. Pare na entrega IMPLEMENTADA para teste humano; nao execute revisao formal de implementacao, validacao formal, aprovacao ou encerramento. Nao crie subagentes como efeito colateral.
