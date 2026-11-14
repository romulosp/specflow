# Checkout publico e acervo local

`python -B tools/verificar_dossie.py` seleciona o modo local quando a pasta imports/acervo-local-2026-11-12 existe; caso contrario, seleciona o modo publico. `--mode public` verifica exclusoes, hashes das substituicoes autorais, recursos de processo e comandos. `--mode local` executa a verificacao historica de integridade e suporte, incluindo fixtures e sintaxe; se o acervo estiver incompleto ou corrompido, falha. No modo publico a integridade do acervo e explicitamente not_run.

O inventario de retirada e os avisos sao declarativos. O verificador nao concede direitos nem confirma upstream. Historico e releases anteriores continuam publicos; so podem ser tratados por acao especifica autorizada. Pacote, CI, aceite humano e eventual publicacao possuem gates separados.

Geracao de PDF, recursos Sprint, scripts Sonar e skills importadas permanecem somente no acervo local e nao integram o checkout publico candidato. Templates e instrucoes essenciais do produto usam textos autorais. Para diagramas, dependencias declaradas continuam opcionais e sob suas proprias licencas.
