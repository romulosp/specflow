# Plano preparatorio

SPEC10032r1 aprovada em 14/11/2026 antes deste plano/codigo.

1. Verificar acesso GitHub e conta PyPI sem expor credenciais.
2. Adicionar verificador de release e testes de comportamento; medir cobertura tambem desse novo arquivo.
3. CI Windows/Linux Python3.11/3.14, build do sdist e smoke. Workflow manual de tag, job OIDC protegido e upload somente apos checks/auditoria.
4. Selecionar somente fonte autoral, licenca, documentacao publica e workflows; revisar diff staged e publicar commit/tag apenas com controles atendidos.
5. Configurar publisher legitimo e publicar. Comprovar indice e uv tool install specflow-cli em ambiente limpo, atualizar guias somente depois.

Sem modelo externo/subagentes; sem acervo, configuracao real ou ambientes no commit/pacote. Indisponibilidade de conta nao vira sucesso.
