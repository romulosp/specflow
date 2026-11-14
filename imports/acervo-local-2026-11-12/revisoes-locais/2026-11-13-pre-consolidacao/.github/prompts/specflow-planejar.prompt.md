---
description: "Preparar implementation-plan de uma Change SpecFlow com SPEC_APROVADA vigente, sem iniciar codigo."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-planejar

Fase: Preparacao entre fases 2 e 3

Entrada: Change com contrato corrente aprovado por humano.

Saida: implementation-plan.md com impactos, ordem de implementacao, testes, seguranca, riscos e validacao manual.

## Procedimento

1. Confirme SPEC_APROVADA humana sobre a revisao atual em proposal e spec, verificando a evidencia; palavra isolada no arquivo nao basta.
2. Sem esse gate, informe precisamente o que falta e pare sem implementar. O planejamento de produto anterior ao aceite pertence a especificar/esclarecer.
3. Registre plano preparatorio conforme workflow, sem reescrever contrato aprovado ou gerar configuracao/infraestrutura.
4. Defina testes pertinentes e roteiro de entrega executavel; nao marque tarefas de implementacao como concluidas por estarem planejadas.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
