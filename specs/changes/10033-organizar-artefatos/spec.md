# SPEC: 10033-organizar-artefatos

## Status
EM_REVISAO_SPEC - r2. Sem aprovacao humana da revisao.

## Requisitos
- RF01: Organizar revisoes de SPEC em `reviews/spec/` e de implementacao em `reviews/implementation/`, mantendo texto e JSON relacionados juntos.
- RF02: Registrar decisoes humanas em `decisions/spec/` e `decisions/final/`, preservando tipo, origem, escopo e vinculos; ADRs continuam em seu local proprio.
- RF03: Guardar registros e relatorios de cobertura em `coverage/` e demais provas em `evidence/`, agrupadas por finalidade. Referencias apontam para os locais reais.
- RF04: Adaptar produtores, consumidores, templates, instrucoes empacotadas e documentacao afetados; criar diretorios somente quando necessarios.
- RF05: Ler referencias e manifests legados nos caminhos originais, sem mover ou reescrever automaticamente arquivos historicos. Conflitos entre registros legados e novos devem produzir diagnostico, sem escolha silenciosa.
- RF06: Preservar arquivos existentes, detectar colisoes e impedir execucao de comandos contidos em JSON. Gates e decisoes humanas mantem a semantica atual.
- RF07: Documentar a arvore, exemplos, compatibilidade e estado real, sem prometer recursos nao comprovados.
- RF08: Documentar instalacao pelo uv sem versao e com versao exata, atualizacao, restricoes persistentes e verificacao com `specflow --version`; nao prometer migracao automatica dos consumidores.
- RF09: Resolver registros por referencias explicitas e distinguir ausencia de conflito; nao depender de ordem de listagem.
- RF10: Definir nomes previsiveis por tipo e revisao e comportamento idempotente sem sobrescrita.

## Requisitos nao funcionais
- RNF01: Testes de comportamento executados e cobertura medida minima de 80% por arquivo executavel alterado e agregado, meta 90%, com inventario arquivo-teste-criterio e relatorios atuais.
- RNF02: Confinar caminhos ao projeto e validar vinculos e hashes; lock permanece cooperativo.

## Criterios de aceite
- CA01 (RF01-04): Artefatos novos sao gravados nos diretorios definidos e encontrados pelas referencias reais.
- CA02 (RF05): Change legada valida continua verificavel sem alteracao de seus arquivos ou aprovacao herdada para outra revisao.
- CA03 (RF05-06): Colisao ou conflito produz erro identificavel e preserva bytes anteriores.
- CA04 (RF06, RNF02): Caminhos externos e JSON com comandos nao causam escrita externa ou execucao; provas ausentes bloqueiam gates.
- CA05 (RNF01): Suite e relatorios reais demonstram cobertura por arquivo e agregado; falhas e limites sao testados.
- CA06 (RF07): Documentacao descreve estrutura entregue e limites reais.
- CA07 (RF08): Em ambiente isolado, registrar versoes observadas e resultados da instalacao padrao, versao exata, atualizacao e versao inexistente; documentar comportamento real e restricoes do uv.
- CA08 (RF09-10): Ausencia e conflito tem diagnosticos distintos; repeticao nao sobrescreve registros nem cria duplicatas indevidas.
