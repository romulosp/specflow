# SPEC - 10034-limpar-acervo-publico

## Status
EM_REVISAO_SPEC - r1. Nao ha aprovacao humana desta revisao.

## Requisitos
- RF01: Manter inventario dos arquivos retirados, origem, motivo, hashes e estado de direitos. Arquivos de direitos desconhecidos ficam fora da arvore publica proposta; licenca declarada nao comprova proveniencia ou atendimento de termos.
- RF02: Preservar copias locais e arquivos alterados, e identificar colisao ou mudanca posterior antes de qualquer acao no indice. Nao apagar arquivos locais ou reescrever historico.
- RF03: Inventariar dependencias do checkout publico e substituir somente quando necessario por artefatos autorais documentados, sem copiar conteudo nao liberado nem alterar bytes de contratos aprovados.
- RF04: O verificador de checkout publico deve distinguir ausencia esperada de acervo local da falha real; nao declarar verificacao de integridade do acervo que nao foi executada. Verificacao local completa continua disponivel quando acervo estiver presente.
- RF05: Validar arvore exata proposta em checkout isolado, sem sobrescrever o workspace; demonstrar comandos de produto, testes e ferramentas afetadas e registrar limitacoes.
- RF06: Identificar referencias quebradas, scripts e workflows dependentes e corrigi-los ou registrar pendencias que bloqueiem a entrega. Atualizar documentacao e avisos para nao prometer direitos ou capacidades nao comprovados.
- RF07: Registrar separadamente historico e releases publicos, licencas declaradas sem confirmacao upstream e recursos nao classificados; nao alegar que remocao do branch elimina exposicao historica.

## Qualidade e seguranca
- RNF01: Testes de comportamento codificados e executados; cobertura minima 80% por arquivo executavel alterado e agregado, meta 90%, com inventario fonte-teste-criterio e medicao atual.
- RNF02: Sem sobrescrita silenciosa, execucao de dados JSON ou escrita fora do workspace; preservar paths e avisos de terceiros e o processo aprovado.

## Aceites
- CA01: Checkout publico nao contem arquivos sem direitos confirmados identificados, e lista exclusoes e pendencias sem reproduzir conteudo restrito.
- CA02: Checkout publico sem acervo apresenta resultado honesto para verificacoes; checkout local completo executa o modo de integridade existente e detecta arquivo ausente ou alterado.
- CA03: Suite e cobertura atuais satisfazem RNF01; testes abrangem ausencia, corrupcao, conflito, paths externos e falha de ferramenta.
- CA04: Arquivos locais e contratos aprovados preservados; nenhum historico, tag ou release alterado sem autorizacao aplicavel.
- CA05: Manifests e logs de teste relacionam a arvore efetivamente testada; CI remoto, exposicao historica e direitos pendentes sao separados de conclusoes locais.
