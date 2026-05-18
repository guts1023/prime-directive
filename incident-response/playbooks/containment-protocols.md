# Prime Directive - Technical Containment & Isolation Protocols

**Version:** 1.0.0 (Core Release 2026)
**Target Lifecycle Phase:** Crisis Containment & Damage Control (NIST SP 800-61r2)

## 1. Isolation Mandates

When a Tier 2 or Tier 3 incident is confirmed by monitoring telemetry, responders must instantly isolate the blast radius without dropping entire application endpoints.

## 2. Containment Execution Modes

- **Model Decoupling:** Dynamic rerouting of user traffic from the active LLM pipeline to static, hardcoded validation rule engines.
- **Context Purging:** Forcing an immediate purge of volatile context memory buffers and vector session states to break data poisoning loops.
- **Traffic Shunting:** Dropping API gateway request rates for unverified external endpoints while maintaining normal operation for internal health-checks.
