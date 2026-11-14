---
name: "Executar mudança Spec Driven"
description: "Use quando: executar uma mudança Spec Driven de ponta a ponta, respeitando todos os gates e registrando evidências."
argument-hint: "Informe o caminho da mudança, por exemplo specs/changes/003-gerenciar-categorias"
agent: "agent"
---

# Execução integral de mudança Spec Driven

Execute a mudança indicada em `${input:changePath}` de ponta a ponta, obedecendo estritamente a [AGENTS.md](../../AGENTS.md) e ao [workflow canônico](../../specs/shared/process/workflow.md). Trabalhe em português do Brasil.

## Objetivo

Conduza a mudança pelas sete fases obrigatórias, sempre respeitando os gates e sem solicitar ao usuário uma nova instrução entre fases aprovadas:

`SPEC → revisão da SPEC → implementação → revisão da implementação → validação → aprovação → commit`.

A SPEC é a fonte da verdade. Identifique a primeira fase pendente, execute-a e avance automaticamente para a seguinte quando o respectivo gate for aprovado. Interrompa imediatamente se um gate for reprovado, falhar ou estiver bloqueado.

## Modo de execução automática

1. Trate este prompt como o orquestrador do fluxo completo; não peça que o usuário escreva separadamente “revisão”, “implementação”, “validação” ou “aprovação”.
2. Quando a mudança estiver em `RASCUNHO` e o contrato estiver completo, execute a revisão da SPEC diretamente. Se a SPEC for aprovada, registre o planejamento técnico preparatório e continue na mesma conversa para a implementação.
3. Após registrar `IMPLEMENTADA`, execute a revisão da implementação. Com `IMPLEMENTACAO_APROVADA`, chame `specflow-validar` por padrão, incluindo security-audit e o script de gate. Só deixe de executar a fase se o prompt do usuário a excluir expressamente; registre revisão, solicitação/motivo e não execução em validation.md e na memória, sem VALIDADA nem avanço para aprovação/encerramento. Um limite explícito como teste-humano continua prevalecendo. Se validada, as decisões humanas e autorizações de aprovação/encerramento continuam obrigatórias; não criar aceite ou commit automaticamente.
4. Ao encontrar um gate reprovado, pare no mesmo turno, informe a evidência objetiva e a primeira fase à qual a mudança deve retornar. Não avance nem tente contornar a pendência. Exceção: achado de segurança confirmado e corrigível dentro da SPEC aprovada retorna automaticamente à implementação, revisão, validação e nova auditoria.
5. Antes de encerrar, informe a última fase alcançada, status, arquivos atualizados, comandos e códigos de saída, bloqueios e hash do commit, quando aplicável.

Exemplo de uso:

```text
/Executar mudança Spec Driven specs/changes/004-parametrizar-nome-projeto-gerado
```

## Preparação obrigatória

1. Leia `proposal.md`, `spec.md`, `DESIGN.md`, `tasks.md`, `implementation-plan.md` quando existir, `validation.md`, todos os relatórios em `reviews/` e as regras compartilhadas aplicáveis.
2. Identifique o estado atual usando os documentos da mudança e [STATUS.md](../../STATUS.md).
3. Antes de executar qualquer comando Maven, configure a sessão do terminal para usar Java 17 e Maven 3.8.8. A configuração é temporária, vale somente para a sessão e não deve ser gravada em `pom.xml`, arquivos gerados ou variáveis permanentes do sistema.
	 - No Prompt de Comando do Windows, execute:

		 ```bat
		 set JAVA_HOME=C:\Desenvolvimento\jdk-17.0.11
		 set MAVEN_HOME=C:\Desenvolvimento\apache-maven-3.8.8
		 set PATH=%JAVA_HOME%\bin;%MAVEN_HOME%\bin;%PATH%
		 ```

	 - No PowerShell, use a sintaxe equivalente:

		 ```powershell
		 $env:JAVA_HOME = 'C:\Desenvolvimento\jdk-17.0.11'
		 $env:MAVEN_HOME = 'C:\Desenvolvimento\apache-maven-3.8.8'
		 $env:PATH = "$env:JAVA_HOME\bin;$env:MAVEN_HOME\bin;$env:PATH"
		 ```

	 - Confirme as versões efetivas com `java -version` e `mvn -version` e registre-as em `validation.md` quando a fase de validação for executada.
4. Verifique as Skills exigidas para a próxima fase antes de agir.
5. Não altere código, contratos ou testes fora da fase permitida.

## Regras inegociáveis

- Nunca implemente antes de `proposal.md` e `spec.md` estarem ambos em `SPEC_APROVADA`.
- Antes da implementação, registre `implementation-plan.md` com impactos, riscos, testes unitários e de integração, qualidade e auditoria de segurança. Esse artefato é preparatório e não altera as fases 01-06.
- Durante a implementação, codifique/execute testes para todo código implementado e meça cobertura mínima de 80%, meta de 90%, por arquivo/escopo conforme `specs/shared/testing/coverage-policy.md`. Código escrito pelo agente não é exclusão. Sem suíte aprovada e relatório atual com o piso, não concluir IMPLEMENTADA ou aprovar IMPLEMENTACAO_APROVADA. LLM, falta de Sonar e omissão da validação formal não dispensam esse gate.
- Não invente decisões, contratos ou requisitos para contornar pendências. Registre a evidência exigida e encerre se a fase estiver bloqueada.
- Revisões não corrigem código ou requisitos. Validação não corrige código. Aprovação não altera código nem executa testes. Commit não revalida a entrega.
- Não arquive a mudança nem crie commit sem relatório formal com estado `APROVADA`.
- Não inclua segredos, `target/` ou outros artefatos gerados no commit.
- Quando houver reprovação ou falha, indique objetivamente a primeira fase à qual a mudança deve retornar.

## Fases e gates

### 1. SPEC — definir o contrato

Se a mudança estiver em especificação (`RASCUNHO` ou equivalente), confirme que `proposal.md`, `spec.md`, `DESIGN.md` e `tasks.md` definem objetivo, escopo, restrições, comportamentos, critérios de aceite e cenários de validação. Não implemente nesta fase. Encaminhe o contrato para revisão.

### 2. Revisão da SPEC — verificar se o contrato é implementável

Execute a Skill `spec-review`. Avalie exclusivamente clareza, completude, consistência, escopo, riscos e testabilidade; não invente requisitos nem implemente soluções. Crie o relatório com achados `REV-*` em `reviews/`.

- Aprovada: atualize `proposal.md` e `spec.md` para `SPEC_APROVADA` e avance.
- Reprovada: registre `REPROVADA`, indique os achados bloqueantes e encerre.

### 3. Implementação — cumprir o contrato aprovado

Somente com `proposal.md` e `spec.md` em `SPEC_APROVADA`, execute o planejamento técnico de `specs/sprint/prompts/prompt-planejar-implementacao.md` e registre `implementation-plan.md`. Em seguida, execute a Skill `spec-implement`. Implemente exclusivamente os artefatos, contratos e comportamentos aprovados. Crie ou atualize testes unitários e de integração aplicáveis, atualize `tasks.md` e mantenha a documentação de código necessária.

Para projetos Java Quarkus gerados, derive `PROJETO_DIR=apps/backend/<artifactId-sem-hifens>/`, crie essa pasta antes de gerar qualquer arquivo e crie `PROJETO_DIR/start_aplicacao.bat` com o conteúdo abaixo, preservando a configuração temporária de Java 17.0.11 e Maven 3.8.8. Execute Maven a partir de `PROJETO_DIR`:

No `pom.xml`, o `quarkus-maven-plugin` deve conter uma execução com o goal `build`, além de `extensions=true`, para que `mvn quarkus:dev` seja reconhecido como aplicação Quarkus e permaneça em execução.

```bat
@echo off
setlocal

cd /d "%~dp0"

rem ===== CONFIGURACAO DO AMBIENTE =====
set JAVA_HOME=C:\Desenvolvimento\jdk-17.0.11
set MAVEN_HOME=C:\Desenvolvimento\apache-maven-3.8.8
set PATH=%JAVA_HOME%\bin;%MAVEN_HOME%\bin;%PATH%

echo ==========================================
echo Java em uso:
"%JAVA_HOME%\bin\java.exe" -version
echo ==========================================
echo.


mvn quarkus:dev

pause
endlocal
```

- Concluída somente com testes executados e cobertura medida atual mínima de 80% por arquivo/escopo (meta 90%): registre `IMPLEMENTADA` e avance. Sem essas evidências ou abaixo do piso, manter em andamento/bloqueada e corrigir; não declarar implementação concluída.
- Bloqueada: registre `BLOQUEADA`, a causa e a fase de retorno; encerre.

### 4. Revisão da implementação — comparar entrega e SPEC

Com a mudança em `IMPLEMENTADA`, confirme a existência de `implementation-plan.md` e execute a Skill `implementation-review`. Compare código, configurações, dependências, contratos, testes, critérios de aceite e alterações indevidas contra a SPEC aprovada e o plano técnico. Não corrija nada durante a revisão. Salve o relatório com achados `IMP-REV-*` em `reviews/`.

- Aprovada somente com aderência, suíte aprovada e evidência atual do gate de cobertura (mínimo 80%, meta 90%): registre `IMPLEMENTACAO_APROVADA` e avance. Relatório ausente/desatualizado, testes ausentes/falhos ou piso insuficiente impedem aprovação.
- Reprovada: registre `REPROVADA`, indique as divergências e retorne à implementação; encerre.

### 5. Validação — provar o comportamento por evidências

Somente com a implementação aprovada, execute por padrão o comando local `specflow-validar`, que conduz o procedimento `implementation-validate`, os testes aplicáveis e o gate obrigatório de segurança. Não aguarde que o usuário peça a validação separadamente. A exceção é o prompt do usuário expressamente pedir para não executar essa fase ou limitar o fluxo antes dela: registre a solicitação, o motivo, a revisão e a fase não executada em validation.md e na memória; pare sem VALIDADA, aprovação ou encerramento. Omitir PDF ou uma ferramenta não omite a fase; falha e bloqueio também não autorizam pular gates. Na execução normal, registre ambiente, versões, comandos, códigos de saída, cenários, resultados e evidências `VAL-*`.

Quando o módulo não possuir Sonar ou ferramenta de cobertura, ou quando Docker, SonarQube, scanner, token ou dependência necessária ao Sonar estiverem indisponíveis, execute a Auditoria de Qualidade Assistida por LLM: rode build, tipo, lint e testes disponíveis; mapeie os artefatos alterados para seus testes aplicáveis; revise bugs, vulnerabilidades e hotspots de segurança, defeitos, tratamento de erro, duplicação, código morto, complexidade e documentação; e registre motivo do fallback, escopo, comandos, resultados, achados e correções em `validation.md`. Não declare percentual estimado de cobertura nem afirme que o Sonar foi executado. Falha de build, scanner ou Quality Gate depois de o Sonar estar disponível não é fallback: reprova a validação e retorna a Change à implementação.

O fallback acima trata qualidade operacional e nunca substitui a cobertura mínima medida da implementação. Sem ferramenta de aferição/relatório atual, o gate de cobertura permanece bloqueado; não aprovar a implementação por análise de LLM ou teste manual.

Quando a fase for executada, security-audit é obrigatória: registre categorias aplicáveis/não aplicáveis, evidências e auditoria atual em `<Change>/security-audit.json` e execute `python -B docs/security-audit/verificar_seguranca.py --change <Change>`. Achado aberto, check incompleto/falho, auditoria ausente/desatualizada ou erro mantém a fase pendente. PDF só quando solicitado; `gerar_relatorio.py` apenas formata dados, não verifica segurança nem libera o gate. Não reutilizar relatório histórico.

Se houver achado de segurança confirmado, retorne à implementação e corrija-o autonomamente dentro da SPEC aprovada. Em seguida, repita revisão da implementação, validação e auditoria. Se a correção exigir alteração da SPEC, ação externa ou decisão fora do escopo, registre `BLOQUEADA` e encerre. Não aprove nem faça commit enquanto houver achado confirmado, relatório ausente ou relatório que não represente a auditoria atual.

- Êxito: registre `VALIDADA` e avance.
- Falha: registre a evidência, a causa e a fase de retorno; encerre.

### 6. Aprovação — decidir formalmente o encerramento técnico

Somente com a mudança validada, execute a Skill `change-approve`. Não implemente, corrija ou teste nesta fase. Verifique que não existem pendências materiais, falhas ou achados bloqueantes e que os gates anteriores correspondem a:

| Fase | Estado obrigatório |
| --- | --- |
| Revisão da SPEC | `SPEC_APROVADA` |
| Implementação | `IMPLEMENTADA` |
| Revisão da implementação | `IMPLEMENTACAO_APROVADA` |
| Validação | `VALIDADA` |
| Segurança, como parte da validação | Auditoria atual sem achados confirmados em aberto |

- Aprovada: produza o relatório formal, atualize [STATUS.md](../../STATUS.md) para `APROVADA` e avance.
- Reprovada: informe a primeira fase que deve ser retomada e encerre.

### 7. Commit — fechar a entrega aprovada

Somente com relatório de aprovação em `APROVADA`, execute a Skill `git-commit`. Atualize `specs/system/`, prepare o arquivamento, revise os arquivos incluídos e crie um único commit rastreável. Depois do commit bem-sucedido, mova a mudança para `archive/`, atualize [STATUS.md](../../STATUS.md) para `ARQUIVADA` e registre o hash no relatório de aprovação.

## Resultado esperado

Ao encerrar, informe a fase alcançada, o status final, os arquivos de evidência criados ou atualizados, comandos e testes executados com seus códigos de saída, bloqueios encontrados, a fase de retorno se houver reprovação e o hash do commit quando houver. Não declare sucesso se algum gate obrigatório não tiver sido concluído.
