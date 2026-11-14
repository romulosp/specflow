> Copia editorial neutralizada. Metricas e verificacoes abaixo sao historicas; originais exatos foram preservados em arquivo externo de auditoria. Links locais mostram recursos atuais, nao provam igualdade com o original.

# Arquitetura candidata — pendente de aprovação humana

## Decisão proposta e justificativa

O [diagnóstico](diagnostico.md) e a [direção autônoma](direcao-autonoma.md) fundamentam esta proposta. Recomenda-se pacote local de políticas, contratos, assets e ferramentas determinísticas, com adaptadores de editor. Não criar sete serviços independentes sem necessidade demonstrada.

| Responsabilidade | Fronteira recomendada | Justificativa pelas evidências |
| --- | --- | --- |
| Core + Workflow | Mesmo módulo interno `workflow` | Mesmos estados, regras e ciclo de revisão; E01–E06 |
| Memory | Módulo interno `memory`, dados por consumidor | Estado e justificativas têm propriedade distinta dos assets; E07–E09/E21/E22 |
| Templates | Módulo `assets`, resolvido por perfil/pacote | Templates atuais são arquivos; não exigem serviço de geração; E34 |
| Automation | Comandos finitos e adaptadores, sem engine genérico | Scripts têm efeitos e dependências particulares; E11–E15 |
| Validation | Módulo `validation`, verificadores puros + adaptadores isolados | Separar sintaxe, contrato, histórico e execução; E12/E13/E16/E27 |
| Extensions | Pacotes opcionais com manifesto e capacidades | Skills e validadores dependem de stack, licença e recursos; E17/E18/E31 |
| Integração de agente | Adaptadores nas bordas | Convenções do provedor não definem estado autoritativo; E32 |

Direção de dependências: CLI/adaptadores → serviços internos → contratos/políticas. `memory` recebe resultados de validação e referências; não dispara scripts. Extensões dependem do contrato público, não de caminhos físicos do core. Apenas o consumidor possui seus documentos e eventos de aprovação.

## Repositório futuro, não criado nesta missão

```text
specflow-framework/
  pyproject.toml
  README.md, LICENSE, CHANGELOG.md
  src/specflow/
    contracts/       formatos versionados
    workflow/        políticas e pré-condições
    memory/          contexto e referências de conhecimento
    assets/          templates e renderização determinística
    validation/      integridade, referências, estado e relatório
    cli/             operações explícitas
  packages/
    core/            política e templates genéricos
    extensions/      Java, Go, Android, Sonar: opt-in
    adapters/        Codex, Copilot
  docs/adr/
  tests/fixtures/    consumidores sintéticos independentes
  .github/workflows/
```

Python >=3.11 é recomendação de implementação para o ferramental local, apoiada pela presença de Python e pelo ecossistema do adaptador pesquisado; não obriga a linguagem das aplicações consumidoras. O laboratório poderá rejeitar um CLI próprio caso composição com o host satisfaça todos os testes. Não haverá dependência de Java/Go/Android/Docker no core. Os pacotes técnicos podem exigir suas ferramentas explicitamente.

## Interfaces públicas mínimas candidatas

| Interface | Entrada / saída | Propriedade e regra |
| --- | --- | --- |
| Manifesto de pacote | ID, versão, licença/proveniência, dependências compatíveis, assets e hashes, capacidades | Framework distribui; consumidor fixa no lock; rejeitar dependência ausente/ciclo e caminho fora da raiz |
| Configuração de projeto | ID local, caminhos, perfil, extensões e política selecionada | Consumidor autoral; nunca conter segredo; `.specflow/project.json` proposto |
| Lock/ownership | Versões exatas, digests e baseline dos arquivos gerados | Ferramenta mantém `.specflow/lock.json`; não contém decisões do projeto |
| Verificador | Raiz, política e referências → achados com ID, severidade, fonte, método, código e limites | Somente leitura; `0` verificado no escopo, `1` violação, `2` erro/precondição; adapter traduz códigos de ferramentas externas |
| Avaliação de transição | Change, fase pretendida, revisões/evidências/decisão → permitida ou bloqueada, com razões | Não muda fase só porque um arquivo existe; nunca fabrica decisão humana |
| Recuperação de contexto | Projeto/Change → fase observada, fontes, decisões, pendências, conflitos e próximos passos | Somente leitura; fontes conflitantes resultam em estado indeterminado, sem promoção silenciosa |
| Template | ID, pacote fixado, parâmetros → candidato + proveniência | Nunca escreve sobre documento autorado sem operação explícita e inspeção de conflitos |
| Adaptador técnico | Capacidade requerida + parâmetros → resultado, código original e artefatos | Não executado por resolução de template ou leitura da memória; política humana preservada |

Os nomes são propostas de contrato, sem API implementada. Formatos terão `schemaVersion`; alterações incompatíveis exigirão migração e major. O MVP precisa validar essas interfaces antes de estabilizar schema público. Importação de estado existente deve preservar o texto original e registrar inferências; não gerar eventos retroativos como se fossem aprovações históricas reais.

## Memória global e particular

- **Global do framework:** políticas, templates, padrões e lições genéricas aprovadas, com versão, autoria, fonte e licença. Publicada no pacote, sem dados de consumidores.
- **Particular do projeto:** estado, contexto, justificativas, ADRs, Changes, pendências e lições locais. Continua no projeto; nenhum envio automático ou acervo global compartilhado.
- **Operacional transitório:** PIDs, portas, logs, caminhos de dispositivo e ambiente. Mantido localmente quando necessário, separado do conhecimento duradouro; nunca convertido em padrão global. Memórias antigas devem advertir que a informação operacional pode ter expirado.

Proposta de armazenamento local: Markdown autoral mais referências/eventos estruturados sob `.specflow/knowledge/`; índice derivado reconstruível, sem servidor ou busca vetorial. `context` deve localizar fase por revisão/evidência vigente, e não pela ocorrência mais recente de uma palavra. Cada decisão precisa de motivo, alternativas, fonte, estado e referência que a substitui. Lições precisam de incidente, ação, aplicabilidade e fonte; exportação exige seleção, sanitização e autorização.

Aprovações devem identificar ator e escopo, vincular hashes dos artefatos revisados e registrar quais decisões substituem. Uma edição posterior do contrato torna sua aprovação anterior insuficiente. Esse registro é rastreável, mas não é autenticação forte nem assinatura criptográfica: validação de identidade é integração futura, se necessária.

Retomada esperada: selecionar projeto → descobrir Change → reconciliar contrato/tasks/reviews/memória/Git → exibir fase e conflitos → recuperar justificativas/lições aplicáveis → informar pendências e condição de avanço. O framework não resolve sozinho conflitos normativos como D-01.

## Instalação, atualização e compatibilidade

Distribuição candidata por wheel e arquivo de release com hashes, sem cópia manual. Instalação em ambiente isolado; comandos de inicialização geram somente o esqueleto e os vínculos de integração aprovados. No MVP, Windows PowerShell e Linux em matriz de testes; shell específico é dependência de extensão, não do core.

Separar arquivo gerenciado imutável, documento gerado ainda intacto e documento autorado. Atualização começa por `plan/dry-run`, compara versão antiga, baseline e arquivo atual, lista conflitos e produz candidatos externos ao documento autorado. Aplicação explícita só modifica arquivos gerenciados sem conflito; requer backup e rollback. Memória, ADRs e aprovação nunca são sobrescritos por atualização de pacote.

SemVer para pacote, política e contratos: patch corrige sem mudar requisito; minor adiciona capacidade opt-in compatível; major altera exigência/formato incompatível. Lock impede atualização implícita. Extensão declara faixa do core e ferramenta; adaptador declara versão do host. Atualizar primeiro o piloto sintético, depois um consumidor autorizado; Protótipo não será convertido automaticamente.
