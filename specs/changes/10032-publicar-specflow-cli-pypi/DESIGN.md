# Design - Publicacao pelo indice

Revisao r1. PROPOSTO.

Manter projeto Python em framework/; pyproject.toml ja define specflow-cli e entry point specflow.cli:main. Acrescentar URLs publicas e README de instalacao, sem mudar o parser apenas para publicar. Preferir job separado de teste/build e job de upload que recebe exatamente artefatos identificados. Nunca promover dist antigo por existencia.

Fluxo: SPEC_APROVADA -> plano -> fonte allowlisted/metadados -> testes e cobertura Windows/Linux -> build do sdist -> smoke -> revisao -> auditoria/gate -> ambiente pypi/publisher -> commit/tag testados -> dispatch manual -> PyPI -> smoke pelo nome -> entrega/aceite humano. Nao marcar tarefas futuras por configuracao presente.

Publisher a cadastrar pelo titular: projeto specflow-cli; GitHub owner romulosp; repository specflow; workflow publish-pypi.yml; environment pypi. OIDC evita segredo persistente. A configuracao do environment deve restringir origem autorizada e exigir liberacao humana disponivel no plano GitHub; se protecao nao estiver disponivel, explicitar mecanismo manual equivalente antes de liberar upload.

Autenticacao interativa/2FA e dados de conta serao tratados no navegador legitimamente autenticado, sem solicitar credenciais em texto. Nao presumir conta PyPI existente. Acesso ausente bloqueia apenas a etapa dependente; trabalho local autorizado continua apos SPEC aprovada.

Documentacao publica recomenda uv tool install specflow-cli apos disponibilidade; source subdirectory framework permite alternativa Git explicita quando versionada. A raiz historica nao e automaticamente um pacote Python ou acervo redistribuivel.

Evidencias separadas de fonte: inventario git, logs CI/run IDs, coverage JSON por ambiente, SHA256 de wheel/sdist, auditoria, resultado do upload e smoke por indice. Compatibilidade >=3.11 exercitada na matriz; plataformas fora da matriz declaradas nao verificadas.

Fontes oficiais consultadas em 14/11/2026: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/ ; https://docs.pypi.org/trusted-publishers/using-a-publisher/ ; https://docs.astral.sh/uv/guides/tools/ .
