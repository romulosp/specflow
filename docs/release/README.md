# Publicação do SpecFlow CLI

Estado: SPEC 10032 r1 aprovada; distribuição pública ainda pendente de execução e acesso ao PyPI. Não anunciar instalação nominal como disponível antes da confirmação do índice.

Destino autorizado: `specflow-cli` no PyPI; repositório `romulosp/specflow`. Conta e segundo fator pertencem ao titular. Nenhuma senha ou token deve entrar no chat, fonte ou logs.

Cadastre o publisher pendente em https://pypi.org/manage/account/publishing/:

| Campo | Valor |
| --- | --- |
| PyPI project name | specflow-cli |
| Owner | romulosp |
| Repository | specflow |
| Workflow | publish-pypi.yml |
| Environment | pypi |

Crie o environment `pypi` no GitHub, exigindo revisão humana antes do job de upload e restringindo a tag de release. Não disparar publicação antes de confirmar essas proteções e o publisher. Não há segredo persistente: o job usa OIDC, conforme [documentação oficial](https://docs.pypi.org/trusted-publishers/using-a-publisher/).

`ci.yml` testa quatro combinações de sistema/Python, mede cobertura por arquivo/agregado, constrói wheel a partir do sdist e executa um smoke isolado. `publish-pypi.yml` é manual em tag `v<versão>`, repete o CI, exige auditoria atual, recusa versão já existente e seleciona os dois artefatos daquela execução. O job de upload tem somente as permissões necessárias e aguarda o ambiente protegido.

Antes do upload: conferir source allowlist, revisão, relatório de segurança, gate atual e os quatro jobs verdes. Nunca enviar acervo, configuração real, ambientes, backups ou saídas históricas. Nunca reconstruir uma versão já publicada para substituir seus bytes.

Depois do upload, comparar os SHA-256 retornados pelo PyPI com os artefatos da execução e testar em instalação limpa, sem dist local ou índice alternativo:

```powershell
uv tool install specflow-cli
specflow --version
specflow init meu-projeto --integration copilot --integration codex
cd meu-projeto
specflow doctor
specflow nova-change "Criar cadastro de clientes"
```

Esse bloco é o aceite a demonstrar, ainda não uma publicação realizada. A versão inicial é experimental; descoberta nos clientes e teste humano mantêm seu estado real enquanto não executados. A autorização de publicar não fabrica aceite final das Changes anteriores.
