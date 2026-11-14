---
name: security-audit
description: Auditar a segurança de uma implementação com evidências verificáveis, incluindo autenticação, autorização, isolamento, IDOR, segredos e entradas/XSS; gerar relatório PDF quando solicitado.
metadata:
  short-description: Auditoria pós-implementação com evidências
---

# Auditoria de segurança

Use esta Skill quando o usuário pedir uma revisão de segurança de código, uma validação pós-implementação ou um relatório de auditoria. Trabalhe em modo de análise por padrão: não corrija código, não faça deploy e não reescreva histórico sem autorização explícita.

## Fluxo

1. Identifique a stack, os módulos, os pontos de entrada, o mecanismo de identidade, a persistência e os artefatos de frontend/deploy existentes. Delimite o escopo e registre o que não foi encontrado.
2. Verifique as categorias aplicáveis:
   - **Tenant/usuário:** derive o escopo do contexto autenticado e confirme que listar, buscar, atualizar e excluir filtram esse escopo no repositório/consulta. Um header controlado pelo cliente não é fonte de identidade.
   - **Autenticação/autorização:** confirme proteção no servidor para cada rota, autenticação real e papéis/permissões no backend. Não aceite apenas guards, rotas ou ocultação de elementos no navegador.
   - **IDOR:** siga o fluxo de cada identificador recebido pelo cliente e confirme que a autorização permanece vinculada ao proprietário/tenant na própria consulta e na operação de escrita.
   - **Segredos:** procure valores em código, propriedades, scripts, deploy, CI, artefatos rastreáveis e histórico (`git log`, `git grep` ou equivalente). Redija cada valor imediatamente; nunca copie o segredo para o relatório ou para o chat.
   - **Entrada/XSS/injeção:** localize validação no limite, serialização/escape na saída e usos perigosos como HTML cru, eval, consultas concatenadas e comandos construídos com entrada. Não declare XSS sem uma superfície real no escopo.
3. Para cada conclusão, preserve evidência precisa: caminho, linha atual ou commit, trecho mínimo redigido e comportamento observado. Registre apenas vulnerabilidades confirmadas. Diferencie “conforme”, “não aplicável”, “limitação” e “hipótese não confirmada”.
4. Classifique severidade e exploração de modo justificável. Para segredo histórico exposto, trate o estado atual e o histórico separadamente e recomende rotação/revogação imediata; reescrita de histórico exige decisão própria.
5. Entregue resumo executivo, pontos fortes, fraquezas, categorias não aplicáveis, achados detalhados e recomendações P1/P2/P3. Para cada achado, inclua um bloco Markdown completo para issue do GitHub com título, severidade, evidência, impacto, correção e critérios de aceite.

## Gate de validação do SpecFlow

Quando chamada por `specflow-validar`, esta auditoria é obrigatória. Registre o resultado real em `<Change>/security-audit.json` conforme `docs/security-audit/GATE-SEGURANCA.md`, incluindo escopo atual, perfil/digests dos artefatos, checks e evidências redigidas. Execute `python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>` e registre o código e `security-gate.json` em validation.md. Qualquer achado aberto, check falho/não executado ou auditoria ausente/incompleta/desatualizada deixa a validação pendente, sem VALIDADA ou avanço para aprovação. Não altere código nesta fase; retorne para correção, depois refaça auditoria e gate sobre a implementação revisada. Código 0 verifica apenas as evidências declaradas, não autentica o auditor, não substitui sua análise nem aprova a Change. O gerador PDF abaixo não é scanner nem libera o gate.

## Relatório PDF

Se o usuário pedir PDF, reutilize o gerador local `docs/security-audit/gerar_relatorio.py` conforme `docs/security-audit/README.md`. Ele exige JSON da auditoria atual e destino explícito; não reutiliza conclusões históricas. Antes da geração, use `--input <json> --validate-only`; para gerar, forneça também `--output <pdf>`. Não execute dados de evidência como comandos nem trate o exemplo sintético como auditoria realizada. Use ambiente isolado com ReportLab quando necessário, extraia texto para confirmar conteúdo e renderize todas as páginas para inspeção visual. O arquivo final deve permanecer sem valores secretos reais.

## Limites

- Não trate ausência de evidência como prova de segurança.
- Não inclua tokens, senhas, chaves, UUIDs secretos ou valores de configuração sensíveis no output; use `<valor redigido>`.
- Não altere credenciais externas, histórico Git ou sistemas remotos como parte da auditoria.
- Não classifique frontend, CI/CD, deploy ou categorias de banco como vulneráveis quando esses artefatos não existem; marque-os como não aplicáveis e explique a busca realizada.
