# Revisão técnica recebida — SPEC r1

Fonte: mensagem do usuário nesta conversa, 2026-11-12. Síntese fiel dos achados; não atribuir autoria independente ou identidade de revisor não informada. Alvo: contrato r1 preservado em `../evidence/HISTORICO-ARQUIVADO.md/`, com hashes originais em `../evidence/contract-r1.json`.

Veredito recebido: favorável sob o ponto de vista arquitetural e de engenharia, condicionado à pacificação da normalização de encoding/newline; o texto menciona consideração dos achados antes da aprovação humana final. Não constitui aprovação humana irrestrita do novo contrato r2.

| ID | Achado recebido | Tratamento documental na r2 | Estado |
| --- | --- | --- | --- |
| REV-01 | Hash byte a byte pode invalidar aprovação por troca LF/CRLF entre plataformas | RF-04 e design definem sha256-utf8-lf-v1 para contrato, UTF-8 estrito, BOM inicial opcional, LF/CRLF/CR equivalentes; sha256-bytes-v1 para integridade binária; perfil integra vínculo | incorporado; execução futura em T03/T08 |
| REV-02 | Validação completa com stdlib exige esforço explícito | RF-01, RNF-01, design e T03 fixam validadores customizados por registro, sem motor JSON Schema genérico; tipos estritos e chaves duplicadas | incorporado; execução futura em T03/T08 |
| REV-03 | Contexto indeterminado precisa de código inequívoco | RF-06 explicita 1 para conflito/pendência obrigatória, 2 para erro e 0 para reconciliado; design já previa 1, agora com prioridade formal | clarificado; execução futura em T07/T08 |
| REV-04 | Encerramento por recibo posterior resolve circularidade de commit | Mantida fase 7; avaliação sintética, sem commit/archive executados | avaliação positiva preservada |
| REV-05 | Classificar evidência por metadados, sem heurística de texto | RF-08 e design exigem enums method/requiredMethod e igualdade; método ausente/desconhecido = 2, incompatível = 1 | incorporado; execução futura em T06/T08 |

Digest canônico deixa de ser prova de igualdade byte a byte do texto; rawSha256 opcional preserva a distinção para auditoria. Não equivale a assinatura, autenticação ou Zero Trust completo. Sem fallback de encoding, trim ou normalização semântica. Modificar conteúdo canônico continua invalidando aprovação.

Tratamento feito pelo executor. Não houve nova revisão independente de r2 nem teste funcional. Gate humano G02 permanece pendente.
