---
description: "Resolver ambiguidades materiais da SPEC com perguntas objetivas e registrar respostas sem inventar aceite."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-esclarecer

Fase: Auxiliar da especificacao

Entrada: Caminho da Change e pontos a esclarecer, quando conhecidos.

Saida: Questoes respondidas ou explicitamente pendentes, contrato revisado e impacto na aprovacao registrado.

## Procedimento

1. Leia contrato e evidencias locais; pergunte apenas o que elas nao resolvem e que muda comportamento ou aceite.
2. Apresente alternativas e consequencias para questoes materiais. Nao transforme silencio em resposta.
3. Incorpore somente respostas recebidas; marque o restante como pendencia e mantenha o gate bloqueado quando relevante.
4. Se alterar contrato, identifique nova revisao e manifesto; a aprovacao anterior nao libera o conteudo alterado. Retorne a revisao da SPEC.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
