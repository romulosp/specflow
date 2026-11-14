# Proposta - Publicar SpecFlow CLI no PyPI

Revisao r1, 14/11/2026. EM_REVISAO_SPEC.

Objetivo: permitir uv tool install specflow-cli seguido de specflow init meu-projeto --integration copilot --integration codex, sem wheel local. O usuario autorizou executar todo o trabalho necessario a essa distribuicao. A autorizacao de publicacao nao e inferida como aprovacao de um contrato ainda nao apresentado.

Repositorio identificado: https://github.com/romulosp/specflow.git. HEAD local d03e0c5 contem somente README.md; framework e demais recursos aparecem untracked. Consulta https://pypi.org/pypi/specflow-cli/json em 14/11/2026 retornou 404; isso nao reserva ou garante a disponibilidade do nome.

Escopo: preparar fonte autoral distribuivel, metadados publicos e guias, CI Windows/Linux, verificacao do pacote, publicacao autenticada e teste de instalacao real pelo indice. Publicacao autorizada como objetivo, condicionada a SPEC vigente, controles de qualidade e acesso legitimo as contas.

Alternativas: wheel local (nao atende experiencia desejada), URL Git (exige URL e fonte versionada), PyPI (recomendado, atende comando exato). Escolha: PyPI por GitHub Actions/OIDC. Nao publicar o acervo historico ou componentes com direitos desconhecidos.

Exclusoes: migracao de consumidores, integracoes operacionais de servicos, alteracao de checkout externo, mudanca de nome sem decisao humana, simulacao de descoberta nos editores, aprovacao final ficticia ou sobrescrita de versao publicada.
