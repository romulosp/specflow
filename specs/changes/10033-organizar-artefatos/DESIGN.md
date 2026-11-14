# Design: 10033-organizar-artefatos

## Estrutura proposta por Change
```text
<change>/
  proposal.md  spec.md  DESIGN.md  tasks.md
  reviews/spec/             # revisoes da SPEC: texto e JSON
  reviews/implementation/   # revisoes da implementacao: texto e JSON
  decisions/spec/           # decisao humana sobre a SPEC
  decisions/final/          # aceite humano final
  coverage/                # registros e relatorios de cobertura
  evidence/                # provas por finalidade
```
Diretorios sao criados quando necessarios. Decisoes humanas sao distintas de pareceres e ADRs. Arquivos contratuais permanecem na raiz.

## Compatibilidade
Novos produtores usam os destinos acima; leitores seguem referencias explicitas e reconhecem registros legados. Inventariar formatos e regras reais antes da implementacao; ambiguidade ou conflito bloqueia com diagnostico. Sem migracao automatica, reemissao de decisao ou alteracao de manifests antigos. Testar fixtures isoladas e referencias legadas, sem alterar acervo. Caminhos sao relativos e confinados; validar hashes.

## Alternativas e versao
Agrupar revisoes por fase mantem parecer e JSON juntos. Migrar historico exigiria nova autorizacao. O uv ja aceita `uv tool install specflow-cli`, `uv tool install "specflow-cli==0.1.0"` e `uv tool upgrade specflow-cli`. Restricoes fixadas persistem no upgrade; para muda-las, reinstalar com a especificacao desejada. Verificar em ambiente isolado, sem instalar no perfil pessoal. Fontes: https://docs.astral.sh/uv/concepts/tools/ e https://github.com/github/spec-kit.
