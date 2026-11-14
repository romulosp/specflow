# Modelagem por dominio

A SPEC descreve o que cada dominio decide e suas invariantes. O design define dados sob responsabilidade, fronteiras e contratos. Plano e tarefas relacionam requisito/criterio -> dominio -> componente -> teste. A implementacao e a revisao seguem esse mapa.

Um dominio unico justificado e valido; demandas tecnicas registram responsabilidade tecnica. Classes que concentram regras de varios dominios exigem separacao ou justificativa revisavel. Orquestracao fina coordena contratos sem absorver regras. Linhas de codigo sao sinal para investigar, sem limite universal.

As secoes permanecem em spec.md, DESIGN.md e tasks.md, protegidas pelo manifesto existente. Nao altere Changes aprovadas nem arquivos do consumidor como migracao automatica. O terminal entrega instrucoes, nao avalia semanticamente a arquitetura nem executa a revisao do agente.

Consulte EXEMPLOS.md para dois dominios, dominio unico e demanda tecnica, com criterios de revisao.
