# Evidencias e contratos JSON

UTF-8 estrito; schemaVersion=1; tipos/IDs/enums fechados, sem chaves duplicadas/NaN. Paths relativos com /, sem escape.
Quatro documentos: proposal.md, spec.md, DESIGN.md, tasks.md. Perfil sha256-utf8-lf-v1 remove somente BOM inicial e normaliza CRLF/CR para LF, sem trim.
Implementacao/evidencias usam sha256-bytes-v1. Manifesto e lista de path, role, digestProfile, sha256; rawSha256 auxiliar nao integra igualdade textual.
project.json fica em .specflow; Change completa tem change.json, contrato/implementacao e refs de revisoes, decisoes, evidencias, matriz, cobertura, seguranca, execucao e entrega.
Draft e convertido explicitamente pelo agente; nao manter draft.json e change.json simultaneamente.
Evidencia exige metodo structural/functional/manual igual ao requiredMethod, resultado/codigos reais e artifactManifest dos bytes citados.
Cobertura exige testManifest e artifactManifest de relatorios/logs. Seguranca exige binding do audit/gate, evidenceManifest e alvo atual; nao incluir o proprio JSON no seu manifesto.
Decisao spec/final exige ator, data com offset, scope {projectId, changeId, revision}, targetManifest, outcome approved/rejected, rationale e sourceRef humano real. Final vincula contrato + implementacao.
Nunca executar command do JSON. A ferramenta verifica consistencia e nao autentica o operador nem prova por si so a verdade das evidencias.

Registros tecnicos de implementacao usam targetManifest = contrato + implementacao; artifactManifest da entrega descreve somente o build. Resultado manual exige evidencia method=manual com criterionIds dos cenarios e hashes do relato humano/quickstart.

# Organizacao dos artefatos por Change

Guarde revisoes de SPEC em reviews/spec/review-<revisao>.md e review-<revisao>.json; revisoes da implementacao em reviews/implementation/ com os mesmos nomes. Decisoes humanas em decisions/spec/decision-<revisao>.json ou decisions/final/decision-<revisao>.json. Relatorios e registros de cobertura ficam em coverage/ e demais evidencias em evidence/<finalidade>/. Auditoria e gate de seguranca novos ficam em evidence/security/security-audit.json e evidence/security/security-gate.json. Arquivos contratuais permanecem na raiz. Crie pastas somente ao gravar. Use identificadores adicionais para evitar colisao; nunca sobrescreva arquivos diferentes nem duplique operacoes identicas. Registre referencias explicitas relativas ao projeto e seus hashes. Respeite caminhos legados ja referenciados; nao mova historico. Ausencia e conflito bloqueiam e devem ser relatados.

Se o gate anterior tiver resultado diferente, uma nova saida com hash no nome preserva o registro anterior; consulte securityGateRef na saida e atualize os vinculos de seguranca com o arquivo realmente avaliado. Auditoria referenciada pelo registro de seguranca tem prioridade; referencias conflitantes bloqueiam.
