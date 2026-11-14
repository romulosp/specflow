# Dependências locais de diagrama

Ferramentas opcionais de documentação; não são dependências do núcleo Python. Versões exatas e integridade estão em `package.json` e `package-lock.json`. Instalação local reproduzível: `npm ci --prefix tools/diagramas --ignore-scripts`.

Para usar os scripts de mermaid-studio no PowerShell, defina temporariamente `$env:MERMAID_STUDIO_DIR` para o caminho absoluto desta pasta e restaure o valor após a execução. Valide `docs/comandos/fluxo-comandos.mmd` com o script validate.mjs e renderize com render.mjs usando engine beautiful-mermaid. Os ajustes locais usam file URLs compatíveis com Windows; avisos e limitações constam na evidência de documentação.

Depois da renderização, `python -B tools/diagramas/exportar_svg.py docs/comandos/fluxo-comandos.svg` remove dependência de CSS dinâmico/fontes remotas para exportação autocontida. O PNG de entrega foi rasterizado desse SVG e inspecionado visualmente. O parser Mermaid foi validado em DOM local de jsdom, sem buscar recursos externos ou executar scripts do diagrama.

Não versionar node_modules; manter os avisos de licença das dependências. Nenhum navegador, serviço ou infraestrutura de aplicação foi instalado/iniciado para produzir o SVG.
