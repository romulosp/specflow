# Change 10031 — SpecFlow CLI

Status: `EM_REVISAO_SPEC`. Revisão r2, 13/11/2026. SPEC_APROVADA: pendente.

Copyright (c) 2026 Rômulo Penha. MIT para o material autoral.

## Pedido e resultado

O usuário escolheu pacote specflow-cli, executável specflow e execução de desenvolvimento pelo agente no editor. Depois pediu expressamente executar o plano completo. Essa fonte autoriza a limpeza documental e a preparação dos contratos; a sequência aprovada do plano exige revisão e aprovação humana das SPECs antes da implementação. Não registrar a aprovação de um contrato que ainda não havia sido apresentado.

Entregar ferramenta Python instalável por wheel local, independente do ambiente de desenvolvimento: inicializar consumidores, criar rascunhos de Changes, conferir gates e preparar instruções para Copilot e Codex. O agente realiza especificação, código e revisão. Sucesso de uma preparação não é conclusão da fase. Não haverá chamada automática a IA no terminal.

## Escopo e dependências

- Núcleo e contratos: Change 10029 r6. Inicialização, propriedades e geração confinada: Change 10030 r4. Não duplicar essas implementações.
- Entry point, parser, doctor, nova-change, comandos de fase, adaptadores de editor e pacote com recursos explicitamente selecionados.
- Suporte obrigatório autoral: políticas, templates, comandos e protocolo/gate de segurança. Componentes com direitos desconhecidos ou transitivas incompletas ficam fora do wheel e da distribuição de fontes.
- Documentação de instalação local, comandos, diagrama e roteiro humano; build e hashes; testes, cobertura, auditoria e revisão.

Fora de escopo: publicação, remoto/Git implícito, instalação global de ferramentas auxiliares, serviço de IA próprio, execução de infraestrutura, extração definitiva, migração de consumidores e atualização aplicada de projetos.

## Estratégia

R2 resolve o caminho inicial nova-change → contexto, a saída saudável de doctor com opcionais em DEFINIR, init aditivo com lock compartilhado e a validação dos vínculos de evidência além do gate v1. Uma distribuição Python, bibliotecas internas e CLI fino evitam três implementações de política/escrita. [Decisão técnica proposta](../../../docs/adr/ADR-001-cli-local-e-gates.md); [achados e tratamentos](../../../docs/cli/AJUSTES-TECNICOS.md).

Uv é a instalação recomendada, não dependência de runtime. Distribuição Python padrão com wheel/sdist, Python >=3.11, argparse e Hatchling. Primeiro instalar o wheel em ambiente de teste isolado; instalar no ambiente pessoal do usuário não é efeito automático da validação. Atualizar o pacote não escreve nos consumidores.

Não vender o suporte local como CLI implementado. O objetivo só será satisfeito com executável real, pacote contendo os recursos necessários, evidências e entrega humana vinculada ao build. Declaração de compatibilidade Windows/Linux e integração visual depende de execução nos respectivos ambientes.

## Gate

Contrato revisável: [SPEC](spec.md), [design](DESIGN.md), [tarefas](tasks.md) e manifesto evidence/contract-r2.json. Após SPEC_APROVADA vigente, preparar implementation-plan.md antes de código. A aprovação desta Change não aprova automaticamente 10029/10030 nem o aceite final do produto.
