# Caminho até o framework SpecFlow autônomo

Planejamento candidato de 2026-11-12. SpecFlow usa processo Spec Driven próprio; nenhum host externo é pré-requisito. A arquitetura autônoma ainda será formalmente aprovada na [Change 10029](changes/10029-criar-nucleo-specflow/proposal.md).

Atualização em 13/11/2026: usuário definiu CLI + agente no editor, pacote specflow-cli e executável specflow. Contratos correntes: núcleo 10029 r6, consumidor 10030 r4 e [CLI 10031 r2](changes/10031-criar-specflow-cli/proposal.md). Todos em revisão, sem código/pacote implementado. A primeira distribuição é wheel local; publicação e atualização aplicada de consumidor ficam fora. Linhas abaixo mantêm a decomposição dos incrementos, sem ampliar o escopo aprovado.

Suporte já preparado por pedidos específicos: onze [comandos de agente e diagramas](../docs/comandos/COMANDOS.md), mais alias de teste humano, recursos locais de auditoria/ADR e MIT/copyright Rômulo Penha para o material autoral. Isso não substitui a aprovação e implementação dos incrementos abaixo nem libera direitos de terceiros. [Cobertura e pendências do acervo](../docs/estado-acervo.md).

| Incremento | Resultado concreto | Gate e evidência de saída |
| --- | --- | --- |
| I1 — Núcleo | Política das sete fases, contratos, avaliação de gates, contexto e check com harness local | SPEC própria aprovada; positivos/negativos; dois consumidores sintéticos; revisão, validação e aceite manual |
| I2 — MVP local | Pacote instalável isolado; init com configuracao.properties/DEFINIR e geração em apps (Change 10030), new-change em rascunho, context, check e upgrade-plan; manifesto, lock e ownership | SPEC própria; recursos DEFINIR não executados, instalação repetida sem sobrescrever documento autorado; contexto privado por consumidor; funcionamento offline |
| I3 — Atualização protegida | Comparação por baseline, conflitos, backup e rollback de arquivos gerenciados | Nova SPEC; customização e memória preservadas; conflito bloqueia aplicação; rollback demonstrado |
| I4 — Extensão piloto | Contrato de capacidades e uma extensão técnica opt-in, criada ou liberada individualmente | Stack ausente não quebra core; dependências/licenças fechadas; falha real detectada; sem execução por leitura |
| I5 — Piloto humano | Consumidor real escolhido expressamente, documentação e suporte de retomada | Autorização específica do consumidor; teste e aceite humanos; Protótipo não é piloto automático |
| I6 — Release | Pacote versionado, changelog, hashes, compatibilidade e suporte | Direitos/nome resolvidos, execução Windows/Linux comprovada, autorização expressa de publicação |

A importação de componentes existentes é trilha opcional, com allowlist, direitos e autorização expressa de extração por lote. Não é dependência implícita da implementação nova de I1. Nunca copiar o acervo inteiro ou atribuir licença por inferência. Não criar remoto, push ou publicar para satisfazer artificialmente um marco.

Cada incremento terá proposta, SPEC, design, tarefas, aceites negativos e plano preparatório após SPEC_APROVADA. Geração dos documentos não aprova seu conteúdo. A implementação e o aceite final são eventos diferentes.

Riscos herdados: direitos do acervo, nome provisório, divergência de encerramento, falsas alegações de gate, dados privados no conhecimento global e sobrescrita em atualização. O núcleo reduz parte desses riscos; testes de aplicações e capacidades técnicas continuam pertencendo às extensões/consumidores.
