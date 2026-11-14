"""Public terminal adapter; editor handoffs are never claims of phase completion."""
import argparse
from importlib import metadata, resources
from pathlib import Path
import sys
from . import contracts, validation
from .consumer import initialize, doctor, new_change, find_project, VERSION
from .fileops import Transaction, busy
from .memory import load, result, reconciled
from .workflow import assess, implementation_target
from .security import gate_result
from .storage import Fault, require, read_json, decode_json, dump, confined, version


class SafeParser(argparse.ArgumentParser):
    def error(self, message):
        raise Fault(2, "ARGUMENTS_INVALID")


def package_version():
    try:
        return metadata.version("specflow-cli")
    except metadata.PackageNotFoundError:
        return VERSION


def catalog():
    value = decode_json(resources.files("specflow").joinpath("assets/catalog-v1.json").read_bytes())
    return {item["name"].removeprefix("specflow-"): item for item in value["commands"]}


def _common(argv):
    filtered, project, as_json = [], None, False
    index = 0
    while index < len(argv):
        item = argv[index]
        if item == "--":
            filtered.extend(argv[index:])
            break
        if item == "--json":
            as_json = True
        elif item == "--project" or item.startswith("--project="):
            if item == "--project":
                index += 1
                require(index < len(argv) and not argv[index].startswith("--"), "PROJECT_ARGUMENT_REQUIRED")
                value = argv[index]
            else:
                value = item.split("=", 1)[1]
            require(bool(value) and (project is None or project == value), "PROJECT_ARGUMENT_CONFLICT")
            project = value
        else:
            filtered.append(item)
        index += 1
    return filtered, project, as_json


def parser():
    value = SafeParser(prog="specflow", description="Processo Spec Driven proprio: CLI local e agente no editor")
    value.add_argument("--version", action="version", version=package_version())
    value.add_argument("--project", help="Raiz explicita; aceita antes/depois do subcomando")
    value.add_argument("--json", action="store_true", help="Saida estruturada")
    commands = value.add_subparsers(dest="command", required=True, parser_class=SafeParser)
    init = commands.add_parser("init", help="Inicializar consumidor sem ativar recursos")
    init.add_argument("destination")
    init.add_argument("--integration", action="append", choices=sorted({"copilot", "codex"}), default=[])
    commands.add_parser("doctor", help="Conferir arquivos e configuracao sem probes")
    new = commands.add_parser("nova-change", help="Criar rascunho sem aprovacao")
    new.add_argument("objective")
    for name, item in catalog().items():
        command = commands.add_parser(name, aliases=["context"] if name == "contexto" else [], help=item["description"])
        command.add_argument("--change", required=True)
    for name in ["check", "evaluate"]:
        command = commands.add_parser(name, help="Avaliacao deterministica, sem aplicar transicao")
        command.add_argument("--change", required=True)
        command.add_argument("--target", choices=contracts.STATES, required=True)
    return value


def admin(operation, **extra):
    return {"schemaVersion": 1, "operation": operation, "projectId": None, "changeId": None,
            "outcome": "prepared", "phaseExecuted": False, "localChecksExecuted": [],
            "editorInstructions": None, "findings": [], "pending": [], "limitations": [], "exitCode": 0, **extra}


def _plan(ctx):
    path = confined(ctx["root"], (ctx["folder"] / "implementation-plan.md").relative_to(ctx["root"]).as_posix())
    require(path.is_file() and path.stat().st_size > 0, "IMPLEMENTATION_PLAN_MISSING", 1)


def phase(root, change_id, name):
    item = catalog()[name]
    value = admin(name, editorInstructions={
        "command": item["name"], "copilot": "/" + item["name"], "codex": "$" + item["name"],
        "phase": item["phase"], "steps": item["steps"], "boundary": item.get("boundary", "Somente a fase solicitada")})
    try:
        busy(root)
        ctx = load(root, change_id)
        value["changeId"] = change_id
        value["projectId"] = ctx["project"]["projectId"]
        if name not in {"especificar", "esclarecer", "revisar-spec"}:
            reconciled(ctx)
        if name == "revisar-spec":
            assess(ctx, "EM_REVISAO_SPEC")
        elif name in {"planejar", "implementar", "teste-humano"}:
            assess(ctx, "SPEC_APROVADA")
            if name != "planejar":
                _plan(ctx)
        elif name == "revisar-implementacao":
            assess(ctx, "IMPLEMENTADA")
        elif name == "validar":
            assess(ctx, "IMPLEMENTACAO_APROVADA")
            with Transaction(root) as tx:
                # Reload under our own lock, directly through the library (no CLI redispatch).
                ctx = load(tx.root, change_id)
                assess(ctx, "IMPLEMENTACAO_APROVADA")
                from .security import security_path
                ref = security_path(tx.root, ctx["folder"], "security-gate.json")
                path = confined(tx.root, ref, writing=True)
                if path.exists():
                    try:
                        previous = read_json(path)
                        version(previous, {"changeId", "status", "validationAllowed", "exitCode", "reasons", "method", "limitations"})
                        require(previous["changeId"] == change_id, "GATE_DESTINATION_CONFLICT", 1)
                    except Fault as error:
                        raise Fault(1, "GATE_DESTINATION_CONFLICT") from error
                gate = gate_result(tx.root, ctx["folder"])
                tx.apply({ref: dump(gate).encode("utf-8")})
                value["localChecksExecuted"] = ["security_gate"]
                require(gate["exitCode"] == 0, "SECURITY_PENDING", gate["exitCode"])
                assess(ctx, "VALIDADA")
        elif name == "aprovar":
            assess(ctx, "VALIDADA")
            require(ctx["handoffs"], "HUMAN_HANDOFF_MISSING", 1)
            for handoff in ctx["handoffs"]:
                validation.handoff(root, handoff, ctx["change"]["implementationManifest"], manual=True,
                                   evidences=ctx["evidences"], target_manifest=implementation_target(ctx))
        elif name == "encerrar":
            assess(ctx, "APROVADA")
    except Fault as error:
        value.update(outcome="blocked" if error.code == 1 else "error", exitCode=error.code,
                     findings=[{"id": error.reason, "source": error.location()}], pending=[{"id": error.reason}])
    return value


def _emit(value, as_json):
    if as_json or "observedState" in value and "allowed" in value:
        print(dump(value), end="")
    else:
        print(value["operation"] + ": " + value["outcome"])
        if value.get("changeId"):
            print("Change: " + value["changeId"])
        for finding in value["findings"]:
            print(finding["id"])
        instructions = value.get("editorInstructions")
        if instructions:
            print("Editor: " + instructions["copilot"] + " ou " + instructions["codex"])
            for step in instructions["steps"]:
                print("- " + step)
        for name, record in value.get("resources", {}).items():
            print(name + ": " + record["status"])
    return value["exitCode"]


def main(argv=None):
    raw = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in raw
    operation = "arguments"
    try:
        arguments, selected, as_json = _common(raw)
        args = parser().parse_args(arguments)
        operation = "contexto" if args.command == "context" else args.command
        if operation == "init":
            base = Path(selected or Path.cwd())
            if selected is not None:
                require(args.destination == "." or not Path(args.destination).is_absolute(), "INIT_DESTINATION_INVALID")
                if args.destination != ".":
                    from .storage import portable
                    portable(args.destination)
                require((base / args.destination).resolve().is_relative_to(base.resolve()), "PATH_ESCAPE")
            destination = base / args.destination
            value = admin(operation, **initialize(destination, args.integration))
        else:
            root = Path(selected).resolve() if selected is not None else find_project(Path.cwd())
            if operation == "doctor":
                value = admin(operation, **doctor(root))
                if value["exitCode"]:
                    value["outcome"] = "blocked"
            elif operation == "nova-change":
                value = admin(operation, **new_change(root, args.objective))
            elif operation in {"contexto", "check", "evaluate"}:
                busy(root)
                value = result(root, args.change, "context" if operation == "contexto" else operation,
                               getattr(args, "target", None))
            else:
                value = phase(root, args.change, operation)
    except (Fault, OSError, UnicodeError, ValueError, TypeError, RuntimeError) as error:
        code = error.code if isinstance(error, Fault) else 2
        reason = error.reason if isinstance(error, Fault) else "OPERATION_INPUT_ERROR"
        value = admin(operation, outcome="blocked" if code == 1 else "error", exitCode=code,
                      findings=[{"id": reason, "source": error.location() if isinstance(error, Fault) else None}], pending=[{"id": reason}])
    return _emit(value, as_json)
