# Revisão técnica da implementação — 0.1.0

14/11/2026. Revisor: assistente executor desta sessão; sem revisão independente. SPECs correntes aprovadas: 10029 r6, 10030 r4 e 10031 r2. O manifesto compartilhado identifica o escopo autoral novo e os artefatos reais.

## Confronto com o contrato

| Área | Implementação e verificação |
| --- | --- |
| 10029 RF-01/04/10/15 | storage, contracts, policy: validação fechada, perfis, vínculos e confinamento; testes de tipos, duplicatas, codificação, hashes, caminhos e política |
| 10029 RF-02/03/05/12/13/14 | workflow e validation: sete gates, decisão tipada, cobertura por arquivo, auditoria e omissão; testes positivos/negativos, contrato alterado, resultados manuais e segurança insuficiente |
| 10029 RF-06/07/09/11/16 | memory, harness e adaptador CLI: rascunhos, contexto, supersessão, conflitos, duas raízes e leitura sem escrita; testes repetidos com snapshots |
| 10029 RF-08 | validation.matrix compara enums de método e IDs; structural não substitui functional/manual; referências e provas atuais verificadas |
| 10030 INIT-01..08 | configuration, consumer, fileops e recursos: 25 propriedades, preservação literal, DEFINIR/parciais, segredo redigido, ignore, integração aditiva, lock e rollback; suíte funcional/negativa |
| 10030 APP-01..03/GATE-01..02 | generate_application confina em apps, exige aprovação/plano/escopo e preserva existentes; serviços nunca ativados; tentativa sem pré-condição bloqueada |
| 10030 QUAL-01 | Cobertura atual por arquivo, testes e fonte vinculados; sem excluir código gerado ou estimar percentuais |
| 10031 CLI-01/02/16/19 | pyproject/entry point e recursos autorais; build a partir do sdist, instalação/reinstalação offline isolada, versão igual no console/módulo, snapshot preservado, inventário e hashes |
| 10031 CLI-03..08/20 | Bibliotecas comuns compartilhadas, init, doctor e rascunhos; preflight/lock, campos DEFINIR, metadados, IDs e erro redigido; mesmos mecanismos exercitados pela API e CLI |
| 10031 CLI-09..15/21 | Catálogo único, instruções e pré-condições; phaseExecuted=false; validar usa rotina empacotada e não executa JSON/script do consumidor; vínculos ausentes/antigos bloqueiam; decisões e encerramento não são fabricados |
| 10031 CLI-17 | Windows real exercitado. Linux e descoberta/invocação nos clientes permanecem not_run; critério não aprovado por presença de arquivos |
| 10031 CLI-18 | Testes/cobertura reais antecedem esta revisão; limites e segurança registrados separadamente |

A matriz detalhada de requisitos, tarefas, arquivos e métodos está em `acceptance-matrix.json` de cada Change. Referências aos testes apontam para funções existentes e para a saída real da suíte. Registros técnicos vinculam contrato + implementação, evitando reaproveitar evidência de uma SPEC alterada. Manifestos de artefatos evitam tratar existência de arquivo como prova suficiente.

Cobertura conferida: 1.280/1.324 linhas (96,68%) e branches 341/368 (92,66%). Todos os arquivos executáveis superam 80%; docstring isolada sem instruções é artefato não executável, sem exclusão de fonte. O único skip de symlink é explicitado; junction e hardlink foram exercitados no Windows.

## Resultado

**IMPLEMENTACAO_APROVADA no escopo técnico local revisado**, sem divergência material de código identificada. Isso permite executar os checks locais de validação; não aprova o critério de homologação indisponível, não declara VALIDADA e não representa aceite humano final. Falta de Linux e dos clientes reais permanece limitação de validação, sem ser ocultada como sucesso.

Não houve alteração de código durante esta revisão. A revisão e a auditoria foram realizadas pelo executor; uma revisão independente continua recomendável antes de distribuição pública. Evidências não autenticam automaticamente a pessoa declarada. Publicação, instalação pessoal, archive e commit permanecem fora desta entrega.

## Retorno e nova revisao do recurso

IMP-REV-001: a conferencia final detectou divergencia entre nomes de Skills auxiliares no catalogo e guias realmente distribuidos. Retorno a implementacao registrado antes da correcao. O catalogo canonico agora nomeia guias locais autorais, utilizados de forma identica pelo CLI, Skills e prompts. Todos os 24 arquivos gerados foram conferidos contra a versao anterior antes da substituicao; nenhum arquivo autoral desconhecido foi sobrescrito. Regressao test_packaged_catalog_matches_every_editor_instruction verifica descricao/passos/guias/aliases no consumidor. Nova suite: 51 testes (50 aprovados/um skip), build e instalacao isolada repetidos. Achado resolvido; este parecer refere-se aos novos hashes.
