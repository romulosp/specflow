# Plano - 10034 r1

SPEC r1 aprovada pelo usuario, hashes conferidos. Plano antes de codigo.

1. Reconciliar inventario com indice e hashes locais. Excluir preventivamente do checkout todo acervo importado, inclusive componentes apenas declarados licenciados sem confirmacao upstream. Preservar bytes locais e avisos. Identificar substituicoes autorais minimas do processo a partir dos ativos autorais do pacote, com backup privado e recibo antes de escrever.
2. Separar verificacao publica da local: modo auto/public/local, saida explicita not_run para acervo ausente, falha para acervo parcial. Manter verificacao historica completa no modo local. Nunca executar comando de inventario JSON.
3. Testar publicacao de arvore candidata completa isolada no workspace, sem commit: inventario, comandos, testes de produto e de ferramentas, build e smoke. Vincular logs ao manifesto exato da arvore.
4. Cobertura minima 80% por arquivo executavel alterado e agregado, meta 90%; inventario fonte-teste-criterio. Revisar e validar seguranca depois das correcoes. Historico publico e licencas continuam limites separados. Sem commit, push ou reescrita de historico automatica.
