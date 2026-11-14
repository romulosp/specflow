"""Explicit script entry to the installed, trusted CLI. Copyright 2026 Romulo Penha, MIT."""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys


class SafeParser(argparse.ArgumentParser):
    def error(self, message):
        print(json.dumps({"exitCode": 2, "reason": "ARGUMENTS_INVALID"}))
        raise SystemExit(2)


def main(argv=None):
    parser = SafeParser(description="Conferir seguranca via SpecFlow instalado")
    parser.add_argument("--change", required=True)
    args = parser.parse_args(argv)
    try:
        root = Path(__file__).resolve().parents[2]
        change = Path(args.change)
        change = (root / change).resolve() if not change.is_absolute() else change.resolve()
    except (OSError, RuntimeError, ValueError):
        print(json.dumps({"exitCode": 2, "reason": "CHANGE_PATH_INVALID"}))
        return 2
    if not change.is_relative_to(root) or not change.is_dir():
        print(json.dumps({"exitCode": 2, "reason": "CHANGE_PATH_INVALID"}))
        return 2
    executable = shutil.which("specflow")
    if executable is None:
        print(json.dumps({"exitCode": 2, "reason": "SPECFLOW_NOT_ON_PATH"}))
        return 2
    # Only the fixed CLI operation is executed, never commands from an audit file.
    try:
        code = subprocess.run([executable, "validar", "--project", str(root), "--change", change.name, "--json"],
                              shell=False, check=False).returncode
        return code if code in {0, 1, 2} else 2
    except OSError:
        print(json.dumps({"exitCode": 2, "reason": "SPECFLOW_EXECUTION_FAILED"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
