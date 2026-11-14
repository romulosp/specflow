# Gate obrigatório de segurança em specflow-validar

`specflow-validar` é executado por padrão quando o fluxo autorizado chega à fase de validação da implementação. Só um pedido explícito do prompt do usuário para não executar a fase, ou um limite de parada anterior, permite omiti-la. Registrar solicitação, motivo e revisão como fase não executada, sem VALIDADA/aprovação. Se a fase for executada, todos os requisitos abaixo continuam obrigatórios; omitir a fase não é obter um resultado favorável do gate. Falha ou ferramenta ausente não autoriza dispensa silenciosa.

1. A skill local `security-audit` analisa a implementação atual e executa os checks aplicáveis no escopo autorizado. Registra evidências redigidas, achados e limitações reais.
2. O resultado estruturado fica em `<Change>/security-audit.json`.
3. Execute na raiz: `python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>`.
4. O script grava `<Change>/security-gate.json`. Código 0 / `verificada` satisfaz apenas este gate; códigos 1 ou 2 deixam `pendente`, `validationAllowed=false` e impedem VALIDADA/aprovação.

**Qualquer achado aberto bloqueia**, inclusive low/info. Também bloqueiam auditoria ausente/incompleta, checks falhos/não executados, manifesto desatualizado, evidências ausentes, falha de leitura ou erro do verificador. A fase continua na sua entrada técnica, com pendência explícita de segurança em `validation.md`; não inventar um novo estado terminal ou marcar VALIDADA com ressalva. Correções retornam à implementação; após revisão técnica atual, repetir auditoria e gate.

## Contrato de entrada v1

Use [auditoria-template.json](auditoria-template.json) como estrutura inicial; ele começa pendente e não pode liberar o gate. Não copiar um resultado favorável de exemplo ou de outra Change.

| Campo | Regra |
| --- | --- |
| schemaVersion | Inteiro 1; bool não é inteiro válido |
| changeId | Nome exato da pasta da Change |
| revision | Revisão/build realmente analisado, reconciliado pelo responsável com a implementação revisada |
| review | skill=security-audit, reviewer identificado, status=completed ou pending e limitations como lista de textos |
| scope | Lista não vazia de arquivos relativos à raiz do projeto, selecionados pela análise do diff/escopo real |
| artifacts | Um item por arquivo do scope: path, digestProfile e sha256; cobertura exata e sem duplicatas |
| findings | Lista de id, severity (critical/high/medium/low/info), status (open/resolved), evidenceRefs; resolvido exige evidência de correção/reteste |
| checks | Lista não vazia de id, method (static/automated/manual), expectedCode, actualCode (inteiro ou null), outcome (passed/failed/not_run), evidenceRefs |

Paths e evidenceRefs são arquivos locais existentes, relativos à raiz. Não aceitar caminho absoluto, `..`, links fora da raiz ou argumentos executáveis. Perfis: `sha256-bytes-v1` nos bytes exatos ou `sha256-utf8-lf-v1` em UTF-8 estrito, BOM inicial opcional e CRLF/CR normalizados para LF, sem trim. Perfil é obrigatório. Não incluir os próprios relatórios/gates no manifesto que os descreve, evitando circularidade.

Checks só passam com outcome=passed, código real igual ao esperado e referências de evidência presentes. Findings resolvidos exigem evidência; qualquer open permanece bloqueante. Campos ou tipos malformados retornam 2; conteúdo válido porém pendente/violado retorna 1. Nem 0 promove APROVADA ou executa aceite humano.

## Limites explícitos

**Helper histórico e produto implementado:** o código 0 deste helper v1 não vincula os bytes de todos os logs/testes/evidenceRefs citados. O núcleo/CLI em `framework/` implementa evidenceManifest, testManifest, vínculos atuais e escrita por lock/temporário/replace com recusa de links, conforme 10029 r6 / 10031 r2 aprovadas. O CLI nativo usa sua rotina empacotada; não executa a cópia do consumidor. Este helper histórico permanece inalterado e seus testes antigos não demonstram os endurecimentos novos. Consulte [a entrega atual](../cli/ENTREGA-0.1.0.md) e os bindings/evidências das Changes.

O script **verifica o gate de evidências**, não substitui o trabalho da skill ou executa scanner por conta própria. Não executa comandos contidos no JSON, não descobre sozinho todo o diff, não autentica reviewer nem comprova a veracidade dos arquivos de evidência. Esses limites não dispensam a análise real de segurança: o agente deve conferir escopo, justificativas, comandos e resultados antes de usar o gate. Alterar apenas um status para resolved não é correção.

O `gerar_relatorio.py` formata PDF de dados declarados e **não libera o gate de segurança**. PDF é opcional; auditoria e gate são obrigatórios em `specflow-validar`. Ausência de ferramenta essencial é pendência, não aprovação por fallback silencioso.

`specflow-teste-humano` para antes da validação formal. Ele faz checks de implementação, entrega para o usuário testar e não chama specflow-validar implicitamente. Quando a validação formal for solicitada, este gate se aplica integralmente.
