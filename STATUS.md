# Estado do projeto SpecFlow

Resultado corrente dos ajustes: 52 checks documentais, 36 do dossiê e 10 testes sintéticos de suporte aprovados, sem falhas. [Evidência](docs/cli/verificacao-ajustes-2026-11-13.json). Escolhas técnicas resolvidas; somente aprovação das SPECs corrigidas pendente antes de código, sem aceite fabricado.

Marco corrente: ajustes técnicos delegados pelo usuário e aplicados aos contratos 10029 r6, 10030 r4 e 10031 r2. [Sete correções e solução escolhida](docs/cli/AJUSTES-TECNICOS.md). Não aguardar detalhamento técnico do usuário. SPECs corrigidas em revisão; sem aprovação humana ou implementação do produto. Entradas anteriores são históricas.


Resposta humana anterior: "Quero corrigir os contratos antes de aprovar". Depois o usuário delegou os ajustes técnicos, agora tratados; aprovação dos novos contratos permanece pendente, sem aguardar detalhamento. Nenhuma implementação autorizada pelos gates atuais. Fonte em docs/cli/feedback-humano-2026-11-13.json.

Data: 2026-11-13. Processo Spec Driven próprio.

Conferência do marco CLI: 55 checks documentais, 36 do dossiê e 10 testes sintéticos de suporte aprovados, sem falhas. Pacote de decisão em docs/cli/DECISAO-SPEC.md; aguardando resposta humana, sem código/wheel implementado.

Marco corrente: limpeza documental solicitada concluída; contratos 10029 r6, 10030 r4 e nova Change 10031 r2 preparados. CLI + agente no editor e nome specflow-cli/specflow já escolhidos pelo usuário. Originais preservados em arquivo externo verificado. SPEC_APROVADA dos novos contratos, código, pacote, instalação e homologação permanecem pendentes. Guia/diagrama em docs/cli/README.md; não declarar os resultados históricos abaixo como execução do CLI.

Correções e decisões correntes em [PENDENCIAS](PENDENCIAS.md). Contratos 10029 r6 e 10030 r4 reconciliados documentalmente, sem aprovação humana. Três links de skills corrigidos, 146 referências ainda ausentes em 30 diretórios de skills opcionais, com operações dependentes limitadas. Gerador PDF executado e inspecionado com exemplo sintético de uma página; não é auditoria real do produto.

Conferência desta rodada: 36 checks do dossiê, 36 checks de reconciliação e 10 testes sintéticos do gate de segurança aprovados, sem falhas. Evidência em docs/revisao-pendencias-2026-11-13.json. Testes do núcleo, cobertura, auditoria real e homologação dos clientes continuam pendentes.

- Investigação 10028: resultados históricos validados; representações editoriais atuais não herdam aprovação dos bytes originais.
- Núcleo 10029: EM_REVISAO_SPEC, contrato r6; implementação não iniciada.
- Inicialização/configuração/apps 10030: EM_REVISAO_SPEC r4; contratos preparados, nenhum init ou gerador implementado.
- CLI 10031: EM_REVISAO_SPEC r2; proposta, SPEC, design, tarefas, guia e diagrama preparados; pacote não implementado.
- Suporte local: 360 recursos com proveniência; gerador de auditoria e ADRs incluídos, com originais preservados fora da árvore de distribuição.
- Onze comandos autorais specflow-* e alias speckflow-teste-humano criados como Skills/prompts: 24 arquivos e 104 Skills locais no total. O composto entrega resultado testável em IMPLEMENTADA e aguarda o usuário. Fases não executadas por sua criação.
- specflow-validar exige skill security-audit e script de gate; pendência/achado de segurança impede VALIDADA e avanço para aprovação.
- specflow-validar é padrão ao chegar à validação da implementação; omissão só por prompt explícito, registrada como não execução, sem liberar aprovação/encerramento. Limite de teste-humano preservado.
- Testes e cobertura medidos durante implementação: piso 80%, meta 90%, permitindo valores superiores; sem evidência atual suficiente, não concluir IMPLEMENTADA nem aprovar IMPLEMENTACAO_APROVADA.
- Quarenta regras consolidadas em specs/shared/process/regras-consolidadas.md, com fontes/tipos e propostas pendentes separados. Configuração futura sempre começa em DEFINIR, recursos sem dados não executam; aplicações geradas ficam em apps/ do consumidor.
- Copyright Rômulo Penha/MIT autoral definidos; terceiros preservam seus avisos. Nenhuma publicação realizada.

Autorização de importação não equivale a SPEC_APROVADA do núcleo, aceite final, commit, archive ou publicação. Este arquivo descreve apenas este projeto; não reproduz o estado do Protótipo.
