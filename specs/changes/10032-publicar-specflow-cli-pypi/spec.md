# SPEC - Distribuicao publica SpecFlow CLI

Revisao r1. EM_REVISAO_SPEC. Nenhuma SPEC_APROVADA registrada.

| ID | Requisito e criterio de aceite verificavel |
| --- | --- |
| PUB-01 | Manter nome specflow-cli e comando specflow. Apos upload confirmado, instalar em venv/tool-dir limpo usando apenas uv tool install specflow-cli; --version e init funcionam sem dist local |
| PUB-02 | Versionar fonte necessaria por allowlist revisada: framework/src, testes, metadados, licenca e documentacao autorais, CI e dados publicos da release. Excluir configuracao.properties real, ambientes, caches, tmp, imports, acervo e backups. Conferir git diff --cached --name-only, conteudo e segredos antes de commit/push; nao usar git add . indiscriminado |
| PUB-03 | Preparar CI que execute suite/cobertura e smoke wheel/sdist em Windows/Linux e Python 3.11/3.14. Cada arquivo executavel e agregado >=80%, meta90%; testes funcionais/negativos atuais e relatorios por manifesto. Ambiente sem execucao nao conta como passed |
| PUB-04 | Construir wheel a partir de sdist, verificar metadados/README/licencas/recursos, hashes e instalacao sem dependencias de runtime. Publicar somente os artefatos novos revisados, sem glob que misture dist antigo |
| PUB-05 | Usar GitHub Actions Trusted Publishing OIDC: owner romulosp, repository specflow, workflow publish-pypi.yml, environment pypi. Configurar publisher pendente no PyPI com conta legitima do titular; exigir identidade e 2FA da plataforma sem coletar senha/token no chat. Falta de acesso permanece bloqueio explicito |
| PUB-06 | Publicacao apenas por disparo manual em tag de versao imutavel ligada ao commit testado; proteger ambiente pypi. Job de upload isolado, permissions contents:read/id-token:write apenas onde necessario; nenhum PR publica. Actions de terceiros fixadas por commit verificado |
| PUB-07 | Rodar auditoria real e gate local security-audit na revisao atual antes da publicacao; qualquer achado aberto, check insuficiente ou cobertura abaixo do piso impede upload. Revisar workflow, escopo git e artefatos alem do runtime |
| PUB-08 | Documentar pendencias legadas com exatidao: Linux so aprovado apos execucao real; descoberta Copilot/Codex e teste humano continuam pendentes enquanto nao executados. A release inicial deve declarar esse estado experimental, sem alegar aceite final dos incrementos anteriores |
| PUB-09 | Verificar versao livre no indice antes de tag/upload; usar 0.1.0 se nunca publicada e controles satisfeitos. Nao substituir arquivo/versao existente ou adotar nome alternativo automaticamente. Conflito bloqueia e exige decisao |
| PUB-10 | Apos publicacao verificar JSON/indice PyPI, nomes/versao/SHA256 iguais aos artefatos revisados. Instalar pelo nome sem cache privado/find-links/indice alternativo, executar help/version/init/doctor/nova-change/contexto e bloqueio sem SPEC. Registrar comandos/codigos/ambiente reais |
| PUB-11 | Atualizar instrucoes principais para o comando pelo nome somente com disponibilidade real confirmada, mantendo alternativa offline. Preservar contratos aprovados 10029/10030/10031 e evidencias historicas; novos hashes invalidam revisoes dependentes quando aplicavel |
| PUB-12 | Atualizar memoria, rastreabilidade e relatorio de release; testes nao fabricam aceite humano final. Falha de upload/install fica pendente. Rollback: corrigir em nova versao, sem apagar historico ou release automaticamente |

Copyright Romulo Penha/MIT para material autoral, preservando avisos necessarios. O upload publico e irreversivel quanto a divulgacao dos bytes; nao enviar material fora da allowlist. Nao alterar as SPECs aprovadas anteriores nem dispensar seus gates. A publicacao experimental nao equivale a homologacao universal ou teste humano concluido.
