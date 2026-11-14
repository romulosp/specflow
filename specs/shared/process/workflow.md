# Workflow SpecFlow

Sete fases: especificar, revisar SPEC, implementar, revisar implementacao, validar, aprovar e encerrar.
Esclarecer e planejar sao auxiliares. Contexto e retomada; RASCUNHO e anterior as fases, sem aprovacao.
Aprovacao humana corrente precede plano/codigo; testes verdes nao aprovam contrato ou build.
Na implementacao, testes reais e piso 80% por arquivo/agregado, meta 90%, sem teto.
validar e padrao na fase de validacao; so prompt explicito permite not_run, nunca VALIDADA por dispensa.
Analise de seguranca e gate sao obrigatorios. Qualquer achado aberto ou evidencia antiga bloqueia.
Confirme hashes de testes, logs e relatorios. Codigo 0 isolado do gate nao atesta verdade ou autenticidade.
Teste humano deve identificar build/revisao e resultado observado. Encerrar/publicar exige autorizacao aplicavel.
Leia [cobertura](../testing/coverage-policy.md) e [evidencias](evidence-conventions.md).
