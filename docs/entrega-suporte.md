# Entrega de suporte e comandos — 12/11/2026

Pedidos do usuário executados: recursos locais, neutralização de identificadores de ambiente, copyright Rômulo Penha/MIT autoral, complemento de auditoria/ADR e comandos por fase com diagrama.

## Entregas concretas

- [Guia dos onze comandos](comandos/COMANDOS.md), com Skills Codex, prompts Copilot, alias speckflow-teste-humano, entradas, resultados e gates.
- [Diagrama SVG](comandos/fluxo-comandos.svg), [PNG](comandos/fluxo-comandos.png) e [fonte Mermaid](comandos/fluxo-comandos.mmd).
- [Gerador local de relatório](security-audit/README.md), com dados explícitos e sem conclusões históricas embutidas. Sintaxe/entrada verificadas; nenhum PDF de auditoria gerado.
- [ADRs](adr/README.md): índice, template e exemplo histórico não adotado como decisão vigente.
- [Licença MIT](../LICENSE) com copyright Rômulo Penha, [escopo](../LICENSE-SCOPE.md) e [avisos de terceiros](../THIRD_PARTY_NOTICES.md).
- Acervo de 360 recursos com proveniência; onze comandos autorais e um alias, totalizando 104 definições locais. Lacunas herdadas de extensões opcionais permanecem registradas.

## Verificação e limites

`python -B tools/gerar_comandos_specflow.py --check` compara os 24 arquivos gerados ao catálogo sem executar as fases. O verificador local confere integridade, links, sintaxe e fixtures; não lê outro checkout. O parser Mermaid confirmou a fonte, o renderizador produziu SVG e o PNG foi visualmente inspecionado. Dependências de renderização estão fixadas localmente; não houve instalação global ou navegador/infraestrutura iniciado.

Falhas iniciais do renderizador/validador em Windows foram corrigidas na cópia local com file URLs ESM e DOM de validação. A exportação final elimina fontes remotas e CSS vars que não eram suportadas pelo rasterizador. A versão entregue foi validada novamente.

Evidência consolidada em `imports/acervo-local-2026-11-12/delivery-check.json`. A varredura de nomes/conteúdo verifica ausência do identificador retirado; backup exato ficou fora da árvore e não é dependência operacional. Histórico editado é derivado neutralizado, sem alegação de conservar seus hashes antigos.

Resultado final: 35 checks locais e 23 checks consolidados aprovados, zero falhas. Varredura em 11.619 arquivos sem ocorrência do identificador removido. Comparação somente leitura confirmou os 1.385 arquivos do corpus e os três recursos complementares, além de HEAD/status Git preservados no checkout externo. O manifesto do contrato r3 e seus quatro documentos correspondem; G02 continua pendente.

As Skills/prompts foram verificados como arquivos; não houve teste de sua descoberta visual nos clientes ou execução de uma fase completa por eles. Recarregue a sessão se os nomes novos não aparecerem. Eles não são um binário de shell nem tornam pronto o núcleo do framework.

## Estado do produto

Atualização em 13/11/2026: acrescentados `specflow-teste-humano` e alias `speckflow-teste-humano`, com parada em IMPLEMENTADA e teste do usuário pendente. Acrescentado gate obrigatório de evidências de segurança em specflow-validar: a skill analisa a implementação; `docs/security-audit/verificar_seguranca.py` bloqueia avanço se há achados abertos, auditoria incompleta/desatualizada ou checks falhos/não executados. Não é scanner autônomo; o gerador PDF continua separado. Evidência desta atualização em `docs/comandos/evidence/2026-11-13-comandos-e-seguranca.json`.

Determinação adicional de 13/11/2026: `specflow-validar` é a execução padrão da fase de validação da implementação em fluxos autorizados. Só um prompt explícito do usuário pode pedir a não execução; registrar solicitação, motivo, revisão e fase não executada, mantendo gates posteriores pendentes. Isso não amplia comandos de fase única, não ultrapassa teste-humano e não transforma falha em dispensa. Se executada a fase, auditoria e gate de segurança continuam obrigatórios. Catálogo/24 arquivos e 36 checks locais conferidos; nenhuma fase real foi executada nesta alteração de instruções.

Consolidação posterior em 13/11/2026: [40 regras registradas](../specs/shared/process/regras-consolidadas.md), cobertura mínima medida de 80%/meta 90% obrigatória na implementação, comandos e modelos propagados, fallback de cobertura por LLM removido e orquestrador legado harmonizado com decisões humanas. Configuração .properties/DEFINIR e geração em apps especificadas na Change 10030 r1, ainda em revisão; nenhum init ou geração real executados. Dados de autenticação opcionais são proposta técnica do contrato, não capacidades de integração já homologadas.

Conferência dessa consolidação: 14 checks documentais aprovados, zero falhas; 25 propriedades do template em DEFINIR; 24 definições geradas conferidas e 36 checks de suporte aprovados. Não são percentuais de cobertura do produto ou validação funcional de init/geração. Evidência em docs/comandos/evidence/2026-11-13-regras-consolidadas.json.

Change 10029 está em EM_REVISAO_SPEC, contrato r4, com aprovação humana pendente; inicialização 10030 está em r2. Nenhuma tarefa de implementação do núcleo foi executada. Criar comandos não autoriza chamar implementar para o contrato pendente. Aprovação de SPEC, aceite final, encerramento, commit e publicação são condições distintas. Nenhum desses eventos foi inventado nesta entrega.

Atualização de fechamento em 13/11/2026: contratos reconciliados com cobertura/segurança/omissão/entrega humana; três nomes de links corrigidos, 146 referências opcionais ainda ausentes com notas de limitação. Exemplo sintético de PDF gerado, texto extraído e página inspecionada visualmente. Registro corrente em [PENDENCIAS](../PENDENCIAS.md); os números e revisões das seções anteriores representam as respectivas rodadas históricas.
