# Cobertura e testes - 10033 r2

Python em .venv-specflow; coverage.py 7.17.3. Com PYTHONPATH=framework/src;framework/tests e COVERAGE_FILE nesta pasta: `python -m coverage run --branch --source=framework/src/specflow -m unittest discover -s framework/tests -q`; depois `python -m coverage json -o coverage.json`. Codigo 0; 54 testes, um skip de permissao de symlink.

- cli.py -> test_cli.py -> CA01, CA03, CA04, CA08.
- security.py -> test_artifact_paths.py, test_core.py e test_cli.py -> CA02, CA03, CA04, CA08.
- bundle-v1.json -> test_cli.py e smoke do wheel -> CA01 e CA06; dados nao executaveis, sem percentual.

- framework\src\specflow\cli.py: 163/166 linhas (98.19%).
- framework\src\specflow\security.py: 67/69 linhas (97.10%).
- Agregado: 1291/1335 linhas (96.70%). Branches: 341/368 (92.66%).

Relatorio completo em coverage.json; hashes de codigo e testes em evidence/implementation-manifest.json.
