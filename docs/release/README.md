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

## Evidencia atual

Os quatro jobs Windows/Linux e Python3.11/3.14 passaram no [run43603359955](https://github.com/romulosp/specflow/actions/runs/43603359955), commit f564677d61c0638cee6cfcba539294fc11a6a02d. Ambiente pypi criado com reviewer romulosp e sem bypass administrativo; tags v* protegidas contra atualizacao/exclusao pelo ruleset27264923. Usuario informou conta PyPI criada; verificacao de email/2FA e cadastro do publisher ainda precisam ser confirmados. Sem upload ou instalacao nominal confirmada.

## Resultado da publicacao

[PyPI 0.1.0](https://pypi.org/project/specflow-cli/0.1.0/) confirmado. Run43604099173 aprovado pelo titular e concluido com sucesso. Wheel/sdist no indice tem os mesmos SHA-256 do artifact14117059756, conferido com digest do ZIP. Quinze operacoes locais de instalacao pelo indice/CLI passaram sem dist, indice privado ou cache anterior; nenhuma instalacao global pessoal. Registros em pypi-installation-smoke.json e ../../specs/changes/10032-publicar-specflow-cli-pypi/pypi-verification.json. Trechos anteriores sobre configuracao/preparacao sao o roteiro historico reutilizavel. A publicacao nao declara teste humano do produto ou descoberta nos clientes concluidos.
