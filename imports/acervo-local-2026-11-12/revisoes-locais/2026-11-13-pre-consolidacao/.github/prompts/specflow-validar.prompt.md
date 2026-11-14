---
description: "Comando padrao da fase de validacao da implementacao, omitido apenas por prompt explicito; exige security-audit e gate de seguranca sem achados ou pendencias."
argument-hint: "Informe objetivo ou caminho da Change"
agent: agent
---

# specflow-validar

Fase: 5. Validacao

Entrada: Change em IMPLEMENTACAO_APROVADA, criterios de aceite e ambiente conhecido.

Saida: validation.md com VAL e evidencias tecnicas; security-audit.json e security-gate.json atuais. Seguranca pendente impede VALIDADA e nao permite avancar para aprovacao.

## Procedimento

1. Este e o comando padrao quando um fluxo autorizado alcancar a fase de validacao da implementacao; nao exija nova solicitacao rotineira do usuario. Se o prompt do usuario pedir explicitamente nao executar essa fase ou limitar o fluxo antes dela, nao execute seus checks: registre em validation.md e na memoria a revisao, a solicitacao, o motivo e a fase nao executada, mantenha os gates posteriores pendentes e pare sem VALIDADA ou aprovacao. Nao infira dispensa de silencio, falha, ferramenta ausente ou pedido para nao gerar PDF. Esta regra nao amplia comandos de fase unica nem ultrapassa a parada do teste-humano.
2. Confirme IMPLEMENTACAO_APROVADA da revisao corrente. Use implementation-validate para executar cenarios aplicaveis e registrar comandos, codigos e limites, sem concluir VALIDADA antes de satisfazer o gate de seguranca abaixo.
3. Chame obrigatoriamente a skill local security-audit: analise a implementacao atual, execute verificacoes de seguranca aplicaveis autorizadas e registre escopo, findings, checks, limitacoes e manifesto dos artefatos em <Change>/security-audit.json conforme docs/security-audit/GATE-SEGURANCA.md. Nao copie resultados do exemplo ou gere conclusoes favoraveis por ausencia de relatorio.
4. Execute obrigatoriamente python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>. Este verificador confere evidencias e digests da auditoria; o gerador gerar_relatorio.py apenas formata PDF e nao o substitui. Registre comando, codigo e security-gate.json em validation.md.
5. Somente codigo 0 com status verificada permite considerar o gate de seguranca satisfeito. Qualquer achado aberto, check falho/nao executado, auditoria ausente/incompleta/desatualizada, erro do script ou dependencia indispensavel ausente deixa seguranca e fase de validacao pendentes. Nao escreva VALIDADA nem avance para specflow-aprovar enquanto isso persistir; informe IDs, impacto e condicao de desbloqueio sem expor segredos.
6. Nao corrija codigo durante a validacao. Encaminhe os problemas para implementacao ou SPEC conforme a causa; depois da correcao, exija revisao tecnica atual, nova auditoria sobre os artefatos atuais e nova execucao do gate. Achados resolvidos exigem evidencia; nao basta renomear status para liberar.
7. Disponibilize build/harness real identificado e quickstart verificavel antes de pedir teste manual; resultado humano pendente continua pendente. PDF de auditoria so se solicitado, com dados atuais, extracao de texto e inspecao visual de todas as paginas. Nao aprove ou encerre automaticamente nem execute comandos do JSON de evidencia.

Argumentos fornecidos pelo usuario: ${input:contexto:Objetivo ou caminho da Change}

## Regras locais

Leia AGENTS.md, specs/shared/process/workflow.md e docs/comandos/COMANDOS.md da raiz do projeto. Trabalhe somente neste workspace e mantenha a memoria da Change. Nenhum comando, checkbox, parecer tecnico ou teste verde fabrica decisao humana. Nao execute fases seguintes por este comando nem crie subagentes como efeito colateral.
