# Prime Directive - Incident Detection & Telemetry Monitoring Standards

**Version:** 1.0.0 (Core Release 2026)
**Target Lifecycle Phase:** Runtime Monitoring & Triage (NIST AI RMF - Measure, Manage)

## 1. Monitoring Scope

This standard establishes the mandatory telemetry logs and early-warning alert thresholds required to detect algorithmic failure, systemic exploitation, or prompt attacks in production gateways.

## 2. Core Telemetry Signals & Alerts

Systems must stream and monitor the following telemetry layers in real-time:

- **Token Distribution Anomalies:** Sudden spikes in output-to-input token ratios indicating potential scraping or loop exploits.
- **Regex Guardrail Triggers:** Immediate alerting on gateway matches for PII structures, database strings, or system configuration keys.
- **Model Refusal Spikes:** Tracking sharp climbs in system-level refusals or error codes, which often indicate an active distributed prompt-injection attempt.
