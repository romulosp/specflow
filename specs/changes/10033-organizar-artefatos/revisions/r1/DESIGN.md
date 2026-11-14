# Design: 10033-organizar-artefatos

## Contexto
Os registros t?m refer?ncias e hashes; mover arquivos existentes pode invalidar evid?ncias e decis?es. A distribui??o 0.1.0 ? imut?vel.

## Estrutura proposta por Change
```text
<change>/
  proposal.md  spec.md  DESIGN.md  tasks.md
  reviews/
    spec/             # revis?es da SPEC, texto e JSON
    implementation/   # revis?es da implementa??o, texto e JSON
  decisions/
    spec/             # decis?o humana sobre a revis?o contratual
    final/            # aceite humano final
  coverage/           # registros e relat?rios de cobertura
  evidence/           # evid?ncias de testes, seguran?a e outras, por finalidade
```
Pastas s?o criadas quando necess?rias. `decisions` ? termo gen?rico e distingue decis?es humanas de revis?es t?cnicas; ADRs n?o s?o transferidos. Arquivos contratuais permanecem na raiz. Nomes concretos e subpastas adicionais devem evitar colis?o e identificar revis?o ou finalidade.

## Compatibilidade e decis?es
Novos produtores escrevem nos destinos acima; consumidores respeitam refer?ncias expl?citas e reconhecem registros legados. Inventariar os formatos e regras reais antes de adaptar; se houver ambiguidade ou duplica??o conflitante, bloquear e apresentar diagn?stico. Sem migra??o autom?tica, links artificiais ou altera??o de manifests antigos. Testar arquivos legados reais e fixtures isoladas, sem modificar o acervo. As refer?ncias continuam relativas e confinadas, com hashes verificados.

## Alternativas e consequ?ncias
Agrupar por formato em `reviews/json` separaria o JSON de seu parecer, dificultando revis?o conjunta; opta-se por agrupar por fase. Migrar todo o hist?rico quebraria v?nculos ou exigiria reemitir decis?es; fica fora deste escopo. Implementa??o e nova distribui??o dependem de SPEC aprovada e gates aplic?veis.
