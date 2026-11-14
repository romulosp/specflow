# Estratégia de testes

A regra universal para qualquer stack está em [coverage-policy.md](coverage-policy.md): testes obrigatórios durante a implementação, mínimo de 80% de cobertura medida por arquivo/escopo implementado e meta de 90%, permitindo valores superiores. Essa condição é necessária para IMPLEMENTADA e IMPLEMENTACAO_APROVADA. Os tópicos JUnit/Mockito/Quarkus abaixo são convenções Java, não requisitos das demais stacks.

## Princípios gerais

- Testes unitários usam JUnit 5 e Mockito, exercitam a lógica real e são independentes de banco de dados e do container Quarkus.
- Testes de integração Quarkus usam `@QuarkusTest` e H2 no perfil de teste quando não for necessária compatibilidade específica com DB2.
- Toda validação registra ambiente, resultado e evidência em `validation.md`.
- A prioridade é a qualidade da validação da regra de negócio, seguida pela cobertura, legibilidade e manutenção futura.

## Inventário e cobertura

1. Cada mudança Java deve inventariar os arquivos `.java` de produção alterados ou incluídos no escopo.
2. Toda classe aplicável deve ter pelo menos uma classe de teste unitário correspondente. São aplicáveis serviços de aplicação e de domínio, repositórios, conversores, validadores, exceções customizadas, utilitários e enums que contenham lógica.
3. Artefatos sem lógica executável podem ser registrados como não aplicáveis com justificativa explícita, sem removê-los do inventário. Código escrito pelo agente não pode ser excluído por ser “gerado”. Exclusão de código mecânico externo deve seguir a política universal e o contrato revisado.
4. O mínimo obrigatório é 80% de cobertura medida de linhas/instruções por arquivo novo/alterado e agregado do escopo, com meta de 90% e valores superiores válidos. Branches devem ser reportados quando disponíveis e atender requisitos adicionais da stack/SPEC. A métrica não substitui cenários relevantes de negócio.
5. Defina ferramenta, baseline, limiar e comando no planejamento; execute a medição ainda na implementação antes de concluir/aprovar a entrega. Não declarar percentual sem aferição reproduzível. Falta de medição bloqueia; não transferir a criação dos testes para a validação formal.

## Mockito avançado

- Use `spy()` apenas quando for necessário executar parcialmente a lógica real da classe.
- Em spies, use `doReturn(...).when(spy)` em vez de `when(spy.metodo()).thenReturn(...)`, evitando a execução antecipada do método real.
- Use `doNothing()` exclusivamente para métodos `void`.
- Use `verify()` para validar interações que façam parte do comportamento relevante.
- Não crie mocks que não participem do comportamento testado. Prefira objetos reais simples quando isso tornar a regra mais clara.

## Panache sem container Quarkus

- Testes unitários não executam com o container Quarkus ativo; `Arc` pode estar nulo.
- Não execute chamadas reais a `persist()`, `find()`, `list()` ou qualquer operação que dependa de `EntityManager`.
- Simule ou intercepte chamadas Panache com Mockito e cubra a lógica anterior à persistência sem depender do runtime Quarkus.
- Quando o comportamento exigir banco, ORM ou ciclo de vida do Quarkus, ele pertence a teste de integração, não a teste unitário.

## Consultas, varargs e reflexão

- Use `TypedQuery<T>` ao simular `entityManager.createQuery(sql, Classe.class)`.
- Use `Query` ao simular `entityManager.createNativeQuery(sql)`.
- O tipo do mock deve corresponder exatamente ao tipo esperado pelo método de produção.
- Em métodos com `Object...`, prefira `any(Object[].class)` a `any()` e aplique casts explícitos quando necessários para resolver overloads ambíguos.
- Use reflexão somente para acessar método privado que contenha regra relevante e que não possa ser coberta pela API pública.
- Centralize a reflexão em utilitários reutilizáveis. Não use `setAccessible(true)` sem justificativa documentada.
- Métodos públicos devem ser testados diretamente; métodos estáticos devem ser invocados diretamente, sem reflexão.

## Dados válidos e regras dependentes de enum

- Construa objetos de teste válidos para a regra exercitada.
- Quando houver dependência de enums, como `CodigoTransacaoEnum` ou `SituacaoMovimentoEnum`, preencha todos os atributos exigidos pelo cenário.
- Não use objetos parcialmente inicializados para produzir exceções artificiais; elas não representam a regra de negócio.

## Qualidade, exceções e branches

- Mantenha os testes compatíveis com SonarQube: elimine ambiguidades de tipo, suppressions desnecessárias, múltiplos `continue` ou `break` no mesmo loop e reflexão injustificada.
- Valide comportamento e resultado, e não apenas a execução de linhas ou detalhes internos. Priorize asserts de negócio em vez de asserts puramente técnicos.
- Evite mocks excessivos que impeçam a execução real da lógica. O teste deve permanecer válido diante de pequenas refatorações internas.
- Cubra fluxos normais e de erro. Blocos `catch` que contenham regra de negócio devem ter cenário que valide o comportamento após a exceção.
- Cubra decisões `if`, `else`, `switch`, enums e opcionais, quando aplicáveis.
- Cubra coleções nulas, vazias e com conteúdo, além de `Optional.empty()` e `Optional.of()` quando aplicáveis.

## Resultado esperado

Os testes unitários devem cobrir a lógica real da aplicação, não depender de banco ou container Quarkus, ser compatíveis com SonarQube, legíveis, pouco frágeis e úteis como documentação executável da regra de negócio.
