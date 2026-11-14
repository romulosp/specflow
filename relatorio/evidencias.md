> Copia editorial neutralizada. Metricas e verificacoes abaixo sao historicas; originais exatos foram preservados em arquivo externo de auditoria. Links locais mostram recursos atuais, nao provam igualdade com o original.

# Evidências locais e cobertura

Data da coleta: 2026-11-12. Caminhos remetem à origem preservada. Linhas são localizadores da revisão fixada no baseline, não prova de execução. A amostra histórica tem seis Changes arquivadas, escolhidas intencionalmente por mecanismo; não representa aprovação das 55 Changes do arquivo. Todos os textos do manifesto foram lidos/indexados automaticamente; revisão semântica aprofundada restringe-se às fontes e casos aqui discriminados.

| ID | Afirmação sustentada | Fonte | Linha | Tipo |
| --- | --- | --- | --- | --- |
| E01 | Processo obrigatório e exceção autorizada somente para este dossiê | AGENTS.md (registro historico; arquivo nao distribuido) | 12 | documentado |
| E02 | Fonte canônica; sete fases e plano preparatório | [specs/shared/process/workflow.md](../specs/shared/process/workflow.md) | 3 | documentado |
| E03 | Formato, severidade e evidência mínima de testes | [specs/shared/process/evidence-conventions.md](../specs/shared/process/evidence-conventions.md) | 20 | documentado |
| E04 | Revisão contratual e veredito limitado | [.agents/skills/spec-review/SKILL.md](../.agents/skills/spec-review/SKILL.md) | 13 | documentado |
| E05 | Move para archive antes de commit | [.agents/skills/git-commit/SKILL.md](../.agents/skills/git-commit/SKILL.md) | 11 | documentado |
| E06 | Prompt manda mover depois de commit; ordem diverge da skill | [.github/prompts/executar-mudanca-spec-driven.prompt.md](../.github/prompts/executar-mudanca-spec-driven.prompt.md) | 154 | documentado |
| E07 | Índice não contém 10027 apesar da pasta presente | STATUS.md (registro historico; arquivo nao distribuido) | 23 | documentado |
| E08 | Referência a resumo de continuidade ausente | README.md (registro historico; arquivo nao distribuido) | 237 | documentado |
| E09 | Declara política documental que já tem exceções técnicas | specs/system/README.md (registro historico; arquivo nao distribuido) | 5 | documentado |
| E10 | Política documental com inclusões explícitas de scripts e código | .gitignore (registro historico; arquivo nao distribuido) | 20 | documentado |
| E11 | Caminhos locais configuráveis e imagem latest | [scripts/sonar/validar-codigo.ps1](../scripts/sonar/validar-codigo.ps1) | 9 | implementação localizada |
| E12 | Build Java não executa os testes; não comprova qualidade completa | [scripts/sonar/validar-codigo.ps1](../scripts/sonar/validar-codigo.ps1) | 350 | implementação localizada |
| E13 | Quatro testes estruturais, não end-to-end | [scripts/sonar/tests/validar-codigo.Tests.ps1](../scripts/sonar/tests/validar-codigo.Tests.ps1) | 3 | implementação localizada |
| E14 | Algoritmo reutilizável misturado com caminho fixo e credenciais | scripts/gerar_start_aplicacao.ps1 (registro historico; arquivo nao distribuido) | 3 | implementação localizada |
| E15 | Valida duplicata e aceita destino explícito; ainda específico | scripts/gerar_start_aplicacao_fotogaleria.ps1 (registro historico; arquivo nao distribuido) | 5 | implementação localizada |
| E16 | Validador mínimo somente leitura, sem validar a totalidade dos gates | [.agents/skills/android-native-engineering/scripts/validate_android_project.py](../.agents/skills/android-native-engineering/scripts/validate_android_project.py) | 11 | implementação localizada |
| E17 | Referência interna a compose-performance não presente | [.agents/skills/android-native-engineering/kotlin/compose-animations/SKILL.md](../.agents/skills/android-native-engineering/kotlin/compose-animations/SKILL.md) | 18 | documentado |
| E18 | Referência a pprof.md não presente no caminho local | [.agents/skills/golang-benchmark/SKILL.md](../.agents/skills/golang-benchmark/SKILL.md) | 104 | documentado |
| E19 | Backlog e DoR/DoD por evidência; fallback não declara Sonar | [specs/sprint/README.md](../specs/sprint/README.md) | 10 | documentado |
| E20 | Retificação explicita encerramento prematuro; lições registradas | specs/sprint/SPRINT-001-Produto-Base.md (registro historico; arquivo nao distribuido) | 58 | evidência histórica localizada |
| E21 | Decisão persistida com contexto e consequências | docs/adr/ADR-001-java-17-quarkus-3.md (registro historico; arquivo nao distribuido) | 10 | documentado |
| E22 | Memória de Change com fase, decisões, pendências e dados operacionais | specs/changes/10017-logging-semantico-abecs/AGENTS-MEMORY.md (registro historico; arquivo nao distribuido) | 5 | documentado |
| E23 | Validação histórica estrutural da governança | specs/archive/2026-08-27-002-consolidar-governanca-spec-driven/validation.md (registro historico; arquivo nao distribuido) | 15 | evidência histórica localizada |
| E24 | Gate negativo por ausência de risco em pendências | specs/archive/2026-09-05-033-consolidar-governanca-sprint-planner/reviews/2026-09-05-implementation-review.md (registro historico; arquivo nao distribuido) | 3 | evidência histórica localizada |
| E25 | Revisão de retorno confirma correção | specs/archive/2026-09-05-033-consolidar-governanca-sprint-planner/reviews/2026-09-05-implementation-review-resubmissao.md (registro historico; arquivo nao distribuido) | 3 | evidência histórica localizada |
| E26 | Histórico de quatro asserts Pester e fallback 20; Sonar real não validado | specs/archive/2026-09-05-034-automatizar-sonar-local/validation.md (registro historico; arquivo nao distribuido) | 6 | evidência histórica localizada |
| E27 | Falhas iniciais, correções e resultado efetivamente executado | specs/archive/2026-09-06-003-concluir-execucao-produto-base/validation.md (registro historico; arquivo nao distribuido) | 11 | evidência histórica localizada |
| E28 | Reprovação por proveniência, fixture e estados adiantados | specs/archive/2026-09-18-067-android-native-engineering/reviews/2026-09-18-spec-review-complementar.md (registro historico; arquivo nao distribuido) | 16 | evidência histórica localizada |
| E29 | Fixtures, comandos, ferramentas e limites registrados após correção | specs/archive/2026-09-18-067-android-native-engineering/validation.md (registro historico; arquivo nao distribuido) | 9 | evidência histórica localizada |
| E30 | Hashes comprovam cópia; não comprovam fechamento das referências transitivas | specs/archive/2026-09-19-998-importar-skill-kotlin/validation.md (registro historico; arquivo nao distribuido) | 11 | evidência histórica localizada |
| E31 | Acervo importado de estudo; upstream e licença por item ainda necessários | [.agents/skills/README.md](../.agents/skills/README.md) | 62 | documentado |
| E32 | Adaptador impõe parada textual em IMPLEMENTADA | [.github/agents/implementador-para-teste.agent.md](../.github/agents/implementador-para-teste.agent.md) | 15 | documentado |
| E33 | Testes Java por comportamento e inventário de classes | [specs/shared/testing/testing-strategy.md](../specs/shared/testing/testing-strategy.md) | 10 | documentado |
| E34 | Template de contrato genérico | [specs/templates/spec-template.md](../specs/templates/spec-template.md) | 8 | documentado |

## Verificações atuais de ausência/presença

- Confirmadas ausências de `specs/resumo_continuar_projeto.txt`, `kotlin/compose-performance/SKILL.md` e `golang-benchmark/references/pprof.md` nos caminhos referenciados. Não se afirma que não existam fontes equivalentes fora do corpus.
- Não existe diretório `.github/workflows/` nesta origem. Isso não exclui integração externa de CI; execução remota de gates não foi comprovada.
- A varredura mecânica encontrou 599 vínculos Markdown locais e 221 candidatos sem destino resolvido. O número contém histórico, caminhos relativos ambíguos e placeholders; não equivale a 221 defeitos confirmados. E17/E18/E08 foram confirmados separadamente.
- 92 arquivos SKILL.md presentes; o catálogo de sistema que menciona 54 skills representa um estado anterior.
- Nenhuma licença global do projeto foi identificada na raiz. Quatro LICENSE.txt foram localizados em skills; nomes não bastam para definir o direito de redistribuição de todo o acervo.

## Cobertura e limites históricos

As seis Changes amostradas cobrem revisão de SPEC positiva e negativa, implementação documental reprovada e corrigida, validação estrutural, fallback Sonar, correção de testes reais e aprovação/encerramento. A [lista da amostra](../specs/changes/10028-investigar-specflow-framework/evidence/history-sample.json) relaciona os arquivos indexados; estados coexistentes não foram interpretados como uma máquina de estados válida. Nenhum teste histórico de aplicação foi reexecutado.
