# Entrega local - 10035 r1

Estado: IMPLEMENTADA. Contrato preservado; autorizacao em decisions/spec, plano anterior ao codigo. Sem revisao formal, VALIDADA ou aceite final inferidos. Limite do pedido: ate a implementacao, com correcao e repeticao dos checks afetados.

- RF01-02/CA01: novos modelos em docs/modelagem e bundle, exemplos de dois dominios, dominio unico e demanda tecnica. Conferencia manual dos exemplos: Pedidos e dono do pedido, Estoque de saldo; contrato de reserva explicito, invariantes e aceites por dominio.
- RF03-05/CA02: catalogos e instrucoes de plano/implementacao/revisao exigem rastreabilidade e fronteiras. Exemplo GestorGeral mistura regras e recebe achado ilustrativo; ConfirmarPedido delega reserva e mantem transicao local, sendo orquestracao fina justificada. Esta conferencia nao e detector automatico de arquitetura ou homologacao de agente.
- RF06-07/CA03: consumer.py gera rascunhos a partir de modelos empacotados; documentRefs e contrato continuam com papeis existentes. Testes core continuam verificando invalidacao de hashes, sem alterar contrato legado.
- RF08/CA04: teste ConsumerTests.test_domain_drafts_preserve_existing_change_and_contract_shape verifica rascunho RASCUNHO, reinit, nova Change e preservacao de SPEC autoral/configuracao; suite inclui consumidores legados. Smoke de wheel real em evidence/smoke.json conferiu ambas integracoes, modelos, exemplos e reinit.
- CA05: 56 testes executados, 1 skip por permissao de symlink, codigo 0. Cobertura linhas total 1302/1346 (96.73%); consumer.py 154/157 (98.09%). Todos arquivos executaveis medidos acima do piso 80%.

## Inventario fonte-teste-criterio
consumer.py -> test_consumer.py, test_cli.py, test_core.py -> CA03-05. Bundle/catalogos/modelos sao dados; test_consumer e teste de catalogo instalado verificam geracao e entrega; revisao manual dos exemplos cobre CA01-02. Nao ha classificador automatico de dominio; o agente e o revisor aplicam as instrucoes.

## Comandos
PYTHONPATH=framework/src;framework/tests; COVERAGE_FILE nesta pasta coverage; `.venv-specflow/Scripts/python.exe -m coverage run --branch --source=framework/src/specflow -m unittest discover -s framework/tests -q`; exportacao coverage json. Ferramenta coverage.py 7.17.3. `uv build framework --out-dir <Change>/evidence/build`; wheel instalado com uv em tool/bin/cache isolados no workspace. `python -B tools/gerar_comandos_specflow.py --check` sem divergencias; `python -B tools/verificar_dossie.py`: 36 passou, no workspace com acervo local.

## Limites
Build local 0.2.1 nao publicado, sem commit, push ou tag. CI remoto e descoberta visual nos editores not_run. Limpeza 10034 pendente: checkout publico sem acervo ainda nao tem verificacao de dossie funcional. Artefatos da Change 10033 anteriores a esta alteracao nao atestam este novo build.
