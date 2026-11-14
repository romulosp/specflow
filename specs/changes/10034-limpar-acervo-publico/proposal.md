# Proposta - Limpar acervo publico com direitos pendentes

Revisao r1, 14/11/2026. EM_REVISAO_SPEC.

## Objetivo
Preparar checkout publico funcional sem acervo de redistribuicao nao liberada ou licencas nao confirmadas, preservando copias locais, contratos aprovados e avisos de terceiros. O usuario escolheu manter o repositorio publico e preparar a limpeza.

## Contexto
Retirada de 273 arquivos preparada no indice; inventario e hashes em docs/release/inventario-retirada-acervo.json. Verificador historico depende do acervo local e falha em checkout da arvore proposta. Historico e release ja publicos permanecem acessiveis. Licencas declaradas e upstream ainda exigem conferencia; nao inferir direitos.

## Escopo e exclusoes
Inventariar direitos e dependencias; definir arvore publicavel e comportamento de verificacao em checkout limpo; criar substituicoes autorais quando necessarias; testar. Nao alterar o checkout externo, eliminar copias locais, reescrever historico, remover tag/release, tornar privado, criar commit ou publicar automaticamente. Tratar exposicao historica explicitamente como pendencia.
