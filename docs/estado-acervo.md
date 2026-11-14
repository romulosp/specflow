# Cobertura e prontidão do acervo — 13/11/2026

Conferência incremental a partir do inventário, manifesto local e presença dos arquivos nos diretórios de suporte. Não repete a investigação semântica, não executa aplicações/infraestrutura, não altera o checkout externo e não autoriza nova extração ou implementação.

## O que já está aqui

| Grupo | Cobertura conferida | Limite |
| --- | --- | --- |
| Skills originais e recursos existentes | 324 arquivos, incluindo 92 SKILL.md; nenhum arquivo presente nesse diretório ficou fora | Cópia não comprova runtime, fechamento de referências ou direitos de publicação |
| Integração textual | Quatro arquivos de agentes/prompts incorporados | Descoberta e execução nos clientes ainda não homologadas |
| Processo e templates | Shared, templates e recursos reutilizáveis de Sprint locais | A Sprint concreta e estados de consumidores não foram adotados |
| Auditoria de segurança | Skill, gerador adaptado, gate de evidências e testes locais | Gate não é scanner; PDF não atesta auditoria real |
| ADR | Índice/template local e exemplo histórico incorporado | Exemplo não é arquitetura aprovada do SpecFlow |
| Auxiliares de qualidade | Dois arquivos Sonar incorporados; validadores Android/MJS e demais recursos existentes nas skills locais | Sonar/Docker/stacks não foram iniciados nem distribuídos como dependências do núcleo |
| Comandos novos | 11 comandos canônicos + alias, 24 arquivos de Skills/prompts; 104 Skills locais no total | Instruções para agente, não motor de workflow/CLI de produto já implementado |

O manifesto tem **360 recursos com proveniência**. No inventário de 24 componentes A e 102 B, 125 dos 126 componentes têm todos os arquivos incorporados. A exceção é o AGENTS original: o projeto possui **AGENTS próprio adaptado**, preservando limites, decisões humanas e escopo, sem adotar configurações particulares de outro consumidor.

## O que não está completo

1. **Recursos transitivos ausentes:** dos 149 pares históricos documento/destino em 30 diretórios de skills opcionais, três nomes de links foram corrigidos com substitutos locais existentes; restam 146 pares. Lista exata em dependency-resolution.json no acervo e notas DEPENDENCIAS-PENDENTES em cada skill afetada. São referências, não necessariamente 146 arquivos distintos. As operações dependentes permanecem bloqueadas; não criar placeholders para alegar completude.
2. **Ferramentas particulares excluídas:** oito arquivos de scripts não foram incorporados: três geradores de launchers de aplicações, três templates BAT específicos, um SQL de correção de aplicação e uma fixture de configuração. O mecanismo genérico de geração pode ser extraído/adaptado em Change própria; a cópia integral desses arquivos não é necessária para o núcleo atual.
3. **Operação não comprovada:** há checks de suporte e casos sintéticos, mas não homologação de todos os scripts/skills em suas stacks, nem teste de descoberta/execução dos comandos nos clientes. Gerador PDF exercitado em 13/11/2026 com exemplo sintético: uma página gerada, texto extraído e imagem inspecionada sem defeitos visuais. Não é auditoria real ou homologação integral.
4. **Núcleo executável:** contrato r6 da Change 10029 continua EM_REVISAO_SPEC, sem implementação iniciada. Ainda faltam biblioteca de contratos/gates/contexto/check, harness independente, testes de consumidores sintéticos e entrega manual real. Consumidor 10030 r4 e CLI 10031 r2 preparados para revisão, sem pacote ou execução real.
5. **Distribuição e atualização:** pacote instalável, init/new-change, ownership/lock, upgrade seguro/rollback, piloto e compatibilidade Windows/Linux continuam no roadmap, sem implementação/validação declarada.
6. **Direitos e nome:** MIT/copyright Rômulo Penha foram definidos para o material autoral. Terceiros mantêm licenças/avisos próprios; componentes de licença desconhecida e disponibilidade de marca continuam pendentes antes de publicação.
7. **Consolidação e contrato:** o [registro consolidado](../specs/shared/process/regras-consolidadas.md) reúne as regras e resolve a precedência. Núcleo 10029 r6 inclui cobertura/segurança/omissão/entrega humana; 10030 r4 integra configuração/apps e depende do núcleo validado. Reconciliação documental concluída, com aprovação humana e implementação ainda pendentes.

Relatórios PDF antigos, histórico de Changes, aplicações, memórias operacionais, logs e dados sensíveis não são ferramentas reutilizáveis do framework e não foram adotados como evidência atual.

## Próxima sequência recomendada

Obter decisão explícita sobre os contratos reconciliados; registrar plano preparatório; implementar e testar o primeiro incremento. Só depois avançar para pacote instalável e extensões, fechando suas transitivas e direitos por lote. O núcleo novo não depende dos recursos opcionais ausentes. [Registro corrente](../PENDENCIAS.md). Não importar recursos particulares ou promover SPEC_APROVADA automaticamente para aparentar conclusão.

Evidência: `imports/acervo-local-2026-11-12/coverage-check-2026-11-13.json`. A conferência atual da origem é por presença/caminhos, não nova validação de seus hashes ou revisão semântica integral. Os digests das 360 representações locais foram conferidos separadamente contra o manifesto atual.
