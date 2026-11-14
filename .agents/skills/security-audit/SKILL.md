---
name: security-audit
description: Auditar a implementacao atual e registrar evidencias verificaveis de seguranca na validacao SpecFlow.
license: MIT
metadata:
  author: "Rômulo Penha"
---
# Auditoria de seguranca SpecFlow
Leia docs/security-audit/GATE-SEGURANCA.md e a SPEC aprovada. Defina superficie real e arquivos/manifesto antes de analisar.
Confira entradas/JSON/paths/links, permissao de escrita, segregacao por consumidor, segredos/configuracao e execucao de comandos. Em aplicacoes, incluir autenticacao/autorizacao/IDOR/isolamento/XSS quando aplicaveis; justificar nao aplicabilidade.
Execute verificacoes autorizadas e registre comando, codigo, metodo, referencia, achados e limites reais. Recurso em DEFINIR nao e executado; indispensavel indisponivel e pendencia, nunca passed por fallback.
Gere security-audit.json atual, com todos os achados e evidencias. Resolvido exige correcao/reteste. Registre binding dos bytes e execute o gate instalado.
Qualquer achado aberto ou prova insuficiente bloqueia validacao. Nao fabricar aprovacao, executar command do JSON ou gerar PDF sem pedido.
