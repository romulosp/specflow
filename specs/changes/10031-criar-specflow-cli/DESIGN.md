# Design — SpecFlow CLI r2

Candidato, sem implementação. Dependências: núcleo 10029 r6 e consumidor 10030 r4 aprovados e entregues conforme seus contratos.

## Organização

Usar o pacote specflow já previsto em framework/src/specflow. Adicionar cli como adaptador fino de argparse, sem duplicar contracts/workflow/memory/validation. Rotinas consumer/configuration cuidam de init e recursos; integrations cuida somente de materialização de arquivos; assets contém allowlist autoral. Não importar módulo do consumidor para descobrir configuração.

framework/pyproject.toml define name=specflow-cli, version=0.1.0, requires-python >=3.11, dependencies vazias, build-backend hatchling.build e project.scripts specflow=specflow.cli:main. __main__ delega ao mesmo main. Recursos carregados via importlib.resources, sem depender do cwd do checkout. Hatchling e cobertura são ferramentas de desenvolvimento, não runtime; fixar suas resoluções no ambiente de build/teste antes da implementação.

Wheel universal Python e sdist construídos em ambiente isolado, com inventário explícito. Wheel reconstruído do sdist precisa conter o mesmo conjunto de recursos e passar o mesmo smoke; não prometer bytes de ZIP idênticos sem controlar timestamps. Build não baixa recursos do consumidor ou da documentação histórica.

## Consumidor e escrita

Metadados em .specflow/project.json e .specflow/managed-files.json; Changes em specs/changes, conhecimento em specs/knowledge; políticas fixadas sob .specflow/policies. Manifesto registra versão e SHA-256 de baseline por arquivo gerenciado, sem credenciais. Configuração operacional é somente configuracao.properties. Preservar AGENTS.md/.github/copilot-instructions.md existentes; instalar instrução complementar com nome próprio, sem substituir esses arquivos. Template inicial autoral pode criar AGENTS.md somente quando ausente.

managed-files.json não inclui seu próprio digest, evitando autorreferência; validar sua estrutura/versão, ownership e baselines dos demais arquivos. configuracao.properties real e conteúdo autoral não recebem baseline gerenciada que impeça o usuário de editá-los. Init aditivo mantém integrações já instaladas, inclusive se a chamada não trouxer --integration; não é mecanismo de remoção. O ignore não desfaz versionamento anterior de um arquivo nem é criptografia: sem executar Git, informar que esse estado não foi certificado.

Inicialização prepara todos os arquivos em memória, resolve caminhos e valida conflitos antes de escrever. Arquivo gerenciado idêntico é no-op; bytes divergentes geram bloqueio, sem reescrita. Configuração já existente é autoral e preservada, inclusive parcial; chaves novas exigem candidato futuro, não reset. .gitignore recebe apenas linha de proteção faltante, preservando o conteúdo e newline existente. Se uma regra posterior negar a proteção, reportar conflito antes da escrita; não alegar proteção efetiva.

Compartilhar o protocolo de lock/preflight/commit/rollback da 10030, sem segundo mecanismo no CLI. Pode acrescentar outra integração por init explícito na mesma versão: atualizar somente seleção/metadados gerenciados validados e criar arquivos novos; não tratar a atualização administrativa esperada como conflito genérico. Não atualizar template divergente, configuracao.properties ou instruções autorais.

Usar criação exclusiva para arquivos novos e temporário/replace para atualização permitida de metadados/ignore/gate, com comparação da baseline. Falha durante escrita reverte somente bytes ainda pertencentes à operação; modificação concorrente interrompe rollback daquele arquivo e gera diagnóstico explícito. Não prometer transação global do filesystem. Recusar links/junctions em destinos gerenciados e colisões/nome reservados do subconjunto portátil da 10030. Nenhuma chamada a Git.

## Rascunhos e handoff

nova-change usa maior prefixo numérico existente +1, com largura mínima de cinco dígitos, slug ASCII do objetivo e criação exclusiva; no consumidor vazio começa 00001. Caracteres originais ficam no texto do objetivo, nunca em comando de shell. Reservar ID numérico em .specflow/reservations com criação exclusiva para evitar colisão concorrente. IDs reservados não são reciclados após falha; informar reserva/limite sem sobrescrever. Não criar change.json válido ou alegar EM_REVISAO_SPEC enquanto os documentos forem somente placeholders; registro draft.json indica rascunho e não é entrada aprovada do núcleo.

Alocar ID sob o mesmo lock do projeto; consultar também todas as reservas, inclusive as de operações falhas. Limitar ID completo ao padrão/comprimento aceitos pela 10029 e truncar apenas o slug, nunca o objetivo autoral. Persistir draft.json conforme o contrato da 10029. Contexto reconhece esse registro como RASCUNHO; especificar/esclarecer podem preparar instrução sobre ele, revisar-spec bloqueia até contrato completo. Ao concluir especificação, o agente converte metadados explicitamente sem apagar os documentos preenchidos.

Para o slug, transliterar o objetivo por NFKD somente para o nome de pasta, converter ASCII em minúsculas e trocar separadores por hífen. Se não restar caractere ASCII, usar mudanca; nunca alterar/normalizar o objetivo guardado no JSON/documento. Esse tratamento do nome não altera regras de digest do conteúdo.

Handoff usa o catálogo docs/comandos/comandos.json: integrações selecionadas geram .agents/skills/specflow-*/SKILL.md e .github/prompts/specflow-*.prompt.md. Suporte autoral de auditoria fica em .agents/skills/security-audit e docs/security-audit, com protocolo/validador novos ou de direitos confirmados; não copiar skill legada sem confirmação de direitos. Todas as referências dos recursos embarcados precisam fechar dentro do consumidor.

JSON de operações administrativas/handoff: schemaVersion=1, operation, projectId/changeId quando disponíveis, outcome, phaseExecuted=false, localChecksExecuted, editorInstructions, findings, pending, limitations e exitCode. localChecksExecuted é lista vazia salvo as rotinas realmente chamadas, como security_gate. Resultado de core conserva o envelope definido na 10029. Sem timestamp de execução e com ordenação estável. Códigos de argparse também precisam de representação JSON quando --json for solicitado; erro usa reason ID/campo conhecido, nunca ecoa argv/valor desconhecido. Ajuda/versão não exigem projeto inicializado.

Pré-condições vêm da política do núcleo, não de cópias de enums na CLI. teste-humano sem aprovação apresenta instrução até revisão/decisão e código 1 com implementação bloqueada; com aprovação/plano válidos apresenta continuidade autorizada, sem declarar entrega executada. aprovar reúne as evidências e solicita registro humano pelo editor; CLI não possui comando de gravação de aprovação. encerrar reúne candidato e autorizações, sem movimentar ou versionar.

## Segurança e testes

doctor inspeciona versão do próprio pacote e existência de arquivos/declarações; não executa --version de recursos, probes de rede ou comandos de configuração. A guarda de recursos da 10030 é obrigatória em todos os adaptadores. Ausência de opcional não torna o núcleo indisponível; ausência de recurso necessário mantém o gate pendente.

doctor no consumidor novo íntegro retorna 0 mesmo com todos os opcionais em DEFINIR; exibe apenas disponibilidade e limitações. Valor preenchido inválido e baseline divergente geram 1; configuração lexicalmente inválida ou projeto malformado geram 2. Processo escritor ativo gera PROJECT_BUSY/1 antes de ler o conjunto em alteração. Não usar a lista de arquivos para declarar descoberta pelos clientes; isso permanece homologação separada.

A guarda PROJECT_BUSY de leitura é aplicada na entrada CLI. A operação de escrita que já detém seu lock pode chamar bibliotecas internas para conferir o próprio conjunto, sem redispatch de comando CLI ou autobloqueio. Não expor flag pública para ignorar lock. Identidade da reserva permanece interna ao executor; um mero campo JSON do consumidor não concede ownership.

validar confere revisão da implementação e invoca a função confiável do verificador empacotado com raiz e Change explícitas, sem shell/subprocesso nem carregamento de script do consumidor. Respeitar schema v1 de security-audit.json e saída security-gate.json; seu conteúdo não autentica reviewer. Gate 0 não promove VALIDADA/APROVADA. Não executar campos command das evidências.

Depois do gate, verificar evidenceManifest/binding da 10029 contra audit/gate, fontes-alvo, testes e evidenceRefs citados. Mesmo gate 0 mantém validação pendente se esses vínculos estiverem ausentes/antigos. Não criar binding de sucesso automaticamente para cobrir uma auditoria antiga; ele é evidência rastreável produzida pelo executor da auditoria. CLI pode gravar somente security-gate.json sob lock, nunca sobrescrever um destino autoral/incompatível ou seguir symlink. A função de suporte atual precisará ser adaptada/testada para essa escrita antes de ser embarcada; seus testes antigos não comprovam este contrato novo.

Testes unittest em consumidores temporários, coverage.py somente no ambiente isolado de testes e relatório por arquivo/agregado. Hooks bloqueiam rede/processos nas operações que não os permitem; cenários de conflito, links, concorrência e interrupção de escrita exercitam comportamento real. Homologação de editor é etapa separada com versão/evidência humana; presença de arquivo não equivale a descoberta pelo cliente.
