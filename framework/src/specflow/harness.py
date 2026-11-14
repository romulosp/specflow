"""Read-only harness, also available as python -m specflow.harness."""
from .cli import SafeParser
from .memory import result
from .storage import dump, Fault


def main(argv=None):
    parser = SafeParser(prog="specflow-core")
    parser.add_argument("operation", choices=["context", "check", "evaluate"])
    parser.add_argument("--project", required=True)
    parser.add_argument("--change", required=True)
    parser.add_argument("--target")
    try:
        args = parser.parse_args(argv)
        value = result(args.project, args.change, args.operation, args.target)
    except Fault:
        value = result(".", None, "invalid")
    print(dump(value), end="")
    return value["exitCode"]


if __name__ == "__main__":
    raise SystemExit(main())
