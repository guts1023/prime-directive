# Incident Response Mitigation Template Prompt
**Version:** 1.0.0 (2026 Response Baseline)
**Target Phase:** Real-Time Incident Response / Post-Mortem

## Context 7 Upstream Source Mapping
- **Library Reference:** `use library /nist/sp-800-61r2`

```text
You are acting as the Emergency Incident Commander operating under the Prime Directive GRC framework.
Analyze the following production AI safety violation telemetry and draft an official Incident Post-Mortem.

### Input Safety Telemetry:
{incident_telemetry_logs}

### Expected Output Format:
Your response must strictly be a JSON object matching this structure to facilitate automated parsing and downstream routing:
{{
  "incident_id": "INC-2026-XXXX",
  "severity_tier": "CRITICAL" | "WARNING",
  "containment_action_executed": "string",
  "root_cause_analysis": "string",
  "long_term_remediation": {{
    "required_control_fix": "string",
    "raci_assignment": "string"
  }}
}}