# Instruções locais — SpecFlow

Marco autoritativo de 14/11/2026: SPEC10032r1 aprovada; publicacao autorizada e concluida. specflow-cli0.1.0 no PyPI, hashes e instalacao nominal verificados (15 operacoes). CI real Windows/Linux Python3.11/3.14 passou. Objetivo uv tool install specflow-cli atendido. Nao pedir novamente aprovacao das SPECs/publicacao. Memoria atual em specs/changes/10032-publicar-specflow-cli-pypi/AGENTS-MEMORY.md. Pendencias antigas de conta/upload/Linux sao historicas; descoberta nos clientes e aceite humano final do produto permanecem separados.

Marco posterior de 14/11/2026: o usuario autorizou todo trabalho necessario para instalacao por nome uv tool install specflow-cli, incluindo preparar a publicacao. Change ativa 10032-publicar-specflow-cli-pypi r1: proposta/SPEC/design/tarefas/manifesto e revisao documental preparados. A autorizacao de publicacao ja foi dada; nao perguntar novamente. SPEC_APROVADA deste novo contrato ainda pendente, antes de workflow/codigo. Conta/publisher PyPI ainda nao demonstrados. Nao declarar comando nominal disponivel antes do upload verificado. Contratos anteriores permanecem congelados; objetivo atual e publicacao controlada sem acervo/segredos, com CI e teste real pelo indice.

## Estado autoritativo

O usuário aprovou expressamente as SPECs **10029 r6, 10030 r4 e 10031 r2**: “aprovo as spec vamos proseguir”. Fonte em docs/cli/aprovacao-humana-2026-11-13.json, decisões tipadas em evidence/spec-approval de cada Change. Não pedir esses aceites novamente. Os quatro documentos contratuais e seus manifestos originais permanecem congelados; cabeçalhos de revisão pendente são históricos. Approval-state, task-progress, validation e memória registram a evolução sem invalidar hashes.

Implementação local em framework/, wheel/sdist em dist/. Retomada: docs/cli/ENTREGA-0.1.0.md e PENDENCIAS.md. Windows, testes/cobertura, instalação isolada, auditoria e gates locais têm evidências atuais. Linux, descoberta/invocação nos clientes e teste humano permanecem not_run. Não promover VALIDADA, APROVADA ou encerramento antes das evidências e decisões correspondentes.

## Escopo e preservação

- Trabalhe somente neste workspace. Não escreva, mova ou apague arquivos em checkouts externos. Não repita a investigação concluída.
- Nenhuma publicação, migração, extração definitiva, instalação no perfil pessoal, startup de infraestrutura, archive ou commit decorre automaticamente desta aprovação.
- Produto: Python >=3.11, runtime stdlib, uma distribuição specflow-cli/comando specflow. Terminal verifica/prepara; agente no editor executa desenvolvimento. phaseExecuted=false não conclui fase.
- Não reintroduza identidades, links ou caminhos do ambiente removido. Auditoria externa e recibo em docs/auditoria-limpeza-cli.json preservam os originais.
- Copyright Rômulo Penha/MIT para material autoral. Preserve direitos e licenças de terceiros; LICENSE-SCOPE e THIRD_PARTY_NOTICES prevalecem por componente. Recursos de direitos desconhecidos ou incompletos ficam fora do pacote.
- Acervo em imports/acervo-local-2026-11-12/manifest.json; 146 referências opcionais ausentes limitam operações dependentes. Leia dependency-resolution.json e DEPENDENCIAS-PENDENTES da extensão antes de usar. Pacote autoral não certifica todo o acervo.

## Gates

- Leia specs/shared/process/regras-consolidadas.md, workflow.md, cobertura e memória da Change. Skills e comandos locais estão em .agents/skills/ e docs/comandos/. Instruções legadas incompatíveis não enfraquecem os gates.
- SPEC_APROVADA humana vigente e plano precedem código. Contrato alterado exige nova revisão/manifesto/decisão aplicável. Não herdar aprovação para novos bytes.
- Toda implementação exige testes de comportamento codificados/executados, suíte aprovada e cobertura atual mínima de 80% por arquivo executável e agregado, meta 90%, sem teto. Código gerado não é exclusão. Registrar inventário fonte→teste, comandos, métricas, revisão e relatórios atuais. Sem medição ou abaixo do piso, não concluir IMPLEMENTADA/IMPLEMENTACAO_APROVADA.
- Na fase correspondente, specflow-validar é padrão. Omissão exige prompt explícito ou parada anterior; registrar fonte, motivo/revisão e not_run sem VALIDADA. Omitir PDF não omite segurança ou fase. Comando de fase única não inicia fluxo completo.
- Validação exige security-audit real e execução de docs/security-audit/verificar_seguranca.py sobre o escopo atual. Qualquer achado aberto de qualquer severidade, check falho/não executado ou prova antiga deixa pendente. Código 0 é gate de evidências, não auditoria automática ou aceite.
- Native CLI usa rotina empacotada confiável e exige evidenceManifest/testManifest e vínculos atuais; nunca executar command de JSON. O helper histórico deste repositório possui limites próprios documentados.
- specflow-teste-humano para em IMPLEMENTADA com build/quickstart reais e aguarda teste humano; não avança automaticamente para revisão/validação formais ou aceite.
- Decisão de SPEC, revisão de implementação, validação, teste humano e aceite final são distintos. Testes verdes, parecer do agente, checkbox ou nome de arquivo não fabricam aprovação.
- Configuracao.properties é criado no consumidor com 25 valores DEFINIR e protegido; qualquer campo DEFINIR mantém recurso inteiro inativo, sem probes, downloads ou autenticação. Configuração preenchida não inicia serviço. NAO_APLICAVEL apenas em campo opcional do modo declarado.
- Aplicações geradas ficam em apps/ do consumidor com SPEC/plano/escopo autorizados. Init não cria aplicações. Preservar configuração, documentos e arquivos existentes; conflitos não permitem sobrescrita silenciosa.
- Lock é cooperativo. Falha parcial preserva bytes alterados por terceiro; recuperação de lock abandonado é ação explícita. Não afirmar proteção contra administrador hostil ou autenticação criptográfica de decisões.

## Continuidade e comunicação

Documente em português do Brasil e registre códigos/limites reais. Mantenha memória/progresso fora dos quatro documentos aprovados. Entradas antigas são históricas, não estado corrente. Não crie subagentes sem solicitação explícita aplicável. Não confunda integridade/sintaxe com execução funcional ou homologação.

Conferências de suporte: python -B tools/verificar_dossie.py e python -B tools/gerar_comandos_specflow.py --check. Esses resultados não substituem testes do produto. A cobertura do pacote não certifica automaticamente helpers antigos.