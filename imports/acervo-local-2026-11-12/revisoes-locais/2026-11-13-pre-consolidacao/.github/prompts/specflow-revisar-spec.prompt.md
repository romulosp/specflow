---
description: "Revisar tecnicamente o contrato SpecFlow e preparar a decisao humana de SPEC_APROVADA sem aprovar automaticamente."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-revisar-spec

Fase: 2. Revisao da SPEC

Entrada: Caminho e revisao da Change.

Saida: Relatorio REV com achados e recomendacao; SPEC_APROVADA somente se houver decisao humana explicita para a revisao corrente.

## Procedimento

1. Use a skill local spec-review e confronte proposta, SPEC, design e tarefas sem alterar implementacao.
2. Verifique clareza, requisitos, rastreabilidade, riscos, aceites negativos, direitos e conflitos. Achado material aberto impede avancar.
3. Registre recomendacao tecnica separada da decisao humana. Apresente contrato concreto, revisao e hashes antes de pedir aceite.
4. Se o usuario ja aprovou explicitamente essa revisao, registre fonte e escopo sem pedir novamente. Caso contrario, mantenha aprovacao pendente. Nunca use testes ou parecer tecnico como substitutos da decisao humana.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
