"""Strict input, confinement and digest primitives; never execute imported data."""
from pathlib import Path
import hashlib
import json
import re
import stat


class Fault(Exception):
    """A redacted, stable operational finding."""

    def __init__(self, code, reason, source=None, field=None):
        super().__init__(reason)
        self.code, self.reason, self.source = code, reason, source
        self.field = field

    def location(self):
        return self.source + ("#" + self.field if self.field else "") if self.source else None


def require(ok, reason="CONTRACT_INVALID", code=2):
    if not ok:
        raise Fault(code, reason)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def fields(value, required, optional=()):
    require(isinstance(value, dict), "OBJECT_REQUIRED")
    missing = set(required) - value.keys()
    if missing or not value.keys() <= set(required) | set(optional):
        raise Fault(2, "FIELDS_INVALID", field=sorted(missing)[0] if missing else "unknown-field")


def version(value, required, optional=()):
    fields(value, {"schemaVersion", *required}, optional)
    require(type(value["schemaVersion"]) is int and value["schemaVersion"] == 1, "SCHEMA_VERSION_INVALID")


def strings(value, nonempty=False):
    require(isinstance(value, list) and all(text(x) for x in value), "STRING_LIST_INVALID")
    require(not nonempty or bool(value), "EMPTY_LIST")
    return value


def _pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, "JSON_DUPLICATE_KEY")
        result[key] = value
    return result


def decode_json(raw):
    try:
        return json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_pairs,
                          parse_constant=lambda _: (_ for _ in ()).throw(Fault(2, "JSON_NONFINITE")))
    except (ValueError, UnicodeError) as error:
        raise Fault(2, "JSON_INVALID") from error


def read_json(path, source=None):
    try:
        return decode_json(Path(path).read_bytes())
    except Fault as error:
        error.source = source or Path(path).name
        raise
    except OSError as error:
        raise Fault(2, "INPUT_UNREADABLE", source=source or Path(path).name) from error


def dump(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def portable(value):
    require(text(value) and not any(x in value for x in ("\\", ":", "\x00")), "PATH_INVALID")
    parts = value.split("/")
    reserved = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)),
                *(f"lpt{i}" for i in range(1, 10))}
    require(all(p not in {"", ".", ".."} and not p.endswith((" ", "."))
                and p.split(".")[0].casefold() not in reserved
                and not any(c in p for c in '<>"|?*') for p in parts), "PATH_INVALID")
    return parts


def link(path):
    try:
        mode = path.lstat()
        return path.is_symlink() or bool(getattr(mode, "st_file_attributes", 0)
                                       & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
    except FileNotFoundError:
        return False


def confined(root, value, writing=False):
    parts = portable(value)
    root = Path(root).absolute()
    if writing:
        cursor = root
        require(not link(cursor), "WRITE_LINK")
        for part in parts:
            cursor = cursor / part
            require(not link(cursor), "WRITE_LINK")
    root = root.resolve()
    path = root.joinpath(*parts).resolve()
    require(path.is_relative_to(root), "PATH_ESCAPE")
    return path


def digest(raw, profile="sha256-bytes-v1"):
    require(isinstance(profile, str) and profile in {"sha256-bytes-v1", "sha256-utf8-lf-v1"}, "DIGEST_PROFILE_INVALID")
    if profile == "sha256-utf8-lf-v1":
        try:
            raw = raw.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
        except UnicodeError as error:
            raise Fault(2, "TEXT_ENCODING_INVALID") from error
    return hashlib.sha256(raw).hexdigest()


def hex_digest(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None, "DIGEST_INVALID")


def manifest(value, contract=False):
    require(isinstance(value, list), "MANIFEST_INVALID")
    paths, roles = set(), set()
    for item in value:
        fields(item, {"path", "role", "sha256", "digestProfile"}, {"rawSha256"})
        portable(item["path"])
        require(text(item["role"]), "ROLE_INVALID")
        require(item["path"].casefold() not in paths, "PATH_DUPLICATE")
        paths.add(item["path"].casefold())
        roles.add(item["role"])
        hex_digest(item["sha256"])
        require(isinstance(item["digestProfile"], str) and item["digestProfile"] in {"sha256-bytes-v1", "sha256-utf8-lf-v1"}, "DIGEST_PROFILE_INVALID")
        if "rawSha256" in item:
            hex_digest(item["rawSha256"])
    if contract:
        require(len(value) == 4 and roles == {"proposal", "spec", "design", "tasks"}, "CONTRACT_MANIFEST_INVALID")
        require(all(x["digestProfile"] == "sha256-utf8-lf-v1" for x in value), "CONTRACT_PROFILE_INVALID")
    return value


def identity(value):
    manifest(value)
    return sorted((x["path"], x["role"], x["digestProfile"], x["sha256"]) for x in value)


def verify(root, value):
    manifest(value)
    failures = []
    for item in value:
        try:
            path = confined(root, item["path"])
            require(path.is_file(), "ARTIFACT_MISSING", 1)
            require(digest(path.read_bytes(), item["digestProfile"]) == item["sha256"], "ARTIFACT_STALE", 1)
        except OSError:
            failures.append(Fault(2, "ARTIFACT_UNREADABLE", source=item["path"]))
        except Fault as error:
            if error.source is None:
                error.source = item["path"]
            failures.append(error)
    if failures:
        raise sorted(failures, key=lambda x: (-x.code, x.reason))[0]


def bind(root, refs, value, roles):
    strings(refs)
    manifest(value)
    require(set(refs) == {x["path"] for x in value}, "EVIDENCE_SCOPE_MISMATCH", 1)
    for item in value:
        expected = roles[item["path"]] if isinstance(roles, dict) else roles
        require(item["role"] == expected and item["digestProfile"] == "sha256-bytes-v1", "EVIDENCE_PROFILE_INVALID")
    verify(root, value)


def capture(root, refs, role="artifact", profile="sha256-bytes-v1"):
    result = []
    for ref in refs:
        try:
            raw = confined(root, ref).read_bytes()
        except OSError as error:
            raise Fault(2, "ARTIFACT_UNREADABLE") from error
        result.append({"path": ref, "role": role, "digestProfile": profile, "sha256": digest(raw, profile)})
    manifest(result)
    return result
