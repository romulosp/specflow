# Revisão técnica — consumidor r4

13/11/2026. Executor da preparação, sem independência humana. Parecer documental favorável para decisão, sem SPEC_APROVADA.

| Achado | Severidade / tratamento | Referência |
| --- | --- | --- |
| REV-103 | material / aplicado ao contrato | INIT-08 permite integração aditiva da mesma versão, distinguindo metadados gerenciados de material autoral |
| REV-104 | material / aplicado ao contrato | INIT-08/APP-03 e design fecham lock, preflight, compare/replace, rollback conservador, nomes portáteis e links |
| REV-105 | material / aplicado ao contrato | INIT-07 define gramática UTF-8, primeiro =, credencial/backslash literais e rejeição de duplicatas/chaves desconhecidas |

Não há decisão técnica material deixada ao usuário sobre esses tratamentos. Confiabilidade real de escrita/recuperação, identidade de arquivo no SO, zero chamadas e cobertura continuam tarefas de implementação. Lock não impede editor externo; rollback não apaga alteração de terceiro. Restrições e limitações estão explícitas para não prometer transação global ou proteção contra controle malicioso da raiz. Sem achado material aberto identificado nesta revisão documental; aprovação humana e testes ainda pendentes.
