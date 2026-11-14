# Roteiro de validação futura — Change 10029

## Marco autoritativo - 14/11/2026

O usuario aprovou expressamente: "aprovo as spec vamos proseguir". SPEC_APROVADA de 10029 r6, 10030 r4 e 10031 r2 registrada com fonte/escopo/hashes; nao pedir novamente. Fonte na raiz: docs/cli/aprovacao-humana-2026-11-13.json. Quatro documentos contratuais congelados; approval-state e task-progress registram o estado posterior aos cabecalhos historicos.

Implementacao local autoral entregue em framework/ e dist/: nucleo, configuracao/preservacao, API de geracao em apps e CLI + instrucoes ao agente no editor. 51 testes: 50 aprovados, um skip por permissao de symlink; junction e hardlink reais passaram. Cobertura de linhas 96,68%, todos os arquivos executaveis acima de 80%; branches 92,66%. Build sdist/wheel e 16 operacoes de instalacao/reinstalacao isolada Windows aprovadas, preservando consumidor.

Revisao tecnica local IMPLEMENTACAO_APROVADA; auditoria real e gate de seguranca codigo 0 nas tres Changes, com bindings atuais conferidos pelo nucleo. Validacao global PENDENTE: Linux, descoberta/invocacao Copilot/Codex e teste humano not_run. Sem VALIDADA/APROVADA/encerramento ou aceite final fabricado. Auditor e revisor foram o proprio executor; limites expressos. Nenhuma instalacao pessoal, infraestrutura, publicacao, commit, extracao definitiva ou escrita em checkout externo.

Proxima acao: roteiro humano e evidencias dos ambientes faltantes em docs/cli/ENTREGA-0.1.0.md; apos satisfazer os criterios, repetir apenas checks afetados e solicitar aceite final do mesmo build. Regras e direitos opcionais nao resolvidos continuam em PENDENCIAS.md. Entradas abaixo sao historicas e nao revogam a aprovacao real ou os resultados atuais.

## Roteiro executavel atual

Use docs/cli/ENTREGA-0.1.0.md na raiz para instalar o wheel ou executar o CLI isolado existente. SHA-256 em dist/SHA256SUMS. Cenarios H01..H09 permanecem not_run para o usuario; a tabela antiga abaixo e planejamento historico. Registre build, ambiente, ator, esperado/observado e codigos; nao marque resultado humano a partir de teste automatizado.

## Historico anterior a este marco

Estado: `em_andamento` documental; implementação aguardando SPEC_APROVADA.

Não há harness ou build disponível. As interfaces no [design](DESIGN.md) são propostas, não comandos já verificados. Após implementar, substituir esta seção por caminhos, invocações, pré-requisitos e hashes reais antes de solicitar teste manual. Ambiente isolado e fixtures deverão ser fornecidos prontos, sem edição manual de hashes pelo usuário.

| Cenário | Preparação e ação após implementação | Esperado | Observado |
| --- | --- | --- | --- |
| M01 / CA-02/03 | Avaliar implementação em fixture sem decisão humana de SPEC | Código 1, bloqueio com motivo; nenhum arquivo alterado | não executado |
| M02 / CA-02/03 | Usar fixture com revisão e decisão sintéticas válidas, identificadas como teste | Código 0, allowed=true; não inicia implementação nem promove estado | não executado |
| M03 / CA-04 | Na cópia temporária de M02, alternar LF/CRLF/CR e BOM UTF-8 inicial; depois alterar uma letra ou espaço do conteúdo | Representações equivalentes mantêm digest e permissão; alteração de conteúdo retorna 1 e invalida suficiência da aprovação; UTF-8 inválido retorna 2 | não executado |
| M04 / CA-06/07 | Consultar A com conflito e depois B com marcador privado só em A | A mostra INDETERMINADO e fontes conflitantes; B não expõe marcador de A | não executado |
| M05 / CA-05/08 | Avaliar aprovação final com teste obrigatório falho e depois method structural onde requiredMethod é functional; repetir removendo method | Falha e método incompatível retornam 1; método ausente retorna 2; nenhuma inferência pelo nome do teste | não executado |
| M06 / CA-01/09/10 | Checar JSON inválido, caminho fora da raiz e repetir entrada válida | Inválidos retornam 2 sem leitura externa; repetição válida tem JSON idêntico | não executado |

Build/hash: inexistente. Checks de runtime: não executados. Executor manual/data: pendentes. Aprovação final: pendente. Compatibilidade Linux: não demonstrada. Testar o harness não é testar o funcionamento de aplicações consumidoras.

## Cenários adicionais r4 — ainda não executados

- M07 / CA-12: relatório de cobertura ausente/antigo e valor 79,99% bloqueiam; 80%, 90% e 100% satisfazem só esse gate com suíte e escopo válidos; total zero exige não aplicabilidade justificada.
- M08 / CA-13: auditoria ausente, achado aberto low/info ou script com erro impede VALIDADA.
- M09 / CA-14: pedido de omitir validação registra not_run e impede aprovação; omitir só PDF não dispensa a fase.
- M10 / CA-14: teste humano para em IMPLEMENTADA somente com cobertura e entrega utilizável; cenários humanos permanecem pendentes.
- M11 / CA-15: alterar somente log, teste ou relatório referenciado e depois a política local, mantendo os JSONs antigos; evidência deixa de ser atual e gates não podem ser reduzidos. Campo/perfil malformado retorna 2; divergência válida retorna 1.
- M12 / CA-16: criar draft válido e consultar contexto; obter RASCUNHO/0 sem aprovação. Avaliar avanço retorna 1. Criar change.json sem retirar draft gera INDETERMINADO/1; entrada malformada mantém prioridade 2.
