# design

RASCUNHO. Completar requisitos, riscos e aceites; este modelo nao registra aprovacao ou execucao.

## Fronteiras por dominio

Para cada dominio definido na SPEC, descrever limites, dados sob responsabilidade, operacoes/contratos, dependencias permitidas e integracoes. Documentar ownership compartilhado, consistencia e comportamento de falha quando aplicaveis.

## Responsabilidades dos componentes

Mapear dominio -> componente/classe -> regras -> contrato de integracao. Concentrar regras em seu dominio; orquestracao fina pode coordenar dominios sem absorver suas regras. Dividir componentes que acumulem responsabilidades independentes. Tamanho e sinal de revisao, sem limite arbitrario de linhas.
