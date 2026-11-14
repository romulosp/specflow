# Plano de implementa??o ? consumidor r4

SPEC_APROVADA: evidence/spec-approval-r4.json; documentos aprovados preservados. N?cleo exercitado em Windows: evidence/core-local-checkpoint.json da 10029 (20 testes, 94% de cobertura agregada e piso por arquivo). Esse checkpoint permite integrar as APIs locais; n?o certifica Linux, cliente ou aceite final.

1. Parser properties estrito e cat?logo autoral de 25 campos; todos come?am DEFINIR, sem rede/processo/sondagem. Testar credenciais e paths literais, duplicatas, Unicode e autentica??o opcional declarada.
2. Uma camada fileops de lock, preflight, cria??o exclusiva, compare/replace e rollback conservador. Testar conflitos, falha intermedi?ria, hardlink, reparse point/junction e escritor concorrente.
3. Init com ownership, preserva??o autoral e integra??es aditivas da mesma vers?o; ignore idempotente, metadados sem autorrefer?ncia/segredos. N?o copiar extens?es incompletas.
4. nova-change com reserva persistente de IDs e draft; gera??o de aplica??o confinada com SPEC/plano/escopo autorizado, usando as mesmas bibliotecas de guarda/escrita.
5. Testes de comportamento com diret?rios tempor?rios, medi??o coverage.py (piso 80% por arquivo/agregado, meta 90%), relat?rio atual e revis?o/auditoria locais. N?o marcar homologa??o Linux/clientes ou aceite humano sem execu??o real.

Ferramentas isoladas e vers?es em docs/cli/build-tools.lock; nenhum componente global/servi?o ser? instalado/iniciado. Progresso em task-progress.json, sem alterar tasks.md aprovado. Pacote/CLI da 10031 reutilizam estas APIs; limita??es dos checkpoints ficam explicitamente pendentes na valida??o global.
