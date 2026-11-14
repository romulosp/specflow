"""Cenarios de bloqueio do suporte de seguranca; nao auditam o nucleo."""
from pathlib import Path
import hashlib
import importlib.util
import json
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('security_gate', ROOT / 'docs/security-audit/verificar_seguranca.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class SecurityGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.change = self.root / 'changes/demo'
        self.change.mkdir(parents=True)
        (self.root / 'code.py').write_text('print("synthetic")\n', encoding='utf-8')
        (self.root / 'evidence.txt').write_text('synthetic check completed; not real audit', encoding='utf-8')
        self.report = {
            'schemaVersion': 1, 'changeId': 'demo', 'revision': 'fixture-r1',
            'review': {'skill': 'security-audit', 'reviewer': 'synthetic fixture', 'status': 'completed', 'limitations': []},
            'scope': ['code.py'],
            'artifacts': [{'path': 'code.py', 'digestProfile': 'sha256-bytes-v1',
                           'sha256': hashlib.sha256((self.root / 'code.py').read_bytes()).hexdigest()}],
            'findings': [], 'checks': [{'id': 'CHECK-1', 'method': 'static',
                                       'expectedCode': 0, 'actualCode': 0, 'outcome': 'passed',
                                       'evidenceRefs': ['evidence.txt']}],
        }

    def run_gate(self):
        (self.change / 'security-audit.json').write_text(json.dumps(self.report), encoding='utf-8')
        result = gate.run(self.change, self.root)
        self.assertEqual(result, json.loads((self.change / 'security-gate.json').read_text(encoding='utf-8')))
        return result

    def test_complete_current_evidence_passes_only_security_gate(self):
        result = self.run_gate()
        self.assertEqual(0, result['exitCode'])
        self.assertTrue(result['validationAllowed'])
        self.assertEqual('verificada', result['status'])

    def test_missing_report_stays_pending(self):
        result = gate.run(self.change, self.root)
        self.assertEqual(1, result['exitCode'])
        self.assertFalse(result['validationAllowed'])

    def test_all_open_severities_block(self):
        for severity in ['critical', 'high', 'medium', 'low', 'info']:
            with self.subTest(severity=severity):
                self.report['findings'] = [{'id': 'SEC-1', 'severity': severity, 'status': 'open', 'evidenceRefs': ['evidence.txt']}]
                result = self.run_gate()
                self.assertEqual(1, result['exitCode'])
                self.assertEqual('pendente', result['status'])

    def test_changed_artifact_blocks_old_audit(self):
        (self.root / 'code.py').write_text('print("changed")', encoding='utf-8')
        self.assertIn('AUDIT_ARTIFACT_STALE', self.run_gate()['reasons'])

    def test_failed_or_not_run_check_blocks(self):
        for outcome, code in [('failed', 1), ('not_run', None)]:
            with self.subTest(outcome=outcome):
                self.report['checks'][0].update(outcome=outcome, actualCode=code)
                self.assertEqual(1, self.run_gate()['exitCode'])

    def test_resolved_finding_without_evidence_stays_pending(self):
        self.report['findings'] = [{'id': 'SEC-1', 'severity': 'high', 'status': 'resolved', 'evidenceRefs': []}]
        self.assertEqual(1, self.run_gate()['exitCode'])

    def test_empty_template_cannot_pass(self):
        self.report['review']['status'] = 'pending'
        self.report['artifacts'] = self.report['scope'] = self.report['checks'] = []
        self.assertEqual(1, self.run_gate()['exitCode'])

    def test_escape_input_errors_and_never_reads_outside_root(self):
        self.report['artifacts'][0]['path'] = '../outside.py'
        self.assertEqual(2, self.run_gate()['exitCode'])

    def test_wrong_change_cannot_reuse_report(self):
        self.report['changeId'] = 'other'
        self.assertEqual(1, self.run_gate()['exitCode'])

    def test_malformed_contract_is_error_and_pending(self):
        self.report['schemaVersion'] = True
        result = self.run_gate()
        self.assertEqual(2, result['exitCode'])
        self.assertEqual('pendente', result['status'])


if __name__ == '__main__':
    unittest.main()
