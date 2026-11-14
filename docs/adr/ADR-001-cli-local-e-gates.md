# ADR-001 — CLI local, bibliotecas compartilhadas e gates verificáveis

Status: PROPOSTO. Data: 13/11/2026. Responsável técnico: executor delegado pelo usuário.
Changes e revisões: 10029 r6, 10030 r4, 10031 r2. Aprovação humana dos contratos: pendente.

## Contexto

O usuário pediu corrigir os contratos e depois delegou a escolha da melhor solução. Nome specflow-cli/specflow e CLI com agente no editor já foram escolhidos. A revisão identificou lacunas concretas entre rascunho/contexto, semântica do doctor, escrita aditiva de integrações, leitura de propriedades e integridade de evidências. O CLI ainda não existe, portanto os tratamentos são contratuais, não resultados de runtime.

## Alternativas

- Um único pacote Python com CLI fino e bibliotecas internas: reaproveita política/validação, reduz divergência e mantém runtime com stdlib. Escolhido como proposta técnica.
- Separar núcleo/consumidor/CLI em três distribuições: acrescenta publicação e matriz de versões sem necessidade demonstrada. Não adotado para 0.1.0.
- Embutir um executor de IA e infraestrutura no terminal: amplia credenciais/permissões e contradiz a opção de agente no editor. Fora da versão inicial.

## Decisão proposta

1. Manter uma distribuição e três contratos de responsabilidade. Aprovação de contrato não significa aceite do build; nenhuma approval é fabricada pelo CLI.
2. Reconhecer RASCUNHO no núcleo antes das sete fases, com contexto utilizável e avanço bloqueado até contrato completo. Não criar uma oitava fase.
3. doctor diferencia opcional inativo de erro, sem executar recursos. Gramática de properties é explícita e preserva senha/caminho literal.
4. Compartilhar um protocolo de lock/preflight/commit/rollback. Init aditivo da mesma versão pode acrescentar integração sem reescrever material autoral. Atualização de produto permanece fora da versão inicial.
5. Vincular evidências, testes, relatórios e política por manifestos/digests; gate legado 0 isolado não prova atualidade do conjunto. A escrita do gate será confiável, confinada e por replace.
6. Validar nomes/colisões Windows/Linux e recusar links de escrita. Documentar limites diante de editor externo e controle malicioso da instalação, sem alegar autenticidade/atomicidade que não existem.

## Consequências

Novos contratos eliminam decisões técnicas deixadas ao implementador, sem exigir novas escolhas do usuário sobre detalhes internos. Testes futuros precisam demonstrar concorrência/rollback, draft/contexto, configuração literal e evidência adulterada; critérios Windows/Linux, clientes, cobertura e auditoria não foram dispensados. Código só depois de SPEC_APROVADA dos contratos correntes; publicação continua separada.

## Proveniência e substituição

Fonte humana: “veja o melhor projeto e resolva”, após solicitar ajustes antes de aprovar. Delegação técnica não foi convertida em aceite humano dos novos contratos. Revisões anteriores preservadas localmente em evidence/revisions de cada Change. ADR substituído: nenhum. Promover a ACEITO somente com decisão humana explícita.
