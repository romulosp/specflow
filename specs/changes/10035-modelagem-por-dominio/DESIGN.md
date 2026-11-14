# Design - 10035-modelagem-por-dominio

## Decisoes propostas
As divisoes de dominio ficam em secoes do spec.md existente, com correspondencia no DESIGN.md e nas tarefas. O manifesto atual exige exatamente quatro papeis; preservar esse formato mantem cada secao protegida pelo hash da SPEC e evita arquivos adicionais fora do contrato. Mudanca de conteudo exige revisao e decisao humana aplicaveis.

O agente identifica fronteiras a partir das necessidades reais, registra responsabilidade e linguagem, e define contratos entre dominios. Orquestracao pode coordenar operacoes; regras pertencem aos respectivos donos. Agregados, entidades e objetos de valor sao registrados quando forem uteis, sem impor padrao ou tecnologia. Dominios unicos e demandas tecnicas recebem tratamento proporcional.

## Integracao
Inventariar gerador de rascunho, templates e catalogo/instrucoes embutidas em framework/src/specflow/assets, alem dos comandos locais relevantes. Evoluir apenas os produtores e documentacao necessarios, mantendo compatibilidade com Changes existentes e preservacao no consumidor. Revisao humana e parecer tecnico continuam distintos.

## Alternativas
Arquivos independentes por dominio exigiriam ampliar o manifesto fechado e os leitores, arriscando aprovacoes; ficam fora desta revisao. Limite fixo de linhas nao identifica necessariamente mistura de dominios; usar sinais de tamanho, responsabilidades e dependencia com justificativa revisavel. Separar processos ou servicos apenas por dominio nao e requerido.
