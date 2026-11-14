---
name: "Executar mudança Spec Driven"
description: "Conduzir o fluxo completo autorizado com gates humanos, cobertura e seguranca obrigatorias."
argument-hint: "Informe o caminho da Change"
agent: agent
---

# Execucao integral de Change SpecFlow

Execute a Change indicada em `${input:changePath}` usando somente recursos locais. Leia [AGENTS.md](../../AGENTS.md), [regras consolidadas](../../specs/shared/process/regras-consolidadas.md), [workflow](../../specs/shared/process/workflow.md) e [comandos](../../docs/comandos/COMANDOS.md). Essas regras substituem sequencias legadas de aprovacao automatica, stacks fixas ou commit implicito.

## Sequencia autorizada e limites

1. Retome estado, memoria, contrato, reviews e validation da mesma Change com specflow-contexto. Nao crie outra Change apenas para retomar.
2. Se faltar contrato, conduza specflow-especificar/esclarecer e specflow-revisar-spec. Pare antes de codigo se faltar SPEC_APROVADA humana da revisao corrente; parecer tecnico nao e essa decisao. Aproveite aceite ja valido, sem perguntar novamente.
3. Apos esse gate, use specflow-planejar e registre implementation-plan antes do codigo, sem reescrever contrato aprovado.
4. Use specflow-implementar no escopo aprovado. Para todo codigo implementado, codifique e execute testes de comportamento e meca cobertura minima de 80% por arquivo/escopo, meta 90%, permitindo valores superiores, conforme coverage-policy.md. Sem suite aprovada e relatorio atual suficiente, nao concluir IMPLEMENTADA ou aprovar IMPLEMENTACAO_APROVADA. LLM, teste manual ou falta de Sonar nao dispensam cobertura.
5. Com implementacao concluida, conduza specflow-revisar-implementacao; divergencia retorna a fase responsavel. Revisao nao corrige codigo nem requisitos.
6. Com IMPLEMENTACAO_APROVADA, execute specflow-validar por padrao, sem nova solicitacao rotineira. Excecao: prompt do usuario explicitamente pede omitir a fase ou parar antes dela; registre solicitacao, motivo, revisao e nao execucao em validation.md/memoria, sem VALIDADA, aceite ou encerramento. Falha ou pedido de nao gerar PDF nao e dispensa. A omissao nao dispensa cobertura da implementacao.
7. Na validacao executada, chame security-audit e execute `python -B docs/security-audit/verificar_seguranca.py --change <Change>`. Qualquer achado aberto, check falho/incompleto, auditoria ausente/desatualizada ou erro mantem pendente. O gerador PDF nao e scanner; PDF somente se solicitado, com dados atuais e QA visual. Nao usar auditoria historica como prova atual.
8. Entregue build/harness real, revisao/hash e quickstart antes de solicitar teste humano. Registre o observado; roteiro nao e execucao. Falhas retornam a implementacao ou SPEC; repetir cenarios afetados e atualizar evidencias da revisao corrigida.
9. Conduza specflow-aprovar somente com evidencias e testes manuais aplicaveis satisfeitos. APROVADA exige aceite humano explicito da mesma revisao. Invocar a fase, teste verde ou silencio nao e aprovacao.
10. specflow-encerrar so pode efetivar acoes autorizadas, com system/candidato de archive conferidos e recibo posterior. Nao criar Git, commit, archive, push, deploy ou publicacao automaticamente. Sem encerramento efetivo, nao declarar ARQUIVADA.

## Fluxo limitado para teste humano

Se o pedido limitar a entrega ao teste humano, use specflow-teste-humano (alias speckflow-teste-humano): cumprir SPEC_APROVADA, plano, implementacao, testes/cobertura e resultado executavel; parar em IMPLEMENTADA aguardando o usuario, sem revisao/validacao formais ou aceite/encerramento.

## Evidencias e comunicacao

Atualize tasks, memoria e validation com arquivos, revisao, comandos/cwd, codigos, metricas e limites reais. Nao inventar gates, aprovacoes, cobertura ou runtime. Mantenha segredos redigidos e checkouts externos intactos. Perfis tecnicos sao opcionais conforme a stack; nao impor configuracao Java/Go/Android ao nucleo ou ao consumidor sem escopo aprovado.
