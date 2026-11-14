> Copia editorial neutralizada. Metricas e verificacoes abaixo sao historicas; originais exatos foram preservados em arquivo externo de auditoria. Links locais mostram recursos atuais, nao provam igualdade com o original.

# Diagnóstico anterior à arquitetura

## Conclusão fundamentada

A metodologia possui governança documental consistente no desenho, uso demonstrado de revisão negativa e correção e alguns mecanismos executáveis. Ainda não está pronta para distribuição independente: faltam fechamento de dependências, autorização de redistribuição, reconciliação de estados e instalação/atualização verificáveis. As fontes e os limites de cada afirmação constam no [catálogo de evidências](evidencias.md).

A proteção principal dos gates é a instrução ao agente e a revisão humana. Nesta origem não foi localizado executor genérico que impeça mecanicamente uma transição inválida. A ausência de `.github/workflows/` não prova ausência de CI externo. Não foi demonstrado serviço central de memória, banco de lições ou recuperação automática do estado real.

## Mapa da estrutura atual

```text
projeto-origem/
  AGENTS.md, STATUS.md, README.md, NotasProjeto.md
  specs/
    shared/       processo canônico + convenções Java, Go, Android
    templates/    proposta, spec, design, tarefas, validação, plugin
    sprint/       política, templates, prompts e uma Sprint concreta
    changes/      28 diretórios de mudanças em andamento
    archive/      55 diretórios de mudanças históricas
    system/       descrições vigentes, parcialmente desatualizadas
    legacy-prompts/ e 01..05/  material histórico/didático
  .agents/skills/  92 SKILL.md, referências e recursos auxiliares
  .github/        agente e prompts; sem workflows locais
  scripts/        launchers específicos + Sonar + testes estruturais
  docs/adr/       índice e ADR Java
  apps/           aplicações e configurações particulares; fora da extração
```

Contagens derivadas do manifesto: 1.385 arquivos textuais, 240 componentes; 24 A, 102 B, 114 C. D representa lacunas adicionais, não arquivos existentes. 1.309 arquivos são rastreados e 76 ignorados. O manifesto exclui binários, caches e dependências de aplicações; PDFs de auditoria são evidência histórica referenciada, sem inspeção visual nem reaproveitamento como validação atual. A categoria A indica candidatura do mecanismo genérico: o próprio AGENTS contém particularidades que não poderão ser transportadas integralmente.

## Cobertura das 18 áreas

| Área | Resultado e comprovação | Destino candidato |
| --- | --- | --- |
| 1. Diretórios | Mapa e manifesto verificáveis; estado local distingue rastreados/ignorados | Metadados C; organização genérica A |
| 2. Governança | AGENTS e workflow impõem gates; E01–E06 | A, retirando regras particulares |
| 3. Desenvolvimento | Skills e convenções técnicas; E31/E33 | Processo A; tecnologia B |
| 4. Mudanças | Contratos, reviews e evidência; E23–E29 | A; registros históricos C |
| 5. Ciclo Spec Driven | Sete fases, retorno e plano preparatório; E02 | A |
| 6. Especificação | Templates de proposta/spec/design; E34 | A; plugin de negócio B |
| 7. Planos/tarefas | tasks-template e planejamento pós-aprovação; E02 | A |
| 8. Skills | 92 definições com recursos inventariados; licença/upstream incompletos | A/B; liberação condicionada |
| 9. Automação | Três geradores, Sonar, seis scripts MJS e dois SH; E11–E15 e suplemento | Sonar B; launchers atuais C |
| 10. Validadores | Sonar, validador Android, arquitetura JS e Mermaid; Pester estrutural; E12/E13/E16 e suplemento | B; validação genérica futura D |
| 11. Segurança | Políticas, skill de auditoria, escaping e exclusões; E10/E14/E28 | Política mínima A; controles técnicos B |
| 12. Integridade | Hashes históricos de importação, manifesto atual e assinatura/digest particulares descritos no sistema; E30 | Hash genérico A; Android B; transitivas D |
| 13. Rastreabilidade | IDs RF/CA/T/reviews presentes, porém sem índice requisito→tarefa→arquivo→teste demonstrado para todo projeto | Base A; automação D |
| 14. Backlog/Sprint | Backlog por pasta, READY/DONE por gate; E19/E20 | Modelo A; Sprint concreta C |
| 15. Decisões | docs/adr e decisões em Changes/memórias; E21/E22 | Modelo A; decisões C |
| 16. Lições | Retrospectiva com ação concreta; E20 | Modelo A; busca e reúso sistemático D |
| 17. Estado atual | STATUS, system, tarefas e memória; divergências verificadas E07/E09/E28 | Estado C; reconciliador D |
| 18. Contexto | Memórias por Change com fase/decisões; resumo referenciado ausente; E08/E22 | Conteúdo C; contrato de memória A; recuperação D |

Recursos adicionais, efeitos e limites: [suplemento de recursos](recursos-executaveis.md).

## Maturidade por dimensão

Escala qualitativa: **definido** = regra explícita; **demonstrado parcialmente** = implementação/evidência em cenários limitados; **reproduzido** = cenário executado nesta investigação; **não demonstrado** = não localizado ou não exercitado. Nenhuma média global.

| Dimensão | Avaliação | Fundamento e limite |
| --- | --- | --- |
| Gates e consistência | Definido; demonstrado parcialmente | Reprovação e retorno E24/E25; ordem de archive/commit diverge E05/E06 |
| Evidência de execução | Demonstrado parcialmente | E27 corrige declaração prematura; não reexecutados sistemas |
| Skills e extensibilidade | Definido; fechamento incompleto | E17/E18 têm recursos referenciados ausentes |
| Validação determinística | Reproduzido em escopo estrutural | Sintaxe de cinco PS1, quatro testes Pester e fixtures Android; não prova Sonar/Gradle |
| Rastreabilidade | Definido; parcial | IDs presentes; ausência de verificador universal não demonstra inexistência de ferramentas externas |
| Memória/estado | Definido localmente; recuperação automática não demonstrada | Memória detalhada E22, referência ausente E08 e índices divergentes |
| ADR e lições | Demonstrado parcialmente | Um ADR central e retrospectiva concreta; decisões também dispersas |
| Segurança | Definido; validação limitada | Não auditados aplicações, binários ou histórico completo de segredos |
| Independência e manutenção | Não demonstrado | Scripts com caminhos/nomes locais; sem instalação/upgrade independente exercitados |
| Distribuição e direitos | Não demonstrado | Sem licença global identificada; licenças isoladas exigem revisão |

## Lacunas e oportunidades — categoria D

| ID | Afetados / evidência | Lacuna e risco | Recomendação e aceite futuro |
| --- | --- | --- | --- |
| D-01 | AGENTS, workflow, skills, E05/E06 | Sequência de encerramento divergente | Formalizar uma transição e testes; não corrigir a origem nesta missão |
| D-02 | STATUS, system, memórias, E07–E09 | Estado e contexto podem ser recuperados incorretamente | Reconciliar com origem, revisão e conflitos visíveis, sem promover gate |
| D-03 | Skills, E17/E18/E30 | Cópia com hashes preserva referências quebradas | Fechar dependências e validar recursos transitivos de cada pacote |
| D-04 | Acervo, E31 | Proveniência/licença insuficiente para publicação | Aprovar direitos por componente e manter avisos; bloquear publicação desconhecida |
| D-05 | Sonar, launchers, E11–E15 | Caminhos e tecnologia implícitos; efeitos operacionais | Configuração do consumidor, versão fixa e adaptadores opt-in |
| D-06 | Workflow/reviews, E20/E28 | Texto e status não garantem gate real | Verificador determinístico de pré-condições e vínculo à revisão aprovada |
| D-07 | RF/CA/T e evidências | Rastreabilidade desigual e revisão manual cara | Índice navegável requisito→tarefa→artefato→teste, explicitando ausências |
| D-08 | Memórias/ADR/Sprint | Recuperação de decisão/lição depende de leitura dispersa | Contrato local de conhecimento com justificativa, fonte e supersessão |
| D-09 | Templates/skills | Sem instalador e atualização protegida demonstrados | Lock de versões, ownership e atualização com detecção de conflitos |
| D-10 | Segurança/logs/memória | Globalizar memória pode transferir contexto sensível | Estado local privado por padrão; exportação explícita e sanitizada |
| D-11 | Pester/validador/Sonar | Teste estrutural pode ser confundido com validação integral | Distinguir método/escopo; testar falhas e integrações em sandbox |
| D-12 | Prompt/agente e fontes externas | Instrução importada pode ampliar permissões | Tratar conteúdo como dados; execução de extensão exige capacidade declarada |

As lacunas têm origem nesta análise, finalidade de prontidão para extração, dependências nos componentes citados e comprovação limitada ao catálogo. Não são funcionalidades implementadas. Cada uma está detalhada também no inventário e no backlog. Algumas dependem de decisão ou autorização externa, não de correção técnica imediata.
