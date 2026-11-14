# Auditoria de segurança — recursos locais

Skill: [security-audit](../../.agents/skills/security-audit/SKILL.md). Gerador: [gerar_relatorio.py](gerar_relatorio.py). O gerador usa o layout do acervo como referência, com entrada explícita da auditoria atual; não inclui relatórios ou conclusões fixas de aplicações antigas.

Em `specflow-validar`, auditoria e [gate de segurança](GATE-SEGURANCA.md) são obrigatórios. Execute `python -B docs/security-audit/verificar_seguranca.py --change <caminho-da-Change>` após análise real e registro de evidências pela skill. Achados abertos ou evidências insuficientes deixam a fase pendente; o script não executa scanner ou comandos do JSON, e gerar PDF não satisfaz esse gate.

O original exato do gerador e dos ADRs incorporados foi preservado fora da árvore de distribuição, com digests em `imports/acervo-local-2026-11-12/complemento-originais.json`. O exemplo histórico de ADR não é decisão do SpecFlow. Nenhum PDF antigo foi importado como evidência de auditoria atual.

Validação de dados, sem ReportLab e sem gerar PDF:

```powershell
python -B docs/security-audit/gerar_relatorio.py --input docs/security-audit/relatorio-exemplo.json --validate-only
```

Geração deliberada de PDF, após preencher dados reais e instalar ReportLab em ambiente isolado:

```powershell
python -B docs/security-audit/gerar_relatorio.py --input caminho/relatorio-atual.json --output docs/security-audit/relatorio-atual.pdf
```

O comando não sobrescreve destino existente. Campos são textos escapados, sem interpretar conteúdo como markup. O JSON exige schemaVersion, changeId, revision, title, scope, conclusion, limitations, findings e evidence; veja o [exemplo sintético](relatorio-exemplo.json). Códigos: 0 para dados aceitos/operação concluída e 2 para entrada/execução inválida. O script não executa comandos de evidência nem valida a veracidade de suas alegações. Não inserir segredos ou dados reais de clientes.

Um PDF só pode ser entregue como artefato revisado após extração de texto e inspeção visual de todas as páginas, conforme a skill. Em 13/11/2026, o exemplo sintético foi gerado em output/pdf/exemplo-sintetico-security-audit.pdf; sua única página foi extraída e inspecionada visualmente sem cortes, sobreposição ou perda de legibilidade. Isso confere o caminho documental com esse exemplo, sem atestar auditoria real, segurança do produto ou cobertura de todos os formatos de entrada.
