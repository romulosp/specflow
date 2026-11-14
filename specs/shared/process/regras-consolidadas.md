# Regras consolidadas do SpecFlow

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Historico anterior a este marco

Revisão normativa de suporte 1 — 13/11/2026. Copyright (c) 2026 Rômulo Penha; MIT para este texto autoral, preservados direitos dos componentes incorporados.

Este registro reúne as determinações desta conversa e sua aplicação operacional. Não aprova arquitetura, SPEC de implementação ou publicação. **U** indica determinação do usuário; **O** indica operacionalização documentada que deve preservar aquela intenção; **P** indica proposta técnica ainda em revisão. Documentos detalhados continuam donos dos respectivos formatos; este registro é o índice normativo e a resolução das divergências legadas.

## Precedência e fontes

Instrução explícita atual do usuário prevalece. Em seguida, aplicar [AGENTS.md](../../../AGENTS.md), este registro e as políticas detalhadas locais; workflow organiza a sequência e Skills/prompts conduzem suas fases. Material histórico/importado não pode enfraquecer os gates. Não promover proposta P a decisão humana por aparecer neste documento. Decisão humana já válida para o mesmo escopo/revisão não precisa ser solicitada novamente.

Fontes locais de continuidade: [memória 10029](../../changes/10029-criar-nucleo-specflow/AGENTS-MEMORY.md), [decisões pendentes](../../changes/10028-investigar-specflow-framework/DECISOES-PENDENTES.md), [guia de comandos](../../../docs/comandos/COMANDOS.md) e [estado do acervo](../../../docs/estado-acervo.md). As mensagens do usuário desta conversa são a fonte das determinações U; não criar citações literais ou aprovações que não ocorreram.

## Identidade, escopo e preservação

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-01 | U | SpecFlow é um projeto autônomo com processo Spec Driven próprio | README e AGENTS; contratos detalhados sujeitos a aprovação |
| SF-02 | U | Trabalhar neste workspace; não apagar, mover ou modificar o checkout externo | AGENTS; cópia local de suporte foi expressamente autorizada, sem autorização geral de migração |
| SF-03 | U/O | Recursos necessários devem estar locais; retirar identificadores/referências ao ambiente anterior da árvore distribuível | Manifesto local separa fonte/representação; originais exatos ficaram no arquivo externo de auditoria, sem dependência de runtime |
| SF-04 | U/O | Não copiar segredos, logs operacionais, dados de pagamento/protocolo ou memória particular para acervo global | Avisos/proveniência preservados; corpus histórico não é estado atual do consumidor |
| SF-05 | U | Manter memória de continuidade e estado real atualizados; continuar das evidências sem repetir investigação concluída | Memórias por Change, STATUS e registros de validação; não transformar tarefa planejada em concluída |

## Processo Spec Driven e decisões humanas

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-06 | U/O | Sete fases: especificação, revisão da SPEC, implementação, revisão da implementação, validação, aprovação e encerramento | [workflow](workflow.md); esclarecimento e planejamento são auxiliares |
| SF-07 | U/O | Contrato contém proposal.md, spec.md, DESIGN.md e tasks.md; reviews e validation registram evidências | Templates locais; requisitos e aceites verificáveis, sem ampliar escopo silenciosamente |
| SF-08 | U | Não implementar sem SPEC_APROVADA da revisão corrente | Parecer técnico favorável, pedido genérico, checkbox, existência de arquivo, tempo ou testes verdes não são aceite humano |
| SF-09 | U/O | Após SPEC_APROVADA, registrar implementation-plan antes do código | Plano não reescreve contrato aprovado e não cria nova fase |
| SF-10 | U/O | Aprovação identifica fonte humana, ator, escopo e revisão/manifesto; alteração relevante exige revisão e aceite atuais | Aprovação da investigação não se transfere ao núcleo; registro não autentica identidade nem é assinatura |
| SF-11 | O | Revisão não corrige código; validação não corrige código; aprovação não implementa/testa | Falha de requisito retorna à SPEC; falha de código/teste à implementação; preservar histórico e repetir cenários afetados |
| SF-12 | U/O | Aceite final é humano e posterior à entrega/revisão/testes aplicáveis da mesma revisão | Executável/harness real, quickstart e resultados observados; roteiro escrito não é teste executado |
| SF-13 | U | Commit, archive, publicação, deploy e ações externas não decorrem automaticamente de aprovação | Encerramento só com condições/autorização aplicáveis; sem Git não inventar commit ou inicializar repositório como efeito colateral |
| SF-14 | O/P | Preparar system e candidato de archive, conferir conjunto e registrar recibo posterior do encerramento efetivo | Política detalhada do novo núcleo está em revisão; não alegar hash de commit dentro do próprio commit nem ARQUIVADA antes da ação |

## Comandos e teste humano

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-15 | U/O | Comandos locais por fase, com guia e diagrama | Catálogo em docs/comandos/comandos.json; Skills Codex e prompts Copilot, não executável de shell ou motor já implementado |
| SF-16 | U/O | Comando de fase única respeita sua fronteira e gates; não dispara todas as etapas seguintes | Fluxo completo é orquestração explícita; nenhum comando autoriza subagentes ou publicação por efeito colateral |
| SF-17 | U | specflow-teste-humano, com alias speckflow-teste-humano, conduz até IMPLEMENTADA e para para o usuário testar | Contrato/aceite/plano antes de código; build/harness real, revisão/hash, checks técnicos e quickstart; não faz revisão/validação formais, aprovação ou encerramento |
| SF-18 | U/O | Resultado não utilizável não é pronto para teste; falha relatada volta à mesma Change e nova entrega identificada | Registrar bloqueio real; não usar simulação como homologação, nem resultado positivo como autorização de fases posteriores |

## Testes e cobertura na implementação

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-19 | U | Todo código implementado exige testes codificados e executados antes de aprovação da implementação | Inclui código gerado pelo agente, scripts, frontend/backend e núcleo; testar comportamento, falhas e limites |
| SF-20 | U/O | Faixa solicitada de 80% a 90%: piso obrigatório 80%, meta 90%, valores superiores válidos | [coverage-policy](../testing/coverage-policy.md); aferição por arquivo/escopo implementado e agregado, sem médias que escondam arquivo sem teste |
| SF-21 | O | Medir linhas/instruções executáveis com ferramenta da stack; branches conforme disponibilidade e requisitos técnicos | Relatório atual, revisão/hashes, arquivos/testes/aceites, ferramenta/versão, comando/cwd, códigos e percentuais reais |
| SF-22 | U/O | Sem suíte aprovada, medição atual e piso atendido, não concluir IMPLEMENTADA nem registrar IMPLEMENTACAO_APROVADA | Bloqueio também vale para entrega teste-humano; ferramenta ausente não dispensa cobertura; não estimar ou usar LLM/manual como substituto |
| SF-23 | O | Não excluir código autoral por ser gerado, mudar denominador artificialmente ou arredondar percentual inferior para passar | Artefato sem código executável: não aplicável com justificativa e sem percentual fictício; exclusões mecânicas reais precisam de contrato/revisão |

## Validação e segurança

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-24 | U | Ao alcançar a validação da implementação em fluxo autorizado, executar specflow-validar por padrão | Não exigir pedido rotineiro separado; pressupõe implementação tecnicamente aprovada |
| SF-25 | U/O | Omitir essa fase somente se o prompt do usuário explicitamente o pedir ou limitar o fluxo antes dela | Registrar solicitação/motivo/revisão e fase não executada; não marcar VALIDADA ou liberar aprovação/encerramento; pedir só para omitir PDF/ferramenta não dispensa a fase |
| SF-26 | U/O | Na validação executada, chamar obrigatoriamente security-audit e verificar_seguranca.py | [gate de segurança](../../../docs/security-audit/GATE-SEGURANCA.md); análise real da skill e JSON atual com escopo/digests/evidências |
| SF-27 | U/O | Qualquer achado aberto, em qualquer severidade, check falho/incompleto, auditoria ausente/desatualizada ou erro deixa a validação pendente | Sem VALIDADA ou avanço para aprovação; corrigir na implementação, revisar e refazer auditoria/gate |
| SF-28 | O | O gate verifica evidências e não é scanner/autenticação; JSON não pode executar comandos ou ampliar permissões | Não alegar segurança completa por código 0 ou arquivo de auditoria existente; responsável confere escopo e veracidade |
| SF-29 | U/O | Gerador PDF apenas formata resultados atuais; PDF somente quando solicitado | Não reutilizar conclusões antigas; sem segredos; se gerar, extrair texto e inspecionar visualmente todas as páginas antes da entrega |
| SF-30 | O | Fallback de qualidade por LLM pode ajudar onde não houver Sonar, mas não substitui cobertura medida, segurança ou checks obrigatórios | Falha de ferramenta disponível não vira fallback ou autorização para pular gates |

## Inicialização e geração de aplicações

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-31 | U | A inicialização sempre cria um arquivo de configuração .properties, independente dos recursos configurados | Nome operacional proposto: configuracao.properties; todos os valores gerados começam em DEFINIR |
| SF-32 | U/O | Enquanto houver DEFINIR na configuração de um recurso, não tentar utilizá-lo | Sem conexão, autenticação, download, inicialização ou execução/version check; bloquear só aquele recurso, sem desabilitar os demais |
| SF-33 | U/O | Recursos só podem ser utilizados com informações aplicáveis preenchidas/válidas e quando requeridos por ação autorizada | Preencher arquivo não dispara execução; faltante/vazio/inválido continua inativo; recurso obrigatório inativo mantém seu gate pendente |
| SF-34 | U/O | Arquivo central reúne URL, autenticação, usuário/senha de serviço e demais parâmetros declarados pelos recursos | Credenciais ficam locais, não versionadas/publicadas/logadas; campos opcionais e autenticação sem credenciais precisam de contrato explícito do adaptador |
| SF-35 | U | A geração de código cria apps/ na raiz do projeto consumidor e põe as aplicações ali | Não confundir saída do consumidor com código interno do framework; geração só após SPEC aprovada |
| SF-36 | O | Inicialização/geração repetida preserva configuração preenchida, apps existentes e documentos autorais | Não sobrescrever/resetar valores nem sair da raiz; parâmetros/links que escapem de apps são rejeitados; mudanças de versão começam por plano de conflito |

As regras SF-31..36 são requisitos determinados para a futura inicialização/geração; não afirmam que já existe init executável. Detalhamento proposto na [Change 10030](../../changes/10030-inicializar-consumidor-configuracao/proposal.md). Não criar apps ou configuração real neste workspace apenas para fingir execução da fase.

## Autoria, licença e distribuição

| ID | Tipo | Regra vigente | Aplicação / fonte operacional |
| --- | --- | --- | --- |
| SF-37 | U | Copyright Rômulo Penha e MIT para o material autoral do SpecFlow | LICENSE e LICENSE-SCOPE; não autoriza publicação remota por si só |
| SF-38 | U/O | Preservar autores/licenças de terceiros e não relicenciar material sem direito confirmado | THIRD_PARTY_NOTICES; MIT de outro projeto não libera todo acervo; excluir direitos desconhecidos de uma distribuição pública até liberação |
| SF-39 | O | Não declarar completude funcional por cobertura de cópia, sintaxe ou fixtures | 360 recursos e 92 skills originais incorporados; das 149 referências opcionais históricas, três links corrigidos e 146 ausências registradas; operações dependentes bloqueadas, sem placeholders |
| SF-40 | U/O | Documentar fatos, comandos, códigos, método, escopo, limitações e revisão; manter evidências separadas das decisões | Diferenciar estrutura/runtime, teste do agente/teste humano, validação técnica/aceite humano e acervo/framework executável |

## Propostas técnicas que continuam em revisão

Não estão aprovadas pela consolidação: arquitetura detalhada, aceite do diagnóstico e SPECs de implementação. A direção de CLI + agente no editor, nome specflow-cli/specflow e memória local foi solicitada pelo usuário; seus contratos concretos continuam em revisão: núcleo 10029 r6, inicialização 10030 r4 e CLI 10031 r2. Originais anteriores estão em auditoria externa. Não editar documentos contratuais sem identificar nova revisão/manifesto.

| ID | Proposta P / limite | Fonte |
| --- | --- | --- |
| P-01 | Núcleo local pequeno, módulos internos de contratos/workflow/memória/assets/validação e adaptadores opcionais; sem sete serviços | Design/arquitetura candidatos, não implementação existente |
| P-02 | Python >=3.11, stdlib no runtime do núcleo, validadores específicos de registro, sem engine JSON Schema genérica | SPEC/design 10029 em revisão; não obriga linguagem das aplicações |
| P-03 | SHA-256 com perfil explícito: texto UTF-8 estrito/BOM inicial opcional/LF, binário byte a byte; sem trim/normalização semântica; perfil integra vínculo | Contrato r6, preservando perfis anteriores e revisão técnica recebida; manifesto não é assinatura de pessoa |
| P-04 | Métodos estruturado/funcional/manual explícitos e códigos 0 verificado, 1 violação/conflito, 2 erro; context indeterminado retorna 1 | Interfaces candidatas; harness do núcleo ainda não implementado |
| P-05 | Memória privada por consumidor, proveniência/supersessão e índice reconstruível; sem servidor ou banco vetorial no primeiro incremento | Recomendada, sujeita às decisões humanas de contratos/memória |
| P-06 | Distribuição/versionamento/lock/ownership e upgrade com plano/conflitos/rollback sem sobrescrever conhecimento autoral | Roadmap futuro; pacote/piloto e Windows/Linux ainda precisam de prova |
| P-07 | Contrato exato das propriedades, modos de autenticação/campos não aplicáveis e catálogo de recursos | Change 10030 em revisão; não atribuir capacidade a integração sem implementação/teste |
| P-08 | RASCUNHO antes das sete fases, contexto utilizável e avanço bloqueado até contrato completo | 10029 r6/10031 r2; ajuste escolhido por delegação técnica, sem aprovação humana de SPEC |
| P-09 | Um protocolo de lock/preflight/compare-replace/rollback e init aditivo da mesma versão | 10030 r4/10031 r2; sem transação global fictícia ou sobrescrita autoral |
| P-10 | Manifestos dos bytes de evidências/testes/relatórios e política fixa; gate v1 0 não basta | 10029 r6/10031 r2; helper existente ainda não implementa os novos vínculos/escrita |
| P-11 | Gramática explícita de properties e doctor saudável com opcionais em DEFINIR | 10030 r4/10031 r2; recurso opcional inativo não é teste executado ou falha global |

## Divergências legadas resolvidas por esta revisão

- Parecer técnico favorável não promove SPEC_APROVADA ou APROVADA humana.
- Encerramento não executa commit/arquivo automaticamente; recibo e estado dependem da ação efetiva autorizada.
- Cobertura deixa de ser opcional por indisponibilidade; LLM não satisfaz seu piso. Meta operacional é 90%, sem rejeitar cobertura superior.
- Segurança é obrigatória em specflow-validar; PDF não é auditoria/gate e não é gerado por padrão.
- Validação é padrão ao alcançar a fase, com omissão somente por prompt explícito e sem promoção de estado.
- teste-humano é fluxo composto até IMPLEMENTADA, não aceite final; inclui cobertura técnica antes da entrega e preserva a parada.
- Regras Java/Go/Android/Frontend continuam perfis técnicos locais, acionados por stack, não imposições universais sobre o núcleo. Índice em [.agents/skills](../../../.agents/skills/README.md) e políticas em specs/shared.

As fontes detalhadas e comandos gerados devem apontar para este registro. Cada nova determinação deve atualizar a regra pertinente, sua evidência e a memória, preservando revisões anteriores; não criar uma segunda aprovação paralela.
