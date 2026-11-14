> Copia editorial neutralizada. Metricas e verificacoes abaixo sao historicas; originais exatos foram preservados em arquivo externo de auditoria. Links locais mostram recursos atuais, nao provam igualdade com o original.

# Extração futura, evolução e backlog

## Estratégia reversível

Nenhuma etapa abaixo foi executada. Aprovação de arquitetura e autorização de extração são pré-condições distintas. O Protótipo continua independente e não será consumidor piloto automático.

| Etapa | Ação e dependências | Evidência de saída | Reversibilidade |
| --- | --- | --- | --- |
| X0 — Decidir | Aceitar diagnóstico, escolher alternativa, liberar proveniência/licenças e nomenclatura | Decisões humanas vinculadas ao dossiê | Sem arquivos transferidos |
| X1 — Contratar | Nova Change aprovada para implementação; fixar core, políticas, contratos e versões | SPEC/Design/tasks e matriz de compatibilidade | Cancelar Change sem tocar origem |
| X3 — Selecionar | Copiar somente candidatos A liberados, preservando origem/hash/avisos; separar regras particulares em fixture | Manifesto allowlist sem dependências do Protótipo | Remover pacote candidato no laboratório |
| X4 — Fechar | Resolver transitivas/licenças e substituir parâmetros locais por configuração; nenhuma alteração retroativa na origem | Testes negativos e validação de recursos | Voltar à versão candidata anterior |
| X5 — MVP | Instalar e testar init, new-change, context, check e upgrade-plan em dois projetos sintéticos | Mesma release funciona em ambos, memórias isoladas | Rollback do pacote/arquivos gerenciados |
| X6 — Extensões | Uma extensão técnica por vez, contrato/capacidades e cenários próprios | Cada extensão instalada e removida isoladamente | Desabilitação/remoção comprovada sem resíduo operacional |
| X7 — Piloto humano | Consumidor expressamente escolhido e autorizado, sem migração automática do Protótipo | Aceite humano, documentação de suporte e release candidata | Backup/rollback aprovado pelo consumidor |
| X8 — Release | Publicar somente após validação e autorização próprias; changelog, hashes, licença e compatibilidade | Release reproduzível e pacote de teste independente | Fixar versão anterior; nunca reverter conhecimento autoral |

## Proposta de MVP

Pacote local pequeno com política versionada, templates genéricos, manifesto/lock e recuperação de contexto baseada em fontes. Operações candidatas: `init`, `new-change`, `context`, `check` e `upgrade --plan`. A sintaxe exata pertence à SPEC futura. A inicialização não aprova contratos; new-change cria rascunho; context/check não promovem estado. Upgrade com aplicação automática fica fora do primeiro MVP, mantendo plano/candidatos para revisão.

O MVP inclui ADR/lição/pendência vinculados à revisão/evidência. Não inclui servidor, UI, IA obrigatória, banco vetorial, telemetria, execução autônoma de infraestrutura nem todas as skills. CLI e integrações de editor são próprios do SpecFlow, entregues por incrementos contratuais.

## Backlog priorizado

P0 bloqueia publicação/extração; P1 compõe o MVP; P2 evolui após validação. Estimativas de prazo não atribuídas sem equipe/capacidade definida.

| Item | Prioridade | Dependências | Resultado esperado | Critério de aceite |
| --- | --- | --- | --- | --- |
| BL-01 — Decisões e direitos | P0 | Dossiê, titulares e DEC-01..04 | Seleção aprovada e licença/proveniência por item | Nenhum arquivo sem direito conhecido no pacote público |
| BL-02 — Política canônica | P0 | BL-01; D-01/D-06 | Estados e transições únicas, incluindo encerramento | Transição inválida bloqueada; alteração de contrato invalida aprovação anterior |
| BL-03 — Recursos transitivos | P0 | BL-01; D-03 | Manifesto fechado por extensão | Recurso ausente causa erro; sem link para compose-performance inexistente |
| BL-04 — Segurança/ownership | P0 | BL-01; D-10/D-12 | Papéis de arquivo e capacidades explícitas | Sem execução por leitura/instalação de memória; nenhum dado de consumidor no pacote |
| BL-05 — Contratos/configuração | P1 | BL-02/04 | Schema versionado e lock | Config inválida, ciclo e caminho fora da raiz rejeitados |
| BL-06 — Templates/init | P1 | BL-03/05 | Inicialização repetível sem cópia manual | Segunda execução não duplica nem sobrescreve documento autorado |
| BL-07 — Contexto e reconciliação | P1 | BL-02/05 | Estado com proveniência e conflitos | STATUS divergente não promove fase; resumo ausente gera pendência clara |
| BL-08 — ADR e lições | P1 | BL-07 | Justificativas e conhecimento recuperáveis | Decisão substituída é identificada; lição tem ação e aplicabilidade |
| BL-09 — Verificador de governança | P1 | BL-02/03/05 | Achados e rastreabilidade de aceite | RF sem tarefa/teste indicado; retorno com códigos e limites corretos |
| BL-11 — Distribuição/CI | P1 | BL-03/06/09 | Wheel/release com hashes e smoke independente | Instala em Windows/Linux sem path/rede do Protótipo |
| BL-12 — Upgrade-plan/rollback | P1 | BL-05/06/11 | Plano seguro de atualização | Customização e memória preservadas; conflito impede sobrescrita |
| BL-13 — Extensão piloto | P2 | BL-03/04/09/11 | Validador técnico opcional com dependências | Ausência da stack não quebra core; negativo real falha |
| BL-14 — Piloto e operação | P2 | BL-07..12, autorização própria | Consumidor humano com instruções de suporte | Retomada por outro executor funciona só com fontes/pacote |
| BL-15 — Acervo ampliado | P2 | BL-01/03/13 | Importação gradual de skills liberadas | Cada lote tem testes de recursos, licenças, conflitos normativos e compatibilidade |

## Riscos técnicos e de evolução

| Risco | Gravidade | Tratamento / evidência de encerramento |
| --- | --- | --- |
| Gates declarados sem execução | Alta | Separar evidência de alegação; cenários negativos BL-02/09 |
| Direitos ou autoria desconhecidos | Alta | BL-01; licença local não cobre outras pastas |
| Dependência implícita de caminhos/segredos | Alta | Configuração explícita e sandbox; nenhum arquivo real de chaves usado |
| Vazamento de memória entre consumidores | Alta | Armazenamento local, isolamento em dois projetos e exportação sanitizada |
| Regras técnicas incompatíveis | Média/alta | Extensões opt-in e ADR; validador de estrutura JS não pode impor sua convenção ao backend Java |
| Escopo virar sete engines antes do MVP | Média | Fronteiras internas e prova de necessidade antes de separar runtime |
| Upgrade destruir documentação autoral | Alta | Baseline/ownership, conflito e backup; memória fora da substituição |
| Falso sucesso de verificador estrutural | Alta | Método/escopo explícitos e teste de erro; não usar exit 0 sozinho como aprovação |
| Índice de contexto obsoleto | Média | Índice reconstruível, referências por revisão/hash e conflito visível |

## Critérios de validação da futura extração

| Cenário | Aceite obrigatório |
| --- | --- |
| Independência física | Executar pacote em diretório sem acesso ao Protótipo; nenhuma referência runtime à origem |
| Integridade/licença | Manifesto, digests, recursos transitivos e avisos completos; recusar pacote adulterado |
| Inicialização | Criar dois consumidores sem copiar arquivos manualmente; repetir sem efeito destrutivo |
| Governança negativa | Bloquear implementação sem SPEC aprovada, aprovação com achado importante e archive sem gates |
| Alteração pós-aprovação | Alterar contrato e exigir nova revisão vinculada ao novo hash |
| Estado contraditório | STATUS diz VALIDADA e revisão atual reprova: mostrar conflito e bloquear promoção |
| Memória e retomada | Recuperar fase, justificativas, Changes, lições e pendências em sessão nova, só das fontes do consumidor |
| Isolamento | Criar marcador sintético privado em A; ausente no contexto/exportação de B e pacote global |
| Extensão ausente/conflitante | Core continua operável; reportar incompatibilidade antes de executar qualquer ferramenta |
| Segurança de entrada | IDs/caminhos maliciosos e arquivo fora da raiz rejeitados; não interpolar argumentos em shell |
| Customização/upgrade | Template local alterado e memória permanecem; conflito gera plano sem sobrescrita |
| Rollback | Restaurar apenas arquivos gerenciados e versão; preservar decisões e conhecimento autoral |
| Plataformas/offline | Windows/Linux testados; pacote instalado executa check/context sem baixar dependências |
| Prontidão humana | Relatórios, limites, piloto e decisões aprovados antes de publicar ou migrar consumidor |

Estes são critérios futuros, não testes já aprovados. Aprovação formal da presente investigação não declara o framework pronto para reutilização.
