# Pendências do SpecFlow

Marco autoritativo de 14/11/2026: SPEC10032r1 aprovada; publicacao autorizada e concluida. specflow-cli0.1.0 no PyPI, hashes e instalacao nominal verificados (15 operacoes). CI real Windows/Linux Python3.11/3.14 passou. Objetivo uv tool install specflow-cli atendido. Nao pedir novamente aprovacao das SPECs/publicacao. Memoria atual em specs/changes/10032-publicar-specflow-cli-pypi/AGENTS-MEMORY.md. Pendencias antigas de conta/upload/Linux sao historicas; descoberta nos clientes e aceite humano final do produto permanecem separados.

Marco posterior de 14/11/2026: o usuario autorizou todo trabalho necessario para instalacao por nome uv tool install specflow-cli, incluindo preparar a publicacao. Change ativa 10032-publicar-specflow-cli-pypi r1: proposta/SPEC/design/tarefas/manifesto e revisao documental preparados. A autorizacao de publicacao ja foi dada; nao perguntar novamente. SPEC_APROVADA deste novo contrato ainda pendente, antes de workflow/codigo. Conta/publisher PyPI ainda nao demonstrados. Nao declarar comando nominal disponivel antes do upload verificado. Contratos anteriores permanecem congelados; objetivo atual e publicacao controlada sem acervo/segredos, com CI e teste real pelo indice.

Estado corrente em 14/11/2026: SPECs 10029 r6, 10030 r4 e 10031 r2 aprovadas pelo usuário; implementação local entregue em `framework/` e `dist/`. [Fonte humana](docs/cli/aprovacao-humana-2026-11-13.json), [entrega verificável](docs/cli/ENTREGA-0.1.0.md).

| Item | Situação e condição de fechamento |
| --- | --- |
| Diagnóstico, arquitetura e contratos | Aceitos no escopo do pacote de decisão. Não solicitar novamente. Aceite final e publicação continuam separados |
| Núcleo, configuração, apps e CLI | Implementados; testes funcionais/negativos e cobertura atuais. Geração de aplicação é API local com gate; o terminal orienta o agente e não gera uma aplicação automaticamente |
| Windows e pacote | Testados com Python 3.14.6; wheel construído a partir do sdist, instalado e reinstalado em ambiente isolado. Compatibilidade mínima declarada Python >=3.11; outras versões ainda não exercitadas |
| Linux | not_run. Sem ambiente Linux geral utilizado. Executar testes e instalação em Linux antes de concluir CLI-17; não iniciar infraestrutura para simular homologação |
| Copilot/Codex | Arquivos instalados e vínculos conferidos. Descoberta/invocação visual nos clientes reais continua not_run; registrar cliente, versão, build e resultados |
| Teste humano e aceite final | Executar roteiro da entrega e registrar observações. Não existe decisão final sobre este build. Sem APROVADA, archive, commit ou publicação automática |
| Segurança | Auditoria e gate locais registrados nas Changes. Código 0 comprova somente consistência das evidências declaradas. Validação global permanece pendente |
| Extensões opcionais | 146 pares documento/destino ausentes em 30 diretórios do acervo. [Lista](imports/acervo-local-2026-11-12/dependency-resolution.json). Fora do pacote; recuperar recursos legítimos ou desenvolver capacidade em Change própria |
| Direitos, marca e distribuição pública | Material autoral MIT. Direitos desconhecidos excluídos. Disponibilidade de nome/marca e publicação pública exigem verificação e decisão próprias |
| Helpers históricos | Cobertura do produto mede os arquivos novos de framework/src/specflow, inclusive o wrapper distribuído. Não certifica cobertura universal dos helpers antigos |

Os resultados documentais anteriores (52 checks, dossiê 36/0 e suporte 10 testes) são históricos e não substituem os testes atuais. Nenhum checkout externo ou original preservado foi modificado nesta implementação.