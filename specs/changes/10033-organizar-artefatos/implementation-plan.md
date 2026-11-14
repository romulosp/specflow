# Plano de implementacao - 10033 r2

Pre-condicoes: decisao humana vinculada a contract-r2.json; conferir hashes antes de iniciar. Revisao tecnica em reviews/spec/review-r2.md.

1. Inventariar gravacoes automaticas e instrucoes ao agente; preservar leitores baseados em referencias e registros legados.
2. Definir destinos e nomes por tipo/revisao nas instrucoes distribuidas, documentacao e geradores aplicaveis; preservar compatibilidade, recusar colisoes e paths externos.
3. Testar comportamento de geracao, leitura legada, conflitos e idempotencia; suite completa via unittest e cobertura com coverage.py. Registrar inventario e relatorio por arquivo e agregado; minimo 80%, meta 90%.
4. Verificar uv em ambiente isolado e registrar versoes e falhas, sem instalacao no perfil pessoal; preparar quickstart e informar limites de atualizacao de consumidor.
5. Revisar e validar nas fases correspondentes, incluindo auditoria de seguranca e gate. Nao publicar, arquivar ou inferir aceite final.

Riscos: gerador de gate possui destino fixo; mudancas exigem continuidade de leituras legadas e compatibilidade de referencias. Atualizar templates distribuidos nao modifica consumidores existentes sem plano de upgrade. Alteracoes em arquivos administrados exigem cuidado com hashes e politica.
