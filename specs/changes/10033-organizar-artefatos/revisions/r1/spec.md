# SPEC: 10033-organizar-artefatos

## Status
EM_REVISAO_SPEC ? r1. Nenhuma aprova??o humana registrada.

## Refer?ncias e depend?ncias
Pol?ticas vigentes de workflow e cobertura; formatos e refer?ncias implementados em framework; Changes 10029?10032 preservadas. README de refer?ncia: https://github.com/github/spec-kit.

## Requisitos funcionais
- RF01: Em cada nova Change, organizar revis?es em `reviews/spec/` e `reviews/implementation/`; colocar Markdown e JSON da mesma revis?o no diret?rio do tipo correspondente. `reviews/` n?o ? pasta exclusiva de JSON.
- RF02: Usar `decisions/` para registros de decis?es humanas, por exemplo `decisions/spec/` e `decisions/final/`, mantendo tipo, origem, escopo e v?nculos verific?veis; decis?es arquiteturais de projeto continuam no local pr?prio de ADR.
- RF03: Guardar relat?rios e registros de cobertura em `coverage/` e demais provas em `evidence/`, agrupadas por finalidade quando necess?rio. Um artefato pertence a uma ?nica categoria; refer?ncias apontam para seu local real.
- RF04: Identificar e atualizar todos os produtores, consumidores, templates, instru??es empacotadas e documenta??o afetados para a estrutura definida, sem gerar diret?rios desnecess?rios antecipadamente.
- RF05: Continuar lendo Changes e registros legados nos caminhos originais, inclusive refer?ncias e manifests v?lidos. N?o mover, reescrever ou invalidar bytes hist?ricos automaticamente. Conflitos entre registros legados e novos devem ser detectados e relatados, sem sele??o silenciosa.
- RF06: Preservar arquivos existentes e detectar colis?es; n?o sobrescrever conte?do nem executar comandos contidos em JSON. Os gates e decis?es humanas mant?m a sem?ntica atual.
- RF07: Documentar ?rvore, prop?sito, exemplos e compatibilidade, distinguindo estrutura planejada do comportamento j? lan?ado.

## Requisitos n?o funcionais
- RNF01: Testes de comportamento executados e cobertura medida m?nima de 80% por arquivo execut?vel alterado e agregado, meta 90%, com invent?rio arquivo?teste?crit?rio e relat?rios atuais.
- RNF02: Caminhos permanecem confinados ao projeto; v?nculos e hashes s?o validados segundo os contratos vigentes. O lock continua cooperativo.

## Cen?rios e crit?rios de aceite
- CA01 (RF01?04): Ao gerar cada tipo de artefato em uma Change nova, ele aparece na categoria correta e os leitores localizam suas refer?ncias reais.
- CA02 (RF05): Uma Change legada com registros v?lidos continua verific?vel sem altera??o dos arquivos e sem tratar registro hist?rico como aprova??o de outra revis?o.
- CA03 (RF05?06): Colis?o ou registros contradit?rios produzem erro identific?vel e preservam os bytes anteriores.
- CA04 (RF06): Caminhos externos, refer?ncias inv?lidas e comandos em JSON n?o levam a escrita externa nem execu??o de conte?do; gates permanecem bloqueantes quando faltam evid?ncias.
- CA05 (RNF01): Su?te e relat?rio reais demonstram cobertura por arquivo e agregado, com falhas e limites testados.
- CA06 (RF07): Documenta??o mostra estrutura e limites reais e n?o promete compatibilidade de cliente n?o comprovada.
