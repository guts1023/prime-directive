# Prime Directive Roadmap

**Roadmap is directional, not a guarantee; issues and discussions drive priorities.**

This roadmap outlines a 3-phase plan to build Prime Directive from a core prompt library into a community-driven resource for AI governance, risk, and compliance (GRC).

---

## Phase 1 – Solidify the Core Library (0–3 months)

### Finish v1 Prompt Sets

- At least 3–5 prompts each in:
  - Governance
  - Risk & Compliance
  - AI Safety
- Ensure all follow the common template and have clear, testable Expected Output.

### Stand Up One Flagship Framework Profile

- Populate `grc_framework/nist-ai-rmf/` with a starter profile and a prompt bundle that assembles a NIST‑aligned pack.
- Serve as a template for future framework profiles.

### Improve Project Ergonomics

- Finalize README, `docs/CONTRIBUTING.md`, `docs/GOVERNANCE.md`.
- Add basic labels in Issues (e.g., `prompt`, `framework-profile`, `good-first-issue`).
- Set up issue templates for common contribution types.

---

## Phase 2 – Frameworks and Adoption Paths (3–9 months)

### Add Opinionated "Profiles"

- **Small startup AI GRC profile** – minimal but real governance for resource-constrained teams.
- **Enterprise / regulated profile** – assumes legal, risk, and audit functions.
- Additional domain-specific profiles as community feedback emerges.

### Map to Established Frameworks

- Short mapping notes in `grc_framework/established-frameworks/*` for:
  - NIST AI Risk Management Framework
  - Major clouds' Responsible AI principles (Microsoft, Google, Amazon, OpenAI, Anthropic, Meta)
  - Other emerging standards and regulations
- Make it easy for teams to see how Prime Directive aligns with their existing governance standards.

### Publish "30‑Minute Adoption" Guides

- Simple, step‑by‑step docs showing how to go from zero to:
  - Charter + approval workflow
  - Basic risk scoring
  - Safety checklist
- Real use-case walkthroughs that demonstrate end-to-end value.

---

## Phase 3 – Community and Integrations (9–18 months)

### Community Growth

- Issue templates for:
  - "New prompt request"
  - "New framework profile request"
- Regular "prompt review" or "profile review" cycles with contributors.
- Highlight community contributions and recognize contributors.

### Ecosystem Integrations

- Example usage with one or two popular AI agent/orchestration frameworks.
- Show how to load Prime Directive prompts as a library or integrate into existing workflows.
- SDK or API patterns for programmatic access to prompt collections.

### Maturity and Maintenance

- Versioning scheme for prompts and frameworks.
- Changelog for breaking changes or updated mappings as regulations and standards evolve.
- Process for deprecating outdated prompts or profiles.

---

## Success Metrics

- **Phase 1:** Core library complete; NIST profile live; contribution guidelines clear.
- **Phase 2:** ≥2 opinionated profiles published; ≥3 framework mappings documented; adoption guides available.
- **Phase 3:** Active community contributions; integrations with ≥1 popular AI framework; versioning/changelog in place.

---

## How to Contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on submitting new prompts, profiles, and improvements.

Interested in a specific roadmap item? Open an issue or discussion to coordinate.
