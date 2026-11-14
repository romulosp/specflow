# SpecFlow CLI

Copyright (c) 2026 **Rômulo Penha**. Licença MIT para este pacote autoral.

CLI local para preparar projetos, recuperar contexto e verificar gates de um processo Spec Driven próprio. O agente no editor executa especificação, implementação e revisão; o terminal não chama IA automaticamente. `phaseExecuted=false` significa que preparar a instrução não concluiu a fase.

## Instalação local

Python >=3.11. Uv é recomendado, não obrigatório; o wheel também é um pacote Python padrão instalável em ambiente isolado.

```powershell
uv tool install .\dist\specflow_cli-0.1.0-py3-none-any.whl
specflow --version
specflow init meu-projeto --integration copilot
cd meu-projeto
specflow doctor
specflow nova-change "Criar cadastro de clientes"
```

Execute a instalação a partir do diretório que contém dist. Para as duas integrações, repita `--integration codex`. Em consumidor existente, use `specflow init .`; mesma versão permite acrescentar integração sem resetar configurações. Atualizar o pacote não aplica upgrade nos consumidores.

`doctor` considera opcionais em DEFINIR como inativos, sem executar probes. O arquivo configuracao.properties é sempre criado no init e preservado depois. Qualquer DEFINIR mantém o recurso inteiro inativo. Campos só opcionais no modo declarado podem usar NAO_APLICAVEL. Perfis none/basic/token validam configuração, sem certificar API ou versão de serviço externo.

## Comandos

- `init`, `doctor`, `nova-change`: estrutura, configuração e rascunhos.
- `contexto` (alias `context`), `check`, `evaluate`: leitura determinística e gates, sem aplicar transições.
- `especificar`, `esclarecer`, `revisar-spec`, `planejar`, `implementar`, `teste-humano`, `revisar-implementacao`, `validar`, `aprovar`, `encerrar`: instruções para o agente e verificação de suas pré-condições.

Fases recebem `--change ID`. check/evaluate exigem `--target ESTADO`. `--project` seleciona raiz explícita; `--json` produz saída estruturada. Flags comuns podem vir antes/depois do subcomando; valores conflitantes são rejeitados. `--help` e `--version` não exigem projeto. Também disponível via `python -m specflow` no ambiente Python em que o pacote estiver instalado.

Após nova-change, contexto reconhece RASCUNHO. O agente completa os quatro documentos, manifesta seus hashes e converte explicitamente draft.json em change.json; os dois simultâneos são conflito. Não há comando para inventar aprovação humana. O formato dos registros é descrito nos recursos instalados e validado pelas bibliotecas fechadas de domínio.

## Gates e limites

SPEC_APROVADA humana corrente e plano precedem código. Aplicações são geradas abaixo de apps e preservam arquivos existentes. A implementação exige suíte aprovada e cobertura atual mínima de 80% por arquivo/agregado, meta 90%, aceitando valores maiores. Evidências de implementação vinculam contrato + build por targetManifest; a entrega vincula o build em artifactManifest. Mudanças em contrato, testes, logs ou relatórios invalidam os registros dependentes.

`validar` executa o gate confiável de segurança quando a revisão da implementação permite, sem executar command do JSON. Qualquer achado aberto ou prova insuficiente bloqueia. Os bindings de evidência são necessários além do código 0 do gate. Aprovação, execução das fases e encerramento não são consequências automáticas de um comando ou de testes verdes.

O lock coordena escritores conformes; um editor externo pode causar conflito/WRITE_PARTIAL, sem rollback destrutivo. Recuperação de lock abandonado é ação explícita do operador. O produto verifica consistência, não autentica pessoas nem garante a verdade de evidências. Não importa código do consumidor nem inicializa infraestrutura. Extensões incompletas/direitos desconhecidos e material de pesquisa não integram esta distribuição.

Compatibilidade e descoberta de comandos nos clientes só são homologadas por evidência do ambiente executado; testes unitários e arquivos presentes não certificam Linux ou interface de editor. Publicação e aceite humano do build são etapas separadas.
