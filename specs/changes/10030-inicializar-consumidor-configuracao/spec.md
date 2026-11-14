# SPEC — Inicialização e configuração do consumidor

Status: `EM_REVISAO_SPEC`. Revisão r4, 13/11/2026. SPEC_APROVADA: pendente.

## Requisitos e critérios verificáveis

| ID | Requisito | Aceite |
| --- | --- | --- |
| INIT-01 | Inicialização nova sempre cria configuracao.properties na raiz do consumidor, mesmo sem integrações habilitadas | CA-I01: arquivo existe; todas as propriedades de recursos geradas têm valor DEFINIR; nenhuma conexão/processo/download de recurso foi tentado |
| INIT-02 | Todos os recursos reconhecidos pelo framework/extensões declaram seus campos no catálogo e usam esse arquivo como entrada autoral de configuração operacional | CA-I02: recurso sem declaração de propriedades não pode executar; arquivo contempla os campos declarados; não há URL/credencial implícita de outro projeto ou fallback de ambiente sem contrato |
| INIT-03 | Qualquer valor DEFINIR na seção de um recurso mantém esse recurso inativo, inclusive em configuração parcial | CA-I03: URL preenchida com usuário/token ainda DEFINIR resulta em zero tentativas de uso; demais recursos independentes não são desativados |
| INIT-04 | Falta, vazio, formato inválido ou autenticação não suportada também impedem uso; informações preenchidas não executam o recurso automaticamente | CA-I04: arquivo válido só produz disponibilidade de configuração; recurso só é chamado por ação autorizada; sem sondagem de rede, login, --version ou startup em recurso inativo |
| INIT-05 | Credenciais e endpoints operacionais têm fonte autoral única local, sem serem logados, copiados para templates/pacotes ou versionados automaticamente | CA-I05: inicialização adiciona regra idempotente de ignore do arquivo real, sem sobrescrever .gitignore; logs/relatórios mostram chaves/estado e não valores; template contém somente DEFINIR |
| INIT-06 | Chamadas repetidas preservam valores autorais e não recriam ou sobrescrevem aplicações | CA-I06: preencher propriedades e criar arquivo em apps, repetir init/geração; bytes autorais preservados; conflito é reportado antes de escrever; campo novo exige plano/candidato sem reset de valor existente |
| APP-01 | Toda geração de aplicação cria ou reutiliza `<raiz-consumidor>/apps/` antes de escrever o código | CA-A01: em consumidor limpo, primeira geração aprovada cria apps; fontes da aplicação ficam abaixo dessa pasta; código interno do framework não é movido para apps |
| APP-02 | Identificador, destino e links de geração permanecem confinados a apps; nenhum arquivo existente é apagado/movido/sobrescrito silenciosamente | CA-A02: IDs com travessia, apps como arquivo e link que escape da raiz são rejeitados sem escrita fora da área autorizada; repetição não duplica ou perde aplicação existente |
| GATE-01 | Inicializar não aprova SPEC; gerar código exige SPEC_APROVADA vigente e escopo de destino autorizado | CA-G01: inicializar com DEFINIR não libera implementação; geração sem aprovação é bloqueada antes de criar código |
| GATE-02 | Recurso inativo obrigatório para cobertura/segurança mantém o gate pendente, sem tentativa de uso ou fallback de aprovação | CA-G02: coletor de cobertura em DEFINIR não é executado e implementação não é aprovada; Sonar inativo não simula auditoria/cobertura executada |
| QUAL-01 | Código implementado possui testes e cobertura atual mínima de 80%, meta 90%, conforme política universal | CA-Q01: relatório por arquivo/escopo, suíte aprovada, falhas/limites e cenários negativos; sem aferição suficiente, não concluir/aprovar implementação |
| INIT-07 | Properties segue gramática própria explícita, sem interpretação Java/shell ou interpolação | CA-I07: UTF-8 LF/CRLF/BOM, valor com = e caminho Windows literal são preservados; duplicata, linha inválida e chave desconhecida geram erro 2 sem ativação; marcador compara espaços/caixa sem alterar senha literal |
| INIT-08 | Reinit pode acrescentar integração declarada, preservando configurações e arquivos autorais, com exclusão mútua das escritas | CA-I08: iniciar Copilot e depois acrescentar Codex preserva bytes anteriores e atualiza somente metadados gerenciados; conflito/lock/falha concorrente não sobrescreve conteúdo autoral nem apaga alteração de outro escritor |
| APP-03 | Destinos gerados obedecem ao subconjunto portátil Windows/Linux e não escrevem por links | CA-A03: nomes reservados, trailing dot/space, colisão por caixa, paths com drive/UNC/travessia e symlink/junction no destino são rejeitados antes de escrita; atualização de metadado por replace não altera inode externo por hardlink |

## Semântica de DEFINIR e autenticação opcional

Valores iniciais são exatamente DEFINIR. A detecção ignora caixa e espaços externos para impedir ativação acidental por ` definir `. Não procurar substring dentro de uma URL válida. DEFINIR é reservado; não é informação de autenticação utilizável. Um DEFINIR em recurso A não bloqueia B, mas A inteiro permanece inativo enquanto qualquer campo declarado dele contiver o marcador.

Campos de usuário, senha, token e modo de autenticação são declarados pelos adaptadores, não universalmente exigidos de serviços sem autenticação. Contrato r4 para revisão: NAO_APLICAVEL pode ser usado explicitamente em campo declarado opcional para o modo escolhido; não é aceito em URL, executável ou credencial obrigatória. Nenhum campo DEFINIR será tratado como opcional preenchido. Modo não suportado mantém o recurso inativo, sem tentar descobrir suporte remotamente. O catálogo de cada integração e sua compatibilidade precisam ser validados na implementação própria.

## Limites não funcionais

Gramática de properties: UTF-8 estrito com BOM inicial opcional, LF ou CRLF; cada linha é vazia, comentário iniciado por # após espaços, ou chave=valor dividido no primeiro =. Chaves são ASCII e declaradas pelo catálogo, sem repetição. Remover espaços externos somente da chave e para comparar o marcador DEFINIR/NAO_APLICAVEL; o valor literal é preservado para o adaptador, inclusive espaços e = em credencial. Não há escapes Java, continuação de linha, expansão de ambiente, aspas especiais ou interpolação. Backslash é literal. Formato inválido/duplicata/chave desconhecida invalida a leitura inteira com erro 2 e zero execução; falta de campo válido mantém apenas o recurso correspondente inativo. Valor real nunca aparece no diagnóstico.

Escrita compartilhada usa o protocolo de bloqueio/preflight/commit do design. A reserva do lock é metadado operacional permitido antes do preflight, não escrita de conteúdo do projeto. Instalação antiga incompatível exige plano de atualização, não reinit que resete versões ou arquivos. Inclusão aditiva de integração da mesma versão por chamada explícita de init não é upgrade aplicado.

- init e leitura de configuração não executam recursos; campos são dados, sem eval, interpolação em shell ou importação de código do consumidor.
- UTF-8, chaves de recurso explícitas; duplicatas/formato inválido geram diagnóstico e zero ações externas.
- Não manter credenciais operacionais duplicadas em JSON/lock/memória. Metadados internos de projeto podem continuar estruturados, sem substituir ou sobrepor valores desse arquivo.
- Arquivo real não é cofre/criptografia por si só; manter privado e fora da distribuição. Não copiar seus valores para backup público, logs ou evidências.
- Planejar e testar Windows e Linux antes de declarar compatibilidade; falta de ambiente permanece limitação.
- Nesta Change apenas proposta/SPEC/design/tasks estão sendo preparados; nenhum critério acima foi executado em runtime.

## Integração com a 10029 r6

O manifesto de implementação e registros de cobertura/segurança/execução/entrega obedecem ao contrato público do núcleo. properties é a fonte de URL/credenciais; project.json contém apenas identidade, política e caminhos. Configuração preenchida não aprova Change. Recursos exigem guarda em todo adaptador; helpers legados não são chamados diretamente para contornar DEFINIR. NAO_APLICAVEL é reservado a campo explicitamente dispensável no modo declarado; jamais substitui URL ou credencial obrigatória. Catálogo inicial é versionado e qualquer extensão sem declaração de campos é recusada, sem detecção remota ou tentativa de executar.
