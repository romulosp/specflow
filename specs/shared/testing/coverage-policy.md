# Cobertura obrigatória na implementação

Regra determinada pelo usuário em 13/11/2026. Aplica-se a toda implementação de código, em qualquer stack, inclusive código escrito por agentes, scripts, validadores, CLI, frontend e backend.

## Limite e escopo

- **Mínimo obrigatório: 80% de cobertura medida. Meta: 90%.** Valores acima de 90% são válidos; não há teto que exija reduzir testes.
- Aferir linhas executáveis ou a métrica equivalente nativa da ferramenta (instruções/statements), identificando-a explicitamente. O mínimo vale por arquivo de produção novo/alterado e no agregado do escopo implementado. Uma média alta não compensa arquivo implementado sem testes.
- Em arquivo legado alterado, medir as linhas novas/alteradas quando houver suporte confiável a essa medição; caso contrário, medir o arquivo inteiro e declarar o escopo. Não usar cobertura de todo o legado ou de código não alterado para esconder lacunas do incremento.
- Medir e informar branches quando a ferramenta/stack oferecer essa métrica; quando exigidos pela SPEC/política técnica, também devem cumprir seu mínimo. Ausência de medição de branches não pode ser apresentada como percentual atingido. O piso universal de 80% acima é para linhas/instruções executáveis.
- Inventariar todos os artefatos implementados e relacioná-los aos testes e critérios de aceite. Código gerado pelo agente faz parte do escopo; o rótulo “gerado” não autoriza excluí-lo.

## Trabalho obrigatório antes de concluir implementação

1. Planejar ferramenta, versão, escopo, comando, relatório e limiar antes de implementar. Preferir o runner e o coletor já adotados pela stack, sem impor ferramenta Java a Python/Go ou vice-versa.
2. Criar testes úteis de comportamento para o código implementado, incluindo sucesso, falhas, limites e decisões relevantes. Mocks não podem eliminar a lógica que deveria ser exercitada. Escrever testes sem executá-los não satisfaz o gate.
3. Executar a suíte e a coleta de cobertura sobre a revisão atual. Configurar o limiar de falha da ferramenta/CI quando disponível; sempre conferir o relatório por arquivo e do escopo.
4. Registrar em validation.md: revisão/hashes do código e dos testes, inventário, vínculo arquivo→teste→aceite, ferramenta/versão, comando/cwd, código de saída, relatório e percentuais por arquivo/agregado. Informar métricas e exclusões justificadas, sem extrapolar o que a ferramenta mediu.
5. Corrigir falhas e lacunas abaixo de 80% ainda na implementação. Sem testes executados e evidência atual suficiente, manter a implementação em andamento/bloqueada; não declará-la concluída ou pronta para teste humano como IMPLEMENTADA.

## Aprovação e manutenção do gate

`IMPLEMENTACAO_APROVADA` só pode ser registrada após a revisão confirmar testes implementados/executados, resultados satisfatórios e cobertura atual mínima de 80%. Relatório ausente/desatualizado, suíte falha, arquivo sem teste ou cobertura inferior ao mínimo impede aprovação e retorna à implementação. Alteração posterior no código/testes exige nova execução e evidência atual.

Sem ferramenta de aferição ou pré-requisito indispensável, registrar bloqueio e providenciar configuração dentro do escopo autorizado. Auditoria por LLM, teste manual, PDF, quantidade de testes, sintaxe ou ausência de Sonar **não substituem cobertura medida**. Não usar estimativa, arredondamento de valor inferior ao piso ou exclusões artificiais para passar. Regras legadas de fallback não dispensam este gate.

Artefatos sem código executável (documentos, configurações puramente declarativas e interfaces sem lógica) podem ser registrados como não aplicáveis com justificativa objetiva no inventário; não recebem cobertura fictícia. Exclusões técnicas reais, como código mecânico de ferramenta externa sem lógica autoral, precisam estar previstas e justificadas no contrato/revisão e não podem retirar código autoral do denominador. Se não restar código executável, reportar não aplicável, nunca 100% por denominador vazio.

## Interação com os comandos

- `specflow-implementar`: codificar testes e medir cobertura durante a implementação, antes de IMPLEMENTADA.
- `specflow-teste-humano`: só entregar como IMPLEMENTADA após cumprir o gate; testes do usuário ficam pendentes e não substituem a cobertura técnica.
- `specflow-revisar-implementacao`: conferir os relatórios e bloquear IMPLEMENTACAO_APROVADA se qualquer requisito do gate faltar.
- `specflow-validar`: reconferir a validade das evidências, além de seus testes e gate de segurança. Não criar testes/corrigir código durante essa fase; retornar à implementação quando necessário.
- O pedido explícito de omitir a validação formal não dispensa testes/cobertura obrigatórios da implementação. Cobertura suficiente também não dispensa segurança, teste humano ou aceite humano final.

Esta regra define o requisito de processo; não afirma que ferramentas existentes ou o núcleo ainda não implementado já atingiram os percentuais. Não promove retroativamente nenhuma Change ou aprovação.
