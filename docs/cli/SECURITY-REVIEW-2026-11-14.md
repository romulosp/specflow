# Auditoria local de segurança — build 0.1.0

14/11/2026. Executor: assistente desta sessão, aplicando a skill local security-audit. Revisão do próprio executor, sem auditor independente. Escopo: código Python novo, recursos autorais distribuídos, testes e metadados de empacotamento em `framework/`; manifests por Change identificam bytes exatos. Não inclui certificação dos helpers históricos ou serviços externos.

## Análise realizada

| Superfície | Evidência e conclusão |
| --- | --- |
| Entrada JSON | `storage.decode_json`, `fields` e `contracts`: UTF-8 estrito, duplicatas/NaN rejeitados, tipos/enums fechados, bool não aceito como inteiro. Testes negativos reais em test_core; nenhuma instrução de evidência é executada |
| Integridade e escopo | `storage.verify/bind`, `workflow.decision/implementation_target`, `validation`: perfil/caminho/papel/hash atual; decisões com projectId/changeId/revision; alterações em contrato, teste, log, cobertura e relatório invalidam os vínculos. Política empacotada fixada por digest |
| Caminhos e escrita | `storage.portable/confined/link` e `fileops.Transaction`: travessia, nomes Windows não portáteis, reparse points e links de escrita bloqueados; preflight, lock cooperativo, replace e rollback que preserva edição concorrente. Testes reais de junction/hardlink passaram; criação de symlink requer permissão ausente no ambiente |
| Segredos e configuração | `configuration.parse/resolve`, `cli.SafeParser` e diagnósticos por ID/caminho relativo: sem interpolação ou echo de valores, argumentos inválidos redigidos, placeholders não ativam recursos. `.gitignore` preservado e configuracao.properties fora dos hashes de ownership. Ignore não remove segredos já rastreados |
| Execução externa | Varredura AST do runtime: única chamada de subprocesso em `assets/gate_wrapper.py`, com lista fixa, shell=False e CLI instalado resolvido por PATH. É entrada de script explícita; o CLI nativo usa sua biblioteca confiável e não executa a cópia do consumidor. Nenhum comando vindo do JSON é executado |
| Distribuição | Wheel/sdist inspecionados, sem dependências de runtime, material do acervo de direitos desconhecidos, caches ou identidades removidas. Busca por padrões conhecidos de chave privada/tokens não encontrou ocorrência no pacote. Inventário/hashes e recursos gerados conferidos |
| Isolamento | Dois consumidores temporários, snapshots de operações de leitura, nenhum índice global; init/doctor com todos os placeholders e parciais exercitados com tentativas externas proibidas pelos testes |
| Aprovações | Não há autenticação criptográfica do ator ou prova automática de veracidade de um relatório. Fonte humana é conferida pelo operador. CLI não cria decisão, commit, publicação ou archive |

Autenticação HTTP, sessão, multi-tenant, IDOR de API, XSS de página, SQL e deploy: **não aplicáveis ao runtime CLI local**, que não expõe servidor, banco ou página de aplicação. Os perfis none/basic/token apenas validam configuração, sem conectar a serviços. Histórico Git: não disponível neste workspace; nenhuma conclusão sobre segredos de histórico externo.

## Resultado e limites

Nenhuma vulnerabilidade confirmada aberta no escopo analisado. Testes, inventário e revisão sustentam essa conclusão limitada; ausência de achados não comprova segurança universal. Referências em `security-audit.json` apontam para resultados realmente executados e hashes atuais. O helper local obrigatório é executado separadamente para cada Change; o código 0 não autentica auditor, comprova a verdade do relato ou aprova a Change.

O modelo de ameaça presume instalação/PATH e permissões do usuário confiáveis. O lock coordena processos conformes e não protege contra administrador ou processo hostil que troca diretórios durante a operação. Não há sandbox de execução, assinatura de aprovador ou criptografia automática de configuracao.properties. Preserve permissões locais e confira a instalação antes de executar o wrapper.

Próximas verificações: Linux real, descoberta dos comandos nos dois clientes e teste humano do build. São pendências de homologação, sem alegação de aprovação final. O PDF opcional não foi solicitado nem usado como prova de segurança.
