# Contributing to Prime Directive

Thank you for helping make actionable AI governance and safety accessible! **Prime Directive** thrives on community input, and we welcome contributions that expand our automation capabilities and playbook inventory.

---

## 🛠️ How to Contribute

### 1. Contribute a Playbook or Script

We focus on machine-parseable, executable assets rather than flat text documentation.

- Select the appropriate NIST AI RMF lifecycle pillar folder (`governance/`, `risk-compliance/`, or `incident-response/`).
- Add or improve a markdown playbook inside its respective `/playbooks/` subdirectory.
- If contributing a compliance validation or risk evaluation script, place it within the root `scripts/` directory.

### 2. Update Codebase Documentation

- Fix typos, clarify execution parameters, or enhance architecture deep-dives.
- Ensure structural changes are accurately documented within the `docs/architecture/` directory.

### 3. Report Vulnerabilities or Issues

- **Security Concerns:** If you identify a flaw that bypasses our algorithmic risk gates or exposes a prompt injection vector, please follow our [SECURITY.md](../SECURITY.md) guidelines and report it confidentially.
- **General Bugs:** For standard code bugs, directory mismatches, or script errors, feel free to open a public GitHub issue with reproduction steps.

---

## 🚦 Core Contribution Guidelines

- **Actionable Over Passive:** Every policy or checklist must be structured as a modular playbook designed to be programmatically parsed and executed by an AI agent or CI/CD runner.
- **Poka-Yoke Compliance:** Your contributions must pass our local automated gate. Before pushing, verify your configuration matches `context7.json` and ensure your code passes the automated verification hooks.
- **Scannability:** All documentation must utilize clean Markdown hierarchies, precise headings, and bolding to ensure quick parsing by both humans and LLM parsing engines.

---

## 📝 Commit Message Protocol

We utilize clean semantic tags to indicate which lifecycle pillar or asset class your changes affect:

```text
[pillar-name] Brief descriptive summary of changes

Optional: Detail the programmatic impact, specific scripts updated, or playbook additions.
```
