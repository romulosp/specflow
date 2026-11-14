# Ajustes técnicos escolhidos e aplicados aos contratos

13/11/2026. Fonte humana: “veja o melhor projeto e resolva”, após solicitar correções antes de aprovar. A escolha técnica foi delegada ao executor; não há detalhes de implementação a devolver ao usuário como perguntas. Contratos resultantes: 10029 r6, 10030 r4 e 10031 r2, ainda EM_REVISAO_SPEC.

## Solução escolhida

Uma distribuição Python specflow-cli, comando specflow, bibliotecas internas de núcleo/consumidor e adaptadores finos de editor. Um catálogo de comandos, uma política de gates e um protocolo de escrita. Não adicionar executor de IA no terminal, três pacotes independentes ou dependência de infraestrutura para inicializar. A estratégia mantém a escolha já feita pelo usuário e reduz divergências. Detalhes e alternativas no [ADR-001 proposto](../adr/ADR-001-cli-local-e-gates.md).

## Achados reais e tratamentos

| ID | Problema anterior | Tratamento contratual | Aceites futuros |
| --- | --- | --- | --- |
| REV-101 | nova-change produz draft que contexto não sabe ler | Núcleo reconhece RASCUNHO antes das sete fases; leitura funciona, avanço continua bloqueado; dois registros conflitantes não são reconciliados silenciosamente | 10029 CA-16; 10031 CA-08 |
| REV-102 | doctor não distingue opcional desligado de instalação quebrada | Consumidor íntegro com DEFINIR retorna 0 e informação; erro de configuração/estrutura retorna 2, conflito/pendência real retorna 1; zero probes externos | 10031 CA-06/15 |
| REV-103 | Reinit aditivo conflita com atualização esperada dos próprios metadados | Acrescentar integração explícita da mesma versão é permitido; bytes autorais e configuração preservados; upgrade continua separado | 10030 CA-I08; 10031 CA-20 |
| REV-104 | Preflight/rollback sem lock e escrita direta podem perder alterações concorrentes ou seguir links | Um lock compartilhado; create exclusivo para novo, compare + temporário/replace para atualização permitida; rollback só sobre bytes ainda próprios; destinos portáteis sem links | 10030 CA-I08/A03; 10031 CA-20 |
| REV-105 | Gramática de properties indefinida pode interpretar senha/path/escapes de forma diferente | UTF-8, primeiro =, backslash e credencial literais, sem interpolação/continuação; duplicatas e chaves desconhecidas falham de forma fechada | 10030 CA-I07 |
| REV-106 | Presença de arquivo de evidência e gate v1 0 não vinculam todos os bytes citados | Manifestos de testes/relatórios/evidenceRefs, comparação dos bytes e política fixada; helper atual não é anunciado como já endurecido | 10029 CA-15; 10031 CA-21 |
| REV-107 | Dependência de entrega completa antes de qualquer plano do CLI confunde plano e integração | Plano após contratos aprovados; integração exige bibliotecas entregues/validadas; não duplicar núcleo e escrita no CLI | 10031 T01/G02/T03 |

Os 55 checks documentais anteriores conferiam estrutura, links e hashes, não provavam ausência dessas inconsistências semânticas. Pareceres favoráveis anteriores pertencem às respectivas revisões, não a estas novas. Nenhum item acima é alegado como código corrigido ou comportamento já executado.

## Preservação e próxima etapa

Revisões anteriores exatas em evidence/revisions/r5, r3 e r1 de suas Changes, com cópia do manifesto e índice de hashes. Manifestos correntes identificam somente os novos quatro documentos. Memória e fonte da delegação preservadas; não fabricar aprovação, cobertura, auditoria ou homologação.

Os ajustes técnicos estão resolvidos para revisão. O gate humano de SPEC_APROVADA continua necessário antes de código porque foi mantido expressamente pelo usuário no plano e nas regras anteriores. Aceite do build e publicação permanecem separados.
