# Validacao corrente - 14/11/2026

PUB-02/03/04: fonte allowlisted, bytes git identicos ao disco, quatro jobs reais verdes e instalacao limpa; ver remote-ci.json, git-allowlist.json e docs/release/local-checks.json. PUB-07: analise e gate local0; nao prova publisher ainda nao configurado.

PUB-05/06 parciais: ambiente/regras GitHub aplicados; PyPI e dispatch pendentes. PUB-01/09/10/11: indice retorna404; sem upload/install nominal e sem anuncio de disponibilidade. PUB-08: Windows/Linux 3.11/3.14 agora exercitados em CI; clientes/teste humano continuam pendentes. Gate global da publicacao pendente, sem aceite final.

## Historico

# Validacao - Publicacao

14/11/2026. Preparacao documental, sem upload ou implementacao do workflow. Consulta PyPI JSON retornou404; nao comprova reserva do nome. Remoto local identificado, HEAD local somente README.md.

PUB-01..12: pendentes de execucao; rastreabilidade no contrato e tarefas T01..T08. Validar install nominal sem dist, CI multiplataforma, cobertura, pacote, licencas, escopo git, seguranca, OIDC, tag/artefatos e hashes do indice. Skill security-audit e comando python -B docs/security-audit/verificar_seguranca.py --change specs/changes/10032-publicar-specflow-cli-pypi obrigatorios na fase de validacao; nenhum gate favoravel copiado.

Proposta/SPEC/design/tarefas identificados no manifesto contratual. Nao repetir testes antigos como aprovacao desta nova Change. Sem SPEC_APROVADA, sem VALIDADA ou aceite final.
