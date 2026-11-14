# Plano de implementa??o ? CLI r2

SPEC_APROVADA: evidence/spec-approval-r2.json, com contratos dependentes aprovados. Nenhum documento aprovado ser? reescrito; progresso separado.

1. Reutilizar bibliotecas do n?cleo e do consumidor depois de seus testes locais; argparse fino, erros sem argv sens?vel, JSON e entrada de console/m?dulo equivalentes.
2. Usar cat?logo autoral ?nico para comandos de editor, pol?tica, templates e protocolo/gate de seguran?a. Recursos via importlib.resources, sem copiar extens?es incompletas/direitos desconhecidos.
3. Testar init/doctor/nova-change, integra??o aditiva, handoff e gates, seguran?a/bindings e c?digos 0/1/2, inclusive falhas e conflitos.
4. Medir cobertura por arquivo e agregado; bloquear conclus?o se abaixo de 80%. Ferramentas de build/teste isoladas e fixadas em docs/cli/build-tools.lock.
5. Gerar wheel/sdist em dist/ na raiz, reconstruir wheel do sdist e executar smoke com ambiente/perfil tempor?rio; testar o caminho uv tool install sem afetar ferramentas pessoais. N?o publicar.
6. Registrar revis?o, auditoria e evid?ncias reais, atualizar guia/quickstart com build/hash. Deixar teste humano, homologa??o de clientes/Linux n?o executada e aceite final explicitamente pendentes quando indispon?veis.

Lock/preflight/rollback e parser de propriedades s?o os da 10030, sem duplica??o. N?o executar agentes/servi?os no CLI. Gate de seguran?a executa c?digo confi?vel do pacote e os campos de evid?ncia nunca s?o shell. Testes Windows locais s?o reproduz?veis; n?o iniciar Docker/infraestrutura para fingir compatibilidade Linux.
