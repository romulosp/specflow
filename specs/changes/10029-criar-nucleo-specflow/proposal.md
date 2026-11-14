# Change 10029 — Criar o núcleo autônomo do SpecFlow

Status: `EM_REVISAO_SPEC`. Revisão documental: **r6**, 2026-11-13.

## Pedido e autorização

O usuário pediu criar um framework autônomo com processo Spec Driven próprio. Esta proposta adota direção autônoma para revisão; não registra aceite humano do diagnóstico ou da arquitetura.

O pedido autoriza preparar esta Change. Pedidos posteriores autorizaram suporte incorporado, recursos de auditoria/ADR, neutralização de identificadores, copyright Rômulo Penha/MIT no material autoral e comandos de agente por fase. Isso não autoriza implementar o núcleo sem SPEC_APROVADA nem publicar componentes ou modificar checkouts externos.

## Problema

A investigação [10028](../10028-investigar-specflow-framework/validation.md) validou o dossiê, mas não criou um framework. Os gates ainda dependem de instruções e leitura manual; há divergências de encerramento e fontes de contexto potencialmente conflitantes. Copiar o acervo inteiro transportaria dependências e direitos não resolvidos.

## Resultado do primeiro incremento

R6 resolve a integração entre rascunhos e contexto e exige vínculos dos bytes reais de evidências/testes/relatórios e da política fixa. Escolha técnica feita pelo executor após delegação do usuário; aprovação do contrato continua pendente. Diagnóstico da revisão em [ajustes técnicos](../../../docs/cli/AJUSTES-TECNICOS.md) e [ADR proposto](../../../docs/adr/ADR-001-cli-local-e-gates.md).

Núcleo local autônomo com política explícita das sete fases, contratos versionados, avaliação determinística de gates, contexto com proveniência e verificação de rastreabilidade. Um harness permitirá testar fluxos positivos e negativos em dois consumidores sintéticos. Não é ainda o MVP completo ou uma extração do Protótipo.

Destino proposto para implementação: `framework/` dentro deste workspace. Nenhum Git, remoto, publicação ou instalação global será criado implicitamente. O núcleo novo terá zero dependência de runtime, assets, caminhos ou comandos de outro checkout.

## Escopo e limites

Inclui política candidata, schemas, biblioteca Python local, harness de inspeção, fixtures sintéticos, testes de comportamento e roteiro manual. Exclui cópia das 92 skills, migração, instalador, servidor de memória, banco vetorial, execução de stacks, upgrade aplicado, commit/archive real e publicação.

## Alternativas para aprovação

1. **Autônoma, recomendada para esta revisão:** preserva a autoria do processo e o controle de seus gates; exige manter ferramentas e distribuição próprias.
2. Híbrida: integrações opcionais futuras; exige compatibilidade adicional. Não é requisito deste incremento.
3. Adiar a implementação: mantém somente suporte documental, sem entregar o núcleo executável necessário ao CLI.

Memória local com proveniência é a recomendação; serviço central adicionaria operação e risco de compartilhamento sem necessidade demonstrada. Material autoral usa MIT/copyright Rômulo Penha por escolha expressa do usuário; suporte incorporado mantém direitos próprios. Marca pública e liberação de componentes sem licença confirmada continuam pendentes.

## Gate concreto

Aprovação solicitada abrange diagnóstico com seus limites, direção autônoma, memória local e o contrato r6 desta Change. Ela autorizará somente implementar o incremento aqui definido. Extração adicional, publicação e aceite final do produto permanecem separados. A revisão a aprovar deve ser vinculada ao manifesto de hashes desta pasta.

A revisão técnica recebida sobre r1 foi favorável, condicionada ao tratamento do digest de texto. A r2 incorpora normalização explícita UTF-8/LF, validação customizada por registro, códigos de saída e método de evidência obrigatório. Esse parecer técnico não foi registrado como decisão humana de SPEC_APROVADA do contrato alterado.

Contrato: [SPEC](spec.md), [design](DESIGN.md), [tarefas](tasks.md), [validação](validation.md). Evolução completa: [roteiro](../../ROADMAP-SPECFLOW.md).
