# SPEC - 10035-modelagem-por-dominio

## Status
EM_REVISAO_SPEC - r1. Nenhuma aprovacao humana da revisao.

## Requisitos funcionais
- RF01: Na elaboracao de uma Change, o agente identifica dominios pertinentes a partir dos requisitos e registra no spec.md uma secao por dominio aplicavel, com nome, responsabilidade, conceitos, regras/invariantes e criterios de aceite. Para alteracao transversal tecnica sem dominio de negocio identificavel, registra justificativa e responsabilidade tecnica em vez de inventar dominios.
- RF02: No DESIGN.md, para cada dominio definido, registrar limites, dados sob responsabilidade, operacoes/contratos e dependencias permitidas; registrar integracoes e ownership compartilhado quando houver. Um dominio unico e valido quando justificado pelo contexto.
- RF03: O plano e as tarefas relacionam requisitos e criterios ao dominio ou responsabilidade tecnica, componentes previstos e testes; quando houver dependencia entre dominios, explicitar seu contrato e comportamento de falha aplicavel.
- RF04: Instrucoes de implementacao orientam concentrar cada regra de negocio em seu dominio, separar responsabilidades quando uma classe ou modulo acumular dominios independentes e manter integracoes por contratos explicitos. Classes de composicao/orquestracao podem coordenar dominios sem concentrar suas regras.
- RF05: A revisao da implementacao verifica o mapeamento, responsabilidades, dependencias, regras de negocio, riscos de classes excessivamente grandes ou multiplas responsabilidades e testes de fronteira. Registrar fontes, achados e justificativas; nao presumir defeito somente por contagem de linhas.
- RF06: Atualizar modelos, instrucoes locais e ativos empacotados de Copilot/Codex aplicaveis com a mesma orientacao; rascunhos e exemplos deixam claro o que e pendente, sem gerar supostos dominios ou aprovacoes automaticamente.
- RF07: Manter os quatro documentos contratuais existentes e seu manifesto fechado; secoes de dominio integram spec.md e DESIGN.md, cujos bytes sao cobertos pela aprovacao. Nao criar contratos adicionais nao protegidos nem alterar registros legados ou exigir nova aprovacao para bytes nao alterados.
- RF08: No reinit e nas Changes legadas, preservar arquivos existentes; nenhuma migracao automatica, reset de configuracao ou mudanca de gate. A existencia de instrucoes nao comprova que um cliente as executou.

## Qualidade
- RNF01: Testes executados para criacao e instrucoes, preservacao, exemplos de um ou varios dominios, responsabilidade tecnica e fronteiras. Para codigo executavel alterado, cobertura por arquivo e agregada minima 80%, meta 90%, com relatorios e inventario fonte-teste-criterio.
- RNF02: Sem dependencia obrigatoria de tecnologia ou tamanho de classe fixo; medidas podem orientar revisao mas nao substituem julgamento e evidencias.

## Criterios de aceite
- CA01 (RF01-02): Um exemplo com dois dominios separa conceitos, invariantes, limites e contratos; um exemplo pequeno com dominio unico justificado nao recebe divisao artificial; tarefa tecnica sem dominio tem justificativa.
- CA02 (RF03-05): Plano e revisao rastreiam um requisito de cada dominio ate componentes e testes; uma classe com regras de dominios independentes gera achado com fonte, enquanto orquestracao fina e aceita com justificativa.
- CA03 (RF06-07): Uma nova Change e instrucoes empacotadas apresentam secoes e orientacoes coerentes, mantendo quatro documentos e vinculacao atual dos hashes; editar uma secao contratual invalida vinculo anterior.
- CA04 (RF08): Change legada e arquivos existentes permanecem inalterados e verificaveis; nao se alega execucao de agente pelo terminal.
- CA05 (RNF01): Suite e relatorios atuais cobrem comportamento, falhas e limites e demonstram piso de cobertura por arquivo e agregado.
