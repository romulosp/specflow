# Design candidato — inicialização e configuração

Revisão r4. Depende dos contratos de evidência e gates da Change 10029 r6. Interfaces lógicas propostas, sem CLI/binário implementado:

1. `initialize_consumer(root, catalog)`: cria somente esqueleto autorizado, template privado configuracao.properties com valores DEFINIR e regra de ignore. Não inicia integrações.
2. `resolve_resource(id, properties)`: valida campos/estado e retorna inativo por configuração, configuração inválida ou disponível para uma ação autorizada. Não testa rede nem executável.
3. `generate_application(root, id, templates, approved_scope)`: verifica gate de SPEC, confinamento e conflitos; prepara apps e escreve somente destinos autorizados sem conflito.

## Propriedade dos arquivos

| Artefato | Dono e atualização |
| --- | --- |
| configuracao.properties | Consumidor; criado com DEFINIR e passa a ser autoral. Nunca substituir valores preenchidos por upgrade/reinit |
| configuracao.example.properties | Template sem segredos reais; catálogo versionado do framework |
| Catálogo de recursos | Framework/extensão; ID, campos, tipos, obrigatoriedade/autenticação suportada e capacidades; não contém credenciais |
| Metadados/lock internos | Ferramenta; versões/digests/ownership, sem URLs privadas ou credenciais duplicadas |
| apps/ | Código e dados autorais do consumidor; geração não pode apagá-los para obter idempotência |

Não há dependência de um checkout anterior. O exemplo desta Change é modelo inicial, não afirma que todas as Skills copiadas já possuem adaptador executável. Toda capacidade adicional deve declarar campos, modo de autenticação e política de execução antes de entrar no catálogo.

## Resolução e bloqueio

Carregar catálogo local → parsear propriedades como dados UTF-8 → validar campos sem I/O externo → identificar qualquer DEFINIR do recurso → manter inativo; só depois conferir completude/tipos/compatibilidade. Sem marcador mas com faltante/vazio/inválido, também inativo. Disponível não é executado: o chamador precisa de fase/ação e autorização aplicáveis.

Autenticação opcional: modo selecionado deve declarar campos necessários e dispensáveis. NAO_APLICAVEL é representação proposta de decisão explícita para campo dispensável, nunca credencial padrão. Não passar marcadores ao serviço. Não assumir suporte a usuário/senha/token em determinada versão de Sonar ou outro serviço; declarar e testar no adaptador correspondente.

## Escrita protegida

Resolver raiz e destinos canonicamente; recusar arquivo no lugar de apps, travessia e links fora da raiz. Preparar conjunto de arquivos e checar conflitos antes da escrita. Para consumidor existente, gerar plano de diferenças/candidato; não resetar arquivo real. Fazer somente adição idempotente da regra de ignore, preservando linhas do usuário. Destinos já autorados exigem operação explícita de atualização com política própria.

### Protocolo único de escrita

init, nova-change, escrita de gate e geração autorizada compartilham lock exclusivo em .specflow/write.lock, criado de forma exclusiva. É permitido criar somente os diretórios/registro de controle necessários à reserva antes do preflight. Lock ocupado retorna 1/PROJECT_BUSY sem esperar indefinidamente; não expirar/apagar lock alheio por tempo ou por --force. Encerramento normal remove apenas o lock da própria operação. Recuperação de lock abandonado é ação explícita do operador, após conferir que não há escritor ativo; o CLI v1 só diagnostica.

Sob lock, ler baseline e planejar todos os destinos; validar conflitos antes de escrever conteúdo. Novos arquivos usam criação exclusiva. Metadados gerenciados e append autorizado do ignore usam temporário na mesma pasta e os.replace, após conferir novamente hash/identidade do arquivo original. Atualizar somente propriedade gerenciada; configuração, aplicações e instruções autorais ficam byte a byte preservadas. Permitir união aditiva de integrações e novas entradas do manifesto da mesma versão; arquivo gerenciado divergente continua bloqueante.

Rollback restaura arquivo gerenciado/ignore anterior somente se seus bytes ainda coincidirem com o que esta operação escreveu; remove arquivo novo somente se ainda tiver os bytes criados por ela. Modificação concorrente impede rollback destrutivo e produz WRITE_PARTIAL explícito; nunca apagar conteúdo de terceiro para fingir transação atômica. O lock coordena ferramentas conformes, não autentica o usuário nem bloqueia um editor externo. Essa limitação precisa constar no diagnóstico/roteiro.

### Portabilidade e links

IDs de aplicação: [a-z][a-z0-9-]{0,62}. Referências de arquivos usam /, sem drive, UNC, backslash, segmentos vazios, . ou ..; recusar componentes reservados CON/PRN/AUX/NUL/COM1..9/LPT1..9 mesmo com extensão, nomes terminados em ponto/espaço e duplicatas por casefold em qualquer plataforma. A própria pasta de controle .specflow é permitida. Não normalizar texto de evidência/Unicode para alterar seu digest. Validar links/junctions de cada destino gerenciado e rejeitar links mesmo que resolvam dentro da raiz; trocar metadados por os.replace, nunca truncar arquivo que possa compartilhar inode via hardlink. Escrita por descritor/criação exclusiva e revalidação reduzem corridas; não prometer proteção contra um processo malicioso que controla a raiz inteira.

### Leitura de configuração

Implementar a gramática descrita em INIT-07; não usar ConfigParser nem java.util.Properties com semântica diferente. Catálogo determina tipos/obrigatoriedade e campos dispensáveis. URL e número podem ter validação específica; credencial literal não recebe trim/casefold. Marcadores são comparados em cópia normalizada, nunca enviados a serviço. Arquivo inválido desativa execução até correção; arquivo válido com recurso incompleto não afeta outros recursos independentes.

## Testes futuros

Fixtures com hooks de rede/processo que falham se chamados em init/recursos DEFINIR; casos de config parcial, autenticação opcional, formato inválido, recursos independentes, reinit sem sobrescrita, apps preexistente, caminho/link malicioso e SPEC ausente. Evidência de cobertura e dois consumidores isolados; não utilizar credenciais reais ou serviços de produção. Testes de disponibilidade de infraestrutura não substituem teste negativo de não utilização.
