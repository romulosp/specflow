# Change 10030 — Inicializar consumidor, configurar recursos e gerar apps

Status: `EM_REVISAO_SPEC`. Revisão r4, 13/11/2026. Aprovação humana da SPEC: pendente.

## Pedido e objetivo

O usuário determinou que a inicialização sempre crie um arquivo .properties com valores DEFINIR, centralizando URLs e credenciais dos recursos; enquanto houver DEFINIR, o recurso não deve ser utilizado. Também determinou que geração de código crie a pasta apps do projeto consumidor.

Esta Change prepara o contrato dessas capacidades para o incremento de inicialização. Não implementa init, não cria configuração real ou apps neste workspace, não migra consumidores e não herda aprovação da investigação ou do núcleo. As diretrizes foram dadas; esta revisão técnica ainda precisa de aceite antes de código.

## Escopo

R4 fecha a gramática de properties, a inclusão aditiva de integrações da mesma versão e o protocolo único de escrita/rollback. Nomes e colisões Windows/Linux são validados antes da gravação. Detalhes técnicos foram resolvidos pela delegação do usuário, sem converter essa delegação em SPEC_APROVADA. Ver [ajustes](../../../docs/cli/AJUSTES-TECNICOS.md).

- Inicialização independente de integrações preenchidas, com `configuracao.properties` privado e template sem credenciais reais.
- Catálogo declarativo de propriedades por recurso; estado inativo para DEFINIR ou configuração incompleta.
- Preservação de configurações e apps existentes em chamadas repetidas.
- Geração de aplicações em `<raiz-consumidor>/apps/`, somente com SPEC_APROVADA da Change que autoriza gerar código.
- Gate de recursos em todas as entradas de execução, sem dispensar cobertura/segurança obrigatórias quando um recurso necessário estiver inativo.

Fora de escopo: instalar/executar Sonar, Docker, scanners ou stacks; publicar; migrar aplicações; liberar terceiros; estabilizar todos os 104 perfis/Skills como adaptadores funcionais. Cada extensão deve declarar propriedades e capacidades antes de poder executar recursos.

## Dependências e prontidão

O núcleo da Change 10029 r6 ainda está em revisão. Esta r4 consome seus manifestos, cobertura, segurança e registros de execução/entrega; implementação integrada depende da entrega validada desses contratos no núcleo. O arquivo properties concentra endpoints/credenciais, enquanto project.json guarda identidade, política e caminhos. Esta proposta não amplia o primeiro incremento para incluir todo o MVP.

## Decisões propostas para revisão

Nome ASCII `configuracao.properties`, formato UTF-8 e localização na raiz do consumidor. Campo opcional não aplicável poderá usar NAO_APLICAVEL somente quando o adaptador declarar que o campo é dispensável no modo de autenticação selecionado; nenhum DEFINIR é ignorado silenciosamente. Essa resolução de autenticação opcional é proposta técnica, não afirmação de capacidade de um Sonar/serviço específico.

Contrato: [SPEC](spec.md), [design](DESIGN.md), [tarefas](tasks.md), [validação](validation.md). Políticas: [regras consolidadas](../../shared/process/regras-consolidadas.md), em especial SF-31..36. Exemplo de propriedades: [template](configuracao.example.properties), sem implementação ou dados reais.
