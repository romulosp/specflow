# Tarefas — SpecFlow CLI r2

Status EM_REVISAO_SPEC. Nenhuma tarefa de implementação iniciada.

| ID | Estado | Entrega | Dependência / aceite |
| --- | --- | --- | --- |
| P01 | preparada | proposta, SPEC, design, tarefas e manifesto r2 | plano solicitado pelo usuário; sem aprovação de SPEC inferida |
| G01 | pendente humana | decisão SPEC_APROVADA vinculada ao manifesto r2 | P01 e revisão técnica corrente |
| G02 | pendente técnica/humana | núcleo 10029 r6 e consumidor 10030 r4 entregues e validados para integração | contratos próprios aprovados e evidências; sem herança de aprovação |
| T01 | não iniciada | implementation-plan e build/test tools fixados em ambiente isolado | G01 e contratos dependentes aprovados; plano pode anteceder entrega das bibliotecas, sem código antecipado |
| T02 | não iniciada | parser, entry points, versão, envelopes e erros | T01; CLI-01/08/15 |
| T03 | não iniciada | assets autorais e adaptação de init/configuração/integrações | T02/G02; CLI-02..06/09/16/20; não duplicar protocolo da 10030 |
| T04 | não iniciada | rascunhos e reserva concorrente de IDs | T03; CLI-07 |
| T05 | não iniciada | comandos de fase/handoff e mapeamento de gates | T02..04; CLI-08..11/13/14 |
| T06 | não iniciada | validar, gate confiável e verificação de bindings atuais | T05; CLI-12/13/21; gate 0 sem evidenceManifest não basta |
| T07 | não iniciada | testes funcionais/negativos e cobertura atual por arquivo/agregado | T02..06; CLI-18 e todos os CA aplicáveis |
| T08 | não iniciada | wheel/sdist e smoke de instalação/atualização isolada | T07; CLI-01/02/16/19 |
| T09 | não iniciada | guia de comandos, diagrama e quickstart vinculados ao build | T08; CLI-09/19 |
| T10 | não iniciada | revisão da implementação e correções rastreáveis | T07..09; nenhum achado material aberto |
| T11 | não iniciada | validação padrão, auditoria real/gate e Windows/Linux | T10; CLI-12/17/18 |
| G03 | pendente futura | descoberta/invocação em clientes e teste humano do build | T08..11; CLI-17/19; resultados observados, sem simulação |
| G04 | pendente humana | aceite final da mesma revisão | G03 e validação suficiente; publicação não incluída |

Não marcar T07 por checks de sintaxe ou por teste de suporte antigo. Se ambiente Linux/cliente não estiver disponível, registrar not_run e manter o critério pendente. Instalação local para smoke usa perfil/ambiente temporário; não instalar na configuração pessoal do usuário implicitamente.
