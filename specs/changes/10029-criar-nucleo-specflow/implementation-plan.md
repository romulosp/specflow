# Plano de implementa??o ? n?cleo r6

SPEC_APROVADA: evidence/spec-approval-r6.json; hashes dos quatro documentos conferidos e mantidos. Implementa??o em framework/src/specflow; progresso separado do tasks.md aprovado.

1. Implementar storage seguro e contratos fechados: tipos/JSON estritos, paths relativos, digests e pol?tica empacotada fixada por hash.
2. Implementar valida??o de manifestos/evid?ncias/cobertura/seguran?a, workflow de sete fases e leitura de contexto com rascunho/isolamento/supersess?o.
3. Disponibilizar harness de leitura e testes com dois consumidores tempor?rios; positivos e negativos por gate, diverg?ncia de bytes e fonte/escopo.
4. Executar unittest/coverage em ambiente isolado .venv-specflow; m?nimo 80% por arquivo execut?vel e agregado, meta 90%, branch measurement e relat?rio JSON/HTML. Fixa??o das ferramentas em docs/cli/build-tools.lock.
5. Revisar implementa??o, registrar matriz requisito?teste?evid?ncia e auditoria real do c?digo local; executar o gate confi?vel. Aprova??o final/teste humano n?o ser?o simulados.

Riscos: corrida/links, entrada malformada, evid?ncia antiga e afirma??es narrativas conflitantes. Leituras sem rede/subprocesso/escrita; bytes de corpus externo n?o acessados. Autenticidade do operador fica fora do n?cleo, explicitamente limitada. Compatibilidade Linux/descoberta em clientes dependem de ambiente real, n?o de testes sint?ticos. Integra??o local ser? exercitada em Windows antes da pr?xima biblioteca; limita??es ficam pendentes sem certificar outros ambientes.
