---
name: specflow-revisar-implementacao
description: "Confrontar implementacao e SPEC aprovada e registrar achados de aderencia, sem corrigir codigo nesta fase."
license: MIT
metadata:
  author: "Rômulo Penha"
---

# specflow-revisar-implementacao

Fase: 4. Revisao da implementacao

Entrada: Change IMPLEMENTADA e manifesto da implementacao.

Saida: Relatorio IMP-REV com IMPLEMENTACAO_APROVADA tecnica ou REPROVADA e retorno indicado.

## Procedimento

1. Use o guia local specs/shared/process/helpers/implementation-review.md. Verifique codigo real, testes, diff e rastreabilidade contra contrato corrente. Confira obrigatoriamente testes codificados/executados e cobertura medida atual minima de 80% por arquivo/escopo implementado, meta 90%, conforme specs/shared/testing/coverage-policy.md. Relatorio ausente/desatualizado, suite falha, arquivo sem testes ou abaixo do piso impede IMPLEMENTACAO_APROVADA e retorna a implementacao.
2. Registre ID, severidade, fonte, impacto e recomendacao para cada achado; explicite se a revisao e pelo mesmo executor.
3. Nao corrija codigo durante esta revisao. Divergencia retorna a implementar; ambiguidade de requisito retorna a especificar/esclarecer.
4. Somente ausencia de pendencia material e gate obrigatorio de testes/cobertura atendido permite IMPLEMENTACAO_APROVADA tecnica; isso nao e aprovacao humana final.

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
