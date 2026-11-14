# SPEC — SpecFlow CLI

Status: `EM_REVISAO_SPEC`. Revisão r2, 13/11/2026. Aprovação humana pendente.

## Contrato de operação

CLI prepara consumidor/rascunhos, avalia registros e entrega instruções ao agente no editor. Não chama IA, não executa código de implementação gerado, não promove estados por invocação e não fabrica aprovações. Comandos abaixo são interfaces futuras, não comandos já disponíveis.

| ID | Requisito | Critério de aceite |
| --- | --- | --- |
| CLI-01 | Distribuir specflow-cli 0.1.0, expondo specflow e python -m specflow com o mesmo parser | CA-01: wheel instalado em ambiente limpo executa --help/--version; module e console têm mesmos resultados; versão vem dos metadados do pacote |
| CLI-02 | Runtime Python >=3.11 e stdlib; wheel e sdist incluem somente allowlist de recursos liberados | CA-02: instalar sem dependências de runtime; construir wheel a partir do sdist; conferir inventário, licenças, hashes e ausência de credenciais, acervo incompleto e caminhos externos |
| CLI-03 | init aceita novo destino ou . existente e integrações copilot/codex repetíveis | CA-03: consumidor novo ou existente recebe estrutura comum; seleção única/dupla instala somente integrações selecionadas; sem flag nenhuma integração é inferida; valor desconhecido retorna 2 antes de escrever |
| CLI-04 | init cria configuracao.properties com todas as propriedades do catálogo em DEFINIR e protege o arquivo real | CA-04: todas as 25 propriedades iniciais em DEFINIR; ignore idempotente sem apagar .gitignore; nenhum segredo copiado para metadados, pacote ou logs; repetir preserva bytes autorais |
| CLI-05 | Toda escrita é confinada e precedida de checagem do conjunto de conflitos | CA-05: arquivo divergente, caminho/link inseguro, destino incompatível e travessia falham antes de escrever o conjunto; repetir operação compatível preserva apps e instruções do usuário |
| CLI-06 | doctor verifica arquivos/versões declaradas/configuração local sem ativar recursos | CA-06: init/doctor com DEFINIR, campos faltantes/inválidos ou recurso parcial executam zero rede, login, download ou subprocesso desse recurso; consumidor íntegro com opcionais em DEFINIR retorna 0 e avisos, sem fingir recursos executados; configuração lexicalmente inválida retorna 2 |
| CLI-07 | nova-change cria ID livre e documentos em rascunho a partir de objetivo não vazio | CA-07: duas chamadas não reutilizam pasta; concorrência não sobrescreve; ID aparece na resposta; proposta/SPEC/design/tasks/validation/memória existem, sem SPEC_APROVADA ou evidência passed inventada |
| CLI-08 | contexto, check e evaluate reutilizam núcleo e saída determinística, inclusive para rascunho | CA-08: nova-change seguida de contexto retorna RASCUNHO/0; avaliar avanço de rascunho bloqueia com 1; draft e change simultâneos geram INDETERMINADO/1; entrada inválida 2; leitura não altera bytes; mudar contrato invalida decisões anteriores |
| CLI-09 | Onze comandos canônicos de fase são derivados do mesmo catálogo das Skills/prompts | CA-09: fases e nomes coincidem; ajuda, prompt e Skill não divergem; alias speckflow-teste-humano preservado no editor; nenhum subprocesso de agente/IA é chamado |
| CLI-10 | Comandos de fase verificam entrada aplicável e retornam instrução para o editor com execução da fase pendente | CA-10: resposta de preparação bem-sucedida informa phaseExecuted=false; planejar exige SPEC corrente aprovada; implementar exige também plano; revisão de implementação exige entrega/cobertura; aprovação/encerramento exigem pré-condições próprias |
| CLI-11 | teste-humano prepara fluxo até IMPLEMENTADA e parada humana, sem ultrapassar gates | CA-11: sem SPEC aprovada entrega instrução de especificação/revisão com implementação bloqueada; sem cobertura ou artefato real não declara pronto; não executa revisão/validação formais, aceite ou encerramento |
| CLI-12 | validar confere entrada de validação e executa o verificador local de segurança sobre a auditoria atual | CA-12: gate executa apenas rotina confiável empacotada; ausência, achado aberto de qualquer severidade, check incompleto ou dados antigos mantêm pendente; nunca executar command do JSON; código 0 só satisfaz segurança |
| CLI-13 | Preservar validação padrão e omissão somente por fonte explícita do usuário | CA-13: instruções de fluxo completo incluem validar; registro not_run não satisfaz VALIDADA; pedir somente omissão de PDF não dispensa a fase; comando de fase única não inicia fluxo inteiro |
| CLI-14 | aprovar/encerrar apresentam pacote para o agente/humano, sem decisão ou encerramento automático | CA-14: comando, --json ou teste verde não criam registro approved, movem Change ou criam commit; testar rejeição e decisões substituídas/desatualizadas |
| CLI-15 | Flags comuns --help, --version, --project e --json; saída 0/1/2 com prioridade 2 > 1 > 0 | CA-15: argumentos inválidos retornam 2; pendências válidas 1; operação satisfeita 0; JSON parseável sem ANSI, segredos ou timestamp variável; stdout para resultado e stderr para diagnóstico textual |
| CLI-16 | Instalação/atualização do CLI não modifica consumidores | CA-16: snapshots antes/depois de instalar e trocar wheel permanecem iguais; package init/update hooks não executam migração; upgrade aplicado permanece fora desta versão |
| CLI-17 | Compatibilidade e integração são demonstradas e limitadas ao que foi exercitado | CA-17: testes reais Windows/Linux; descoberta e invocação no editor Copilot/Codex com cliente/versão/evidência; ambiente indisponível fica not_run e impede declarar aquele critério aprovado |
| CLI-18 | Testes funcionais/negativos, cobertura e auditoria antecedem aprovação de implementação | CA-18: suíte passa e cobertura >=80% por arquivo executável e agregado, meta 90%, sem teto; relatórios atuais por manifesto; faltante/falha/79,99% bloqueiam; agente não estima cobertura |
| CLI-19 | Entregar pacote local verificável e documentação sem referências externas removidas | CA-19: wheel/sdist, hashes, inventário, guia, diagrama e quickstart reais; varredura na árvore, arquivos gerados e arquivos de texto do pacote sem identidades/links retirados; originais auditáveis fora da distribuição |
| CLI-20 | Todas as operações de escrita compartilham lock e protocolo da 10030, incluindo integração aditiva da mesma versão | CA-20: init Copilot seguido de init Codex preserva arquivos existentes, acrescenta somente novos recursos/metadados permitidos; dois escritores não intercalam commits; lock ocupado é 1, erro de I/O é 2 e rollback nunca apaga bytes alterados por terceiro |
| CLI-21 | validar exige vínculos atuais dos bytes de evidência além de executar o gate confiável | CA-21: gate 0 com evidenceManifest ausente/antigo, teste/log/relatório alterado ou escopo incompleto mantém saída 1; metadado malformado retorna 2; nenhum binding é atualizado para aparentar reexecução aprovada |

## Interfaces públicas e fronteiras

`specflow init <destino> [--integration copilot] [--integration codex]`, `doctor`, `nova-change <objetivo>` e os onze nomes de fase sem o prefixo specflow-. Fases recebem --change <id>; projeto padrão é a raiz reconhecida no diretório corrente ou ancestral mais próximo, sem varrer diretórios irmãos. --project explícito prevalece. check/evaluate recebem também --target; contexto não exige alvo.

As flags de projeto/JSON são aceitas antes ou depois do subcomando, com repetição conflitante rejeitada. init sem --project resolve o destino relativo ao diretório corrente; com --project o destino é relativo à raiz explícita. Nenhum --force/--yes permite ignorar conflito, gate ou aprovação. Objetivos e campos de configuração são dados, nunca shell.

Read-only: doctor, contexto, check/evaluate e preparação de fases. Escrita: init, nova-change e, em validar, somente security-gate.json na Change selecionada. Comandos de editor continuam conduzindo os trabalhos autorizados; resultado do CLI não declara sua execução. Gate de validação é exceção explícita de rotina local determinística, não um scanner.

A reserva/remoção do próprio lock é exceção de metadado de controle dessas operações de escrita, não alteração autoral nem fase concluída. Comandos de leitura com escritor ativo retornam 1/PROJECT_BUSY para não ler um commit parcial; --help/--version independem da raiz. O gate é gravado por temporário/replace, sem seguir link no destino; arquivo autoral/incompatível no lugar do gate é conflito 1. Resultado do CLI pode conter localChecksExecuted=['security_gate'], mantendo phaseExecuted=false para a fase completa.

doctor considera recurso opcional não configurado como informação, não falha global. Recurso preenchido porém inválido gera pendência 1; erro lexical/estrutural de configuração ou projeto retorna 2; arquivo gerenciado divergente ou lock ocupado retorna 1. Gates específicos continuam exigindo recurso configurado quando necessário à fase. Nenhum código 0 do doctor significa auditoria, cobertura ou integração visual executada.

Nomes de fase: contexto, especificar, esclarecer, revisar-spec, planejar, implementar, teste-humano, revisar-implementacao, validar, aprovar, encerrar. Contexto usa a operação nativa de leitura; demais fases retornam instrução e pendências. validar agrega a rotina de segurança somente se a implementação já tiver revisão técnica válida; caso contrário informa bloqueio sem alterar a Change.

## Qualidade e segurança

Perfis de digest, métodos de evidência e decisões seguem 10029 r6. DEFINIR e NAO_APLICAVEL seguem 10030 r4. Código de aplicação criado pelo agente fica abaixo de apps e exige SPEC aprovada da Change consumidora; init não cria código de aplicação.

Nenhum diagnóstico imprime valor de configuração/credencial. Referências são confinadas à raiz explícita, inclusive após resolução de links. Ambiente do processo e metadados não sobrepõem silenciosamente properties. Dependência obrigatória indisponível bloqueia o gate; não simular auditoria, cobertura ou compatibilidade.

O produto verifica consistência de registros, sem autenticar a pessoa declarada ou garantir a verdade de uma evidência. Auditoria real, revisão e decisão humanas continuam necessárias. PDF opcional exige revisão visual própria, sem substituir segurança. Publicação permanece autorizável separadamente.
