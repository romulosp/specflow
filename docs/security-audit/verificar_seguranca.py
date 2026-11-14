"""Gate local de evidencias da skill security-audit; nao substitui analise de seguranca."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
ID = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,99}')


def text(value):
    return isinstance(value, str) and bool(value.strip())


def confined(root, value):
    if not text(value):
        raise ValueError('invalid path')
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or '\\' in value or ':' in value:
        raise ValueError('invalid path')
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError('path escapes project')
    return resolved


def evaluate(report, root):
    """Return code/reason IDs only; never execute commands or echo report bodies."""
    reasons = []
    if not isinstance(report, dict) or type(report.get('schemaVersion')) is not int or report['schemaVersion'] != 1:
        return 2, ['AUDIT_SCHEMA_INVALID']
    required = {'schemaVersion', 'changeId', 'revision', 'review', 'scope', 'artifacts', 'findings', 'checks'}
    if set(report) != required or not text(report['changeId']) or not text(report['revision']):
        return 2, ['AUDIT_FIELDS_INVALID']
    review = report['review']
    if not isinstance(review, dict) or set(review) != {'skill', 'reviewer', 'status', 'limitations'}:
        return 2, ['AUDIT_REVIEW_INVALID']
    if review['skill'] != 'security-audit' or review['status'] not in {'completed', 'pending'}:
        return 2, ['AUDIT_REVIEW_INVALID']
    if not isinstance(review['limitations'], list) or not all(text(v) for v in review['limitations']):
        return 2, ['AUDIT_REVIEW_INVALID']
    if not text(review['reviewer']) or review['status'] != 'completed':
        reasons.append('AUDIT_REVIEW_PENDING')
    scope, artifacts, findings, checks = (report[k] for k in ['scope', 'artifacts', 'findings', 'checks'])
    if not all(isinstance(v, list) for v in [scope, artifacts, findings, checks]):
        return 2, ['AUDIT_LIST_INVALID']
    if not scope or not artifacts or not checks:
        reasons.append('AUDIT_EVIDENCE_INCOMPLETE')
    if not all(text(p) for p in scope) or len(scope) != len(set(scope)):
        return 2, ['AUDIT_SCOPE_INVALID']
    artifact_paths = []
    for artifact in artifacts:
        if not isinstance(artifact, dict) or set(artifact) != {'path', 'digestProfile', 'sha256'}:
            return 2, ['AUDIT_ARTIFACT_INVALID']
        path = confined(root, artifact['path'])
        profile = artifact['digestProfile']
        if profile not in {'sha256-bytes-v1', 'sha256-utf8-lf-v1'}:
            return 2, ['AUDIT_DIGEST_PROFILE_INVALID']
        if not isinstance(artifact['sha256'], str) or not re.fullmatch('[0-9a-f]{64}', artifact['sha256']):
            return 2, ['AUDIT_DIGEST_INVALID']
        artifact_paths.append(artifact['path'])
        if not path.is_file():
            reasons.append('AUDIT_ARTIFACT_MISSING')
            continue
        raw = path.read_bytes()
        if profile == 'sha256-utf8-lf-v1':
            raw = raw.decode('utf-8-sig', errors='strict').replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
        if hashlib.sha256(raw).hexdigest() != artifact['sha256']:
            reasons.append('AUDIT_ARTIFACT_STALE')
    for path in scope:
        confined(root, path)
    if len(set(artifact_paths)) != len(artifact_paths):
        return 2, ['AUDIT_ARTIFACT_DUPLICATE']
    if set(artifact_paths) != set(scope):
        reasons.append('AUDIT_SCOPE_UNCOVERED')
    seen = set()
    for row in findings:
        if not isinstance(row, dict) or set(row) != {'id', 'severity', 'status', 'evidenceRefs'}:
            return 2, ['AUDIT_FINDING_INVALID']
        ident = row['id']
        if not isinstance(ident, str) or not ID.fullmatch(ident) or ident in seen:
            return 2, ['AUDIT_FINDING_ID_INVALID']
        seen.add(ident)
        if row['severity'] not in {'critical', 'high', 'medium', 'low', 'info'} or row['status'] not in {'open', 'resolved'}:
            return 2, ['AUDIT_FINDING_INVALID']
        refs = row['evidenceRefs']
        if not isinstance(refs, list) or not refs or not all(text(p) for p in refs):
            reasons.append('AUDIT_FINDING_EVIDENCE_MISSING:' + ident)
        else:
            if not all(confined(root, p).is_file() for p in refs):
                reasons.append('AUDIT_FINDING_EVIDENCE_MISSING:' + ident)
        if row['status'] == 'open':
            reasons.append('AUDIT_FINDING_OPEN:' + ident)
    seen = set()
    for row in checks:
        if not isinstance(row, dict) or set(row) != {'id', 'method', 'expectedCode', 'actualCode', 'outcome', 'evidenceRefs'}:
            return 2, ['AUDIT_CHECK_INVALID']
        ident = row['id']
        if not isinstance(ident, str) or not ID.fullmatch(ident) or ident in seen:
            return 2, ['AUDIT_CHECK_ID_INVALID']
        seen.add(ident)
        if row['method'] not in {'static', 'automated', 'manual'} or row['outcome'] not in {'passed', 'failed', 'not_run'}:
            return 2, ['AUDIT_CHECK_INVALID']
        if type(row['expectedCode']) is not int or (row['actualCode'] is not None and type(row['actualCode']) is not int):
            return 2, ['AUDIT_CHECK_CODE_INVALID']
        refs = row['evidenceRefs']
        if not isinstance(refs, list) or not all(text(p) for p in refs):
            return 2, ['AUDIT_CHECK_EVIDENCE_INVALID']
        if row['outcome'] != 'passed' or row['actualCode'] != row['expectedCode'] or not refs:
            reasons.append('AUDIT_CHECK_PENDING:' + ident)
        if refs and not all(confined(root, p).is_file() for p in refs):
            reasons.append('AUDIT_CHECK_EVIDENCE_MISSING:' + ident)
    return (1 if reasons else 0), sorted(set(reasons))


def run(change, root=ROOT):
    root = root.resolve()
    change = change.resolve()
    if not change.is_relative_to(root) or not change.is_dir():
        raise ValueError('change outside project or missing')
    path = change / 'security-audit.json'
    report = None
    try:
        if not path.is_file():
            code, reasons = 1, ['AUDIT_REPORT_MISSING']
        else:
            # Resolve symlinks before reading audit evidence.
            if not path.resolve().is_relative_to(root):
                raise ValueError('audit outside project')
            report = json.loads(path.read_text(encoding='utf-8-sig'))
            code, reasons = evaluate(report, root)
            if code != 2 and isinstance(report, dict) and report.get('changeId') != change.name:
                code, reasons = 1, ['AUDIT_CHANGE_MISMATCH']
    except (ValueError, OSError, UnicodeError, TypeError):
        code, reasons = 2, ['AUDIT_INPUT_ERROR']
    summary = {'schemaVersion': 1, 'changeId': change.name,
               'status': 'verificada' if code == 0 else 'pendente',
               'validationAllowed': code == 0, 'exitCode': code,
               'reasons': reasons,
               'method': 'Evidence gate; security-audit analysis remains mandatory',
               'limitations': ['Does not authenticate reviewer or prove evidence truth or completeness outside declared scope',
                               'Does not run commands from audit JSON or approve the Change']}
    summary_path = change / 'security-gate.json'
    if not summary_path.resolve().is_relative_to(root):
        raise ValueError('summary outside project')
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--change', type=Path, required=True)
    args = parser.parse_args()
    try:
        summary = run(args.change)
    except (ValueError, OSError):
        print('Gate pendente: caminho da Change ou destino invalido.', file=sys.stderr)
        return 2
    print(json.dumps(summary, ensure_ascii=False))
    return summary['exitCode']


if __name__ == '__main__':
    sys.exit(main())
