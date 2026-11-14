# Revisão técnica — CLI r1

13/11/2026. Revisão do executor, sem independência humana. Manifesto em ../evidence/contract-r1.json. Parecer documental favorável para decisão humana, sem SPEC_APROVADA.

| Achado | Severidade / estado | Evidência e impacto | Tratamento |
| --- | --- | --- | --- |
| REV-001 | material / resolvido no contrato | Confundir terminal e agente poderia fabricar conclusão; CLI-09..11/14 | CLI prepara handoff com phaseExecuted=false, aplica pré-condições e não chama IA ou grava aprovação |
| REV-002 | material / resolvido no contrato | init em projeto existente pode perder configurações; CLI-04/05 | Plano de escrita, conflitos prévios, preservação de configurações/AGENTS e limites de rollback/concorrência explícitos |
| REV-003 | material / resolvido no contrato | JSON/arquivos de consumidor poderiam executar comandos; CLI-06/12 | Gate confiável empacotado, root explícito, sem shell/importar scripts do consumidor e sem executar command |
| REV-004 | material / resolvido no contrato | Copiar todo acervo distribui recursos incompletos/direitos desconhecidos; CLI-02/19 | Allowlist autoral/liberada, protocolo autoral de segurança e inventário de wheel/sdist; arquivos de pesquisa fora do produto |
| REV-005 | material / resolvido no contrato | Instalação e descoberta não são provadas por arquivo presente; CLI-01/17 | Wheel instalado/reconstruído, cenários reais Windows/Linux e clientes com versões/evidências; indisponibilidade not_run |
| REV-006 | material / resolvido no contrato | Cobertura agregada pode ocultar arquivo não testado; CLI-18 | Piso por arquivo e agregado, meta 90%, sem teto, evidência atual vinculada ao manifesto |

Nenhum achado documental material aberto identificado. Os tratamentos acima são obrigações especificadas, não correções de um runtime já existente. Compatibilidade, cobertura, segurança, instalação e homologação ainda não executadas. A recomendação não promove estado, não autentica futuro revisor e não substitui decisão humana dos três contratos.
