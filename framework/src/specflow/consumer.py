"""Consumer initialization, ownership, drafts and confined application generation."""
from importlib.resources import files
from pathlib import Path
import re
import unicodedata
from . import contracts
from .configuration import statuses
from .fileops import Transaction, busy
from .policy import POLICY_ID, POLICY_VERSION, POLICY_DIGEST, policy_bytes, load_policy
from .memory import read_project
from .storage import (Fault, require, text, read_json, decode_json, dump, confined, digest, fields, version, portable)

VERSION = "0.2.1"
INTEGRATIONS = {"copilot", "codex"}


def bundle():
    value = decode_json(files("specflow").joinpath("assets/bundle-v1.json").read_bytes())
    version(value, {"common", "copilot", "codex"})
    for group in ("common", "copilot", "codex"):
        require(isinstance(value[group], dict), "BUNDLE_INVALID")
        for path, content in value[group].items():
            portable(path)
            require(isinstance(content, str), "BUNDLE_CONTENT_INVALID")
    return value


def find_project(start):
    path = Path(start).resolve()
    for candidate in (path, *path.parents):
        if (candidate / ".specflow/project.json").is_file():
            confined(candidate, ".specflow/project.json")
            return candidate
    raise Fault(2, "PROJECT_NOT_INITIALIZED")


def _managed(root):
    path = confined(root, ".specflow/managed-files.json", writing=True)
    if not path.is_file():
        return None
    record = read_json(path)
    version(record, {"version", "integrations", "files"})
    require(record["version"] == VERSION, "UPGRADE_PLAN_REQUIRED", 1)
    contracts.strings(record["integrations"])
    require(set(record["integrations"]) <= INTEGRATIONS, "INTEGRATION_INVALID")
    require(isinstance(record["files"], dict), "OWNERSHIP_INVALID")
    require(".specflow/managed-files.json" not in record["files"]
            and "configuracao.properties" not in record["files"], "OWNERSHIP_SELF_REFERENCE")
    for ref, expected in record["files"].items():
        contracts.hex_digest(expected)
        path = confined(root, ref, writing=True)
        require(path.is_file() and digest(path.read_bytes()) == expected, "MANAGED_FILE_DIVERGED", 1)
    return record


def initialize(root, integrations=()):
    require(all(isinstance(x, str) and x in INTEGRATIONS for x in integrations), "INTEGRATION_INVALID")
    load_policy()
    original = Path(root).absolute()
    project_id = re.sub(r"[^A-Za-z0-9_-]", "-", original.name)[:80].strip("-_") or "project"
    with Transaction(original) as tx:
        root = tx.root
        previous = _managed(root)
        project_path = confined(root, ".specflow/project.json", writing=True)
        if project_path.exists():
            require(previous is not None, "PROJECT_WITHOUT_OWNERSHIP", 1)
            project = read_project(root)
            project_id = project["projectId"]
        else:
            require(previous is None, "OWNERSHIP_WITHOUT_PROJECT", 1)
            project = {"schemaVersion": 1, "projectId": project_id, "policyId": POLICY_ID,
                       "policyVersion": POLICY_VERSION, "policyDigest": POLICY_DIGEST,
                       "changesPath": "specs/changes", "knowledgePath": "specs/knowledge"}
        selected = sorted(set(integrations) | (set(previous["integrations"]) if previous else set()))
        content = bundle()
        plan = {key: value.encode("utf-8") for key, value in content["common"].items()}
        # AGENTS belongs to the consumer once created; it is not managed or overwritten.
        agents = confined(root, "AGENTS.md", writing=True)
        if agents.exists():
            plan.pop("AGENTS.md", None)
        for group in selected:
            plan.update({key: value.encode("utf-8") for key, value in content[group].items()})
        plan[".specflow/project.json"] = dump(project).encode("utf-8")
        plan[".specflow/policies/policy-v1.json"] = policy_bytes()
        wrapper = files("specflow").joinpath("assets/gate_wrapper.py").read_bytes()
        plan["docs/security-audit/verificar_seguranca.py"] = wrapper
        properties = confined(root, "configuracao.properties", writing=True)
        if properties.exists():
            require(properties.is_file(), "PROPERTIES_DESTINATION_CONFLICT", 1)
        else:
            plan["configuracao.properties"] = files("specflow").joinpath("assets/configuracao.example.properties").read_bytes()
        ignore = confined(root, ".gitignore", writing=True)
        old_ignore = ignore.read_bytes() if ignore.is_file() else b""
        require(not ignore.exists() or ignore.is_file(), "IGNORE_DESTINATION_CONFLICT", 1)
        try:
            lines = old_ignore.decode("utf-8-sig").splitlines()
        except UnicodeError as error:
            raise Fault(2, "IGNORE_ENCODING_INVALID") from error
        marker = "/configuracao.properties"
        matches = [i for i, line in enumerate(lines) if line.strip() in {marker, marker[1:]}]
        if matches:
            require(not any(line.lstrip().startswith("!") for line in lines[matches[-1] + 1:]), "IGNORE_PROTECTION_CONFLICT", 1)
        else:
            newline = b"\r\n" if b"\r\n" in old_ignore else b"\n"
            plan[".gitignore"] = old_ignore + (newline if old_ignore and not old_ignore.endswith(b"\n") else b"") + marker.encode() + newline
        managed = dict(previous["files"]) if previous else {}
        for ref, data in plan.items():
            if ref not in {"AGENTS.md", "configuracao.properties", ".gitignore"}:
                managed[ref] = digest(data)
        plan[".specflow/managed-files.json"] = dump({"schemaVersion": 1, "version": VERSION,
                                                    "integrations": selected, "files": managed}).encode("utf-8")
        tx.apply(plan, mutable={".specflow/managed-files.json", ".gitignore"})
        return {"projectId": project_id, "integrations": selected, "filesPrepared": len(plan),
                "limitations": ["Ignore does not remove previously tracked secrets; no Git or service was executed"]}


def doctor(root):
    root = Path(root).resolve()
    busy(root)
    project = read_project(root)
    require(_managed(root) is not None, "OWNERSHIP_MISSING")
    values = statuses(confined(root, "configuracao.properties").read_bytes())
    code = 1 if any(x["status"] == "inactive_invalid" for x in values.values()) else 0
    return {"projectId": project["projectId"], "resources": values, "exitCode": code,
            "limitations": ["Configuration readiness does not execute or certify integrations", "Editor discovery requires a real client test"]}


def new_change(root, objective):
    require(text(objective) and "\x00" not in objective, "OBJECTIVE_REQUIRED")
    with Transaction(root) as tx:
        root = tx.root
        project = read_project(root)
        directory = confined(root, project["changesPath"], writing=True)
        reservation_dir = confined(root, ".specflow/reservations", writing=True)
        numbers = []
        for parent in [directory, reservation_dir]:
            if parent.is_dir():
                for child in parent.iterdir():
                    match = re.match(r"^(\d+)(?:[-.]|$)", child.name)
                    if match:
                        numbers.append(int(match[1]))
        number = max(numbers, default=0) + 1
        prefix = str(number).zfill(5)
        require(len(prefix) < 79, "CHANGE_IDS_EXHAUSTED")
        slug = unicodedata.normalize("NFKD", objective).encode("ascii", "ignore").decode().lower()
        slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-") or "mudanca"
        ident = prefix + "-" + slug[:79 - len(prefix)].rstrip("-")
        contracts.ident(ident)
        tx.reserve(".specflow/reservations/" + prefix + ".json", dump({"schemaVersion": 1, "number": number}).encode())
        base = project["changesPath"] + "/" + ident
        refs, plan = {}, {}
        templates = bundle()["common"]
        names = {"proposal": "proposal.md", "spec": "spec.md", "design": "DESIGN.md", "tasks": "tasks.md",
                 "validation": "validation.md", "memory": "AGENTS-MEMORY.md"}
        for role, name in names.items():
            ref = base + "/" + name
            refs[role] = ref
            content = ("# " + role + " — " + ident + "\n\nRASCUNHO. Nenhuma aprovacao ou execucao registrada.\n\nObjetivo autoral:\n\n"
                       + objective + "\n\nCompletar requisitos, riscos e aceites antes de revisar a SPEC.\n")
            if role in {"spec", "design", "tasks"}:
                content += "\n" + templates["specs/templates/" + role + "-template.md"]
            plan[ref] = content.encode("utf-8")
        draft = {"schemaVersion": 1, "changeId": ident, "revision": "r1", "objective": objective, "documentRefs": refs}
        contracts.draft(draft)
        plan[base + "/draft.json"] = dump(draft).encode("utf-8")
        tx.apply(plan)
        return {"changeId": ident, "revision": "r1", "observedState": "RASCUNHO", "path": base}


def generate_application(root, app_id, templates, approved_scope):
    from .memory import load
    from .workflow import assess
    require(isinstance(app_id, str) and re.fullmatch(r"[a-z][a-z0-9-]{0,62}", app_id) is not None, "APPLICATION_ID_INVALID")
    fields(approved_scope, {"changeId", "paths"})
    require(isinstance(templates, dict) and templates, "APPLICATION_TEMPLATE_REQUIRED")
    with Transaction(root) as tx:
        ctx = load(tx.root, approved_scope["changeId"])
        assess(ctx, "SPEC_APROVADA")
        plan_path = confined(tx.root, (ctx["folder"] / "implementation-plan.md").relative_to(tx.root).as_posix())
        require(plan_path.is_file(), "IMPLEMENTATION_PLAN_MISSING", 1)
        plan = {"apps/" + app_id + "/" + ref: content for ref, content in templates.items()}
        contracts.refs(approved_scope["paths"], True)
        require(set(plan) == set(approved_scope["paths"]), "GENERATION_SCOPE_MISMATCH", 1)
        tx.apply(plan)
        return sorted(plan)
