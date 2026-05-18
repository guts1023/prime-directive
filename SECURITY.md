# Security Policy

## Supported Versions

Because **Prime Directive** operates as an automated framework runtime, security updates are strictly rolled out to the active main branch. Production systems should track the main branch or tagged stable releases.

| Version    | Supported          |
| ---------- | ------------------ |
| Main (Dev) | :white_check_mark: |
| v1.x.x     | :white_check_mark: |
| < v1.0     | :x:                |

## Reporting a Vulnerability

As an AI Governance, Risk, and Compliance (GRC) and safety framework, maintaining the integrity of our runtime execution engines (such as prompt hardening checklists and validation scripts) is paramount.

### How to Report

If you discover a security vulnerability, prompt injection vector, or a structural flaw that bypasses our algorithmic risk gates, please **do not open a public GitHub issue**. Instead, report it securely by following these steps:

1. Draft a detailed summary of the vulnerability, including step-by-step reproduction steps or the specific payload used to bypass the gate.
2. Open a confidential tracking issue via the repository's **Security Advisories** tab on GitHub, or notify the project maintainers directly via your designated enterprise workspace contact channel.

### What to Expect

- **Acknowledgement:** You will receive an initial response within **48 hours** confirming receipt of the report.
- **Triage & Resolution:** The maintainers will provide updates every **3 to 5 business days** while a mitigation patch is developed and tested within the CI/CD pipeline.
- **Disclosure:** Once a fix is merged into the main branch, a Security Advisory will be published acknowledging your contribution (unless anonymity is requested).
