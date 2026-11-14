"""Pinned installed policy; consumer copies never override the runtime policy."""
from importlib.resources import files
from .storage import decode_json, require, digest, version, strings

POLICY_DIGEST = "108c383c53415bc3950fbf2d557fb5c8ac287a1c5de80621a6385184419160d0"
POLICY_ID = "specflow-local"
POLICY_VERSION = "1"


def policy_bytes():
    return files("specflow").joinpath("assets/policy-v1.json").read_bytes()


def load_policy():
    raw = policy_bytes()
    value = decode_json(raw)
    version(value, {"policyId", "policyVersion", "coverageFloor", "coverageTarget", "states", "methods",
                    "securityAllOpenFindingsBlock", "humanApprovalRequired"})
    require(value.get("policyId") == POLICY_ID
            and value.get("policyVersion") == POLICY_VERSION, "POLICY_VERSION_INVALID")
    strings(value["states"], True)
    strings(value["methods"], True)
    require(type(value["coverageFloor"]) is int and type(value["coverageTarget"]) is int
            and type(value["humanApprovalRequired"]) is bool
            and type(value["securityAllOpenFindingsBlock"]) is bool, "POLICY_INVALID")
    require(digest(raw) == POLICY_DIGEST, "INSTALLED_POLICY_STALE", 1)
    return value
