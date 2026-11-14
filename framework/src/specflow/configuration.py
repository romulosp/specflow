"""Properties are data, with no Java escapes, environment interpolation or probes."""
from importlib.resources import files
from urllib.parse import urlsplit
import re
from .storage import decode_json, fields, version, require, text, Fault


def catalog():
    value = decode_json(files("specflow").joinpath("assets/resources-v1.json").read_bytes())
    version(value, {"resources"})
    require(isinstance(value["resources"], dict), "RESOURCE_CATALOG_INVALID")
    return value["resources"]


def parse(raw, definitions=None):
    definitions = catalog() if definitions is None else definitions
    declared = {key for item in definitions.values() for key in item["fields"]}
    try:
        content = raw.decode("utf-8-sig")
    except UnicodeError as error:
        raise Fault(2, "PROPERTIES_ENCODING_INVALID") from error
    result = {}
    for line in content.replace("\r\n", "\n").split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        require("=" in line and "\r" not in line and "\x00" not in line, "PROPERTIES_SYNTAX_INVALID")
        key, value = line.split("=", 1)
        key = key.strip()
        require(re.fullmatch(r"[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)+", key) is not None
                and key in declared and key not in result, "PROPERTIES_KEY_INVALID")
        result[key] = value
    return result


def resolve(resource_id, properties, definitions=None):
    definitions = catalog() if definitions is None else definitions
    require(resource_id in definitions, "RESOURCE_UNDECLARED")
    resource = definitions[resource_id]
    keys = list(resource["fields"])
    missing = [k for k in keys if k not in properties or not properties[k].strip()]
    placeholders = [k for k in keys if properties.get(k, "").strip().casefold() == "definir"]
    outcome = {"status": "available", "missingKeys": sorted(missing), "invalidKeys": [],
               "configurationReady": False, "automaticExecution": False}
    if placeholders:
        outcome["status"] = "inactive_placeholder"
        return outcome
    if missing:
        outcome["status"] = "inactive_missing"
        return outcome
    optional = set()
    if resource.get("authKey"):
        mode = properties[resource["authKey"]].strip().casefold()
        if mode not in resource["modes"]:
            outcome.update(status="inactive_invalid", invalidKeys=[resource["authKey"]])
            return outcome
        optional = set(resource["modes"][mode]["optional"])
    invalid = []
    for key, kind in resource["fields"].items():
        value = properties[key]
        if value.strip().casefold() == "nao_aplicavel":
            if key not in optional:
                invalid.append(key)
            continue
        if kind == "url":
            try:
                url = urlsplit(value)
                if url.scheme not in {"http", "https"} or not url.hostname or url.username or url.password or value != value.strip():
                    invalid.append(key)
                if url.port is not None and not 0 < url.port < 65536:
                    invalid.append(key)
            except ValueError:
                invalid.append(key)
    if invalid:
        outcome.update(status="inactive_invalid", invalidKeys=sorted(set(invalid)))
    else:
        outcome["configurationReady"] = True
    return outcome


def statuses(raw):
    definitions = catalog()
    values = parse(raw, definitions)
    return {key: resolve(key, values, definitions) for key in sorted(definitions)}


def require_resource(resource_id, raw):
    values = parse(raw)
    value = resolve(resource_id, values)
    require(value["configurationReady"], "RESOURCE_INACTIVE", 1)
    return value
