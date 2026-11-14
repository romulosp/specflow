# Auditoria de seguranca

A [skill autoral security-audit](../../.agents/skills/security-audit/SKILL.md) orienta a analise real. O [gate de seguranca](GATE-SEGURANCA.md) verifica os registros e digests dessa analise; nao executa scanner ou comandos contidos no JSON. Execute `python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>` depois de produzir uma auditoria atual. Qualquer achado aberto ou evidencia incompleta bloqueia a validacao.

O antigo gerador PDF incorporado, seus recursos de referencia e exemplos de ADR foram retirados do checkout publico por direitos pendentes. As copias permanecem no acervo local do titular; nao sao capacidades disponiveis de um clone publico. PDF e opcional e nunca substitui auditoria ou gate. Gerar um novo exportador autoral exige escopo e contrato aplicaveis.

Os recibos da retirada e dos arquivos autorais substitutos estao em [inventario-retirada-acervo.json](../release/inventario-retirada-acervo.json). Alteracoes atuais nao removem historico nem releases anteriores. Consulte [CHECKOUT-PUBLICO.md](../release/CHECKOUT-PUBLICO.md) para distinguir verificacao publica de integridade do acervo local.
