# Exemplos para especificacao e revisao por dominio

Exemplos didaticos. Nao representam contratos aprovados, execucao de agente ou aceite humano.

## Dois dominios: Pedidos e Estoque

### SPEC
Pedidos decide o ciclo do pedido. Conceitos: pedido, item, confirmacao. Invariante: confirmar somente apos reserva aceita. CA-P01: reserva recusada mantem pedido pendente.
Estoque decide disponibilidade. Conceitos: saldo, reserva. Invariante: saldo disponivel nunca negativo. CA-E01: reserva maior que saldo e rejeitada sem debito.

### DESIGN
Pedidos e dono do estado do pedido; Estoque e dono do saldo e da reserva. Pedidos usa contrato ReservarItens(idPedido, itens) que retorna aceita/recusada. Pedidos nao acessa tabelas internas de Estoque. Para erro ou timeout, pedido permanece pendente e pode repetir com o mesmo identificador idempotente, conforme contrato de reserva.

### Plano e testes
CA-P01 -> Pedidos -> ConfirmarPedido -> teste de recusa com contrato de reserva simulado.
CA-E01 -> Estoque -> ReservarItens -> teste de saldo insuficiente e ausencia de debito.
Integracao -> contrato ReservarItens -> teste de timeout e repeticao idempotente, sem saldo negativo ou dupla reserva.

### Revisao de responsabilidades
Se GestorGeral confirma pedido, calcula saldo e debita estoque internamente, o revisor registra achado material: mistura de ciclo de Pedidos e regras de saldo de Estoque. A fonte e GestorGeral e suas operacoes; mover regras de reserva ao dominio Estoque e testar a fronteira.
Se ConfirmarPedido chama ReservarItens e aplica somente transicoes do pedido, a coordenacao e fina e aceita com essa justificativa. Contar linhas isoladamente nao decide nenhum desses resultados.

## Um dominio: Lista de tarefas

Responsabilidade: gerir tarefas pessoais. Conceitos: tarefa e conclusao. Invariante: concluir tarefa existente e operacao idempotente. Uma unica fronteira e suficiente porque linguagem e ciclo de vida sao os mesmos; nao dividir criacao e conclusao em dominios artificiais. CA-T01 -> Tarefas -> ConcluirTarefa -> teste de repeticao sem mudanca adicional.

## Demanda tecnica: normalizar saida de diagnostico

Nao introduz regra de negocio ou novo dominio. Responsabilidade tecnica: formatacao deterministica do diagnostico. Contrato: mesma entrada produz a mesma saida ordenada; nao inclui segredos. CA-D01 -> responsabilidade tecnica -> FormatadorDiagnostico -> teste de ordenacao e redacao. Justificativa: trata apresentacao tecnica e preserva as regras existentes.
