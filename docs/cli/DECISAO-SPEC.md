# Contratos concretos para decisão humana

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Historico anterior a este marco

13/11/2026. Processo Spec Driven próprio. Aprovação humana pendente. Após pedir correções, o usuário delegou a escolha técnica: “veja o melhor projeto e resolva”. [Delegação registrada](delegacao-tecnica-2026-11-13.json); [sete tratamentos aplicados](AJUSTES-TECNICOS.md). Não é mais necessário indicar detalhes técnicos. Este pacote não registra aprovação.

O usuário pediu implementar o plano. O próprio plano determina: revisão e aprovação humana das SPECs correspondentes antes da implementação. Os contratos abaixo foram materializados depois desse pedido, portanto não há aprovação retroativa de seus hashes. Nome, estratégia CLI + agente no editor e instalação local já foram escolhidos e não precisam ser decididos outra vez.

| Contrato | Escopo da decisão | Manifesto exato |
| --- | --- | --- |
| [10029 r6](../../specs/changes/10029-criar-nucleo-specflow/spec.md) | Diagnóstico com seus limites, núcleo/memória, contexto de rascunho e evidências vinculadas | [Quatro documentos r6](../../specs/changes/10029-criar-nucleo-specflow/evidence/contract-r6.json) |
| [10030 r4](../../specs/changes/10030-inicializar-consumidor-configuracao/spec.md) | Configuração literal/DEFINIR, escrita protegida/portátil e integrações aditivas | [Quatro documentos r4](../../specs/changes/10030-inicializar-consumidor-configuracao/evidence/contract-r4.json) |
| [10031 r2](../../specs/changes/10031-criar-specflow-cli/spec.md) | CLI fino, doctor/contexto utilizáveis, empacotamento e validação com vínculos atuais | [Quatro documentos r2](../../specs/changes/10031-criar-specflow-cli/evidence/contract-r2.json) |

Recomendação: aprovar os contratos se os limites e critérios estiverem de acordo; ou indicar correções materiais por Change/requisito. Consequência da aprovação: liberar planos preparatórios e implementação na ordem núcleo → consumidor → CLI, com os respectivos testes, cobertura, revisão, validação e entrega humana. Uma aprovação não supre a de outro contrato.

A decisão pode abranger o conjunto ou cada Change separadamente. Uma resposta explícita possível é: “Aceito o diagnóstico com seus limites e aprovo como SPEC_APROVADA os contratos 10029 r6, 10030 r4 e 10031 r2 apresentados neste pacote.” Esta frase é apenas sugestão para a resposta humana, não aprovação existente.

Aceite final do produto, encerramento efetivo e publicação permanecem separados. Nenhuma instalação no ambiente pessoal, escrita no checkout de origem ou extração definitiva é autorizada por consequência.
