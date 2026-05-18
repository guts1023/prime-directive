# Prime Directive - Remediation, Recovery & Re-Certification Standards

**Version:** 1.0.0 (Core Release 2026)
**Target Lifecycle Phase:** Eradication & System Recovery (NIST SP 800-61r2)

## 1. Remediation Requirements

System restoration cannot occur until the technical root cause of the exploit is verified, patched, and systematically tested on an isolated hotfix branch.

## 2. Mandatory Re-Certification Gates

Before a hotfix code change can be deployed to production, it must pass through the following validation checks:

- **Adversarial Regression Run:** Exposing the updated prompt architecture to the exact exploit payload that triggered the initial breach to confirm the fix works.
- **Evaluation Baseline Sync:** Running the core system evaluation suite to verify that prompt hardening patches did not cause a regression in standard operational performance.
