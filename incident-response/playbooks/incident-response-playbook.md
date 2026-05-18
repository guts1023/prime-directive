# AI Incident Response Playbook

## Detect

- Objective: Identify AI incidents quickly through monitoring, alerts, and human reporting.
- Key activities and decision points:
  - Define detection signals for anomalous outputs, drift, abuse, and system errors.
  - Monitor model behavior, input distributions, latency, and safety thresholds.
  - Establish automated alerts for critical failures and manual reporting channels for users and operators.
  - Decide when a detection event becomes an incident requiring formal response.
- Who should be involved:
  - AI operations team
  - Monitoring/observability engineers
  - Product owners and safety reviewers
  - Customer support or incident intake personnel
- Expected outputs or documentation:
  - Detection rules and alert definitions
  - Incident intake checklist
  - Monitoring dashboards and alert logs

## Notify

- Objective: Alert the right stakeholders quickly so the incident is understood and escalated appropriately.
- Key activities and decision points:
  - Confirm incident severity and impact.
  - Notify the incident response lead and core response team.
  - Escalate to legal, security, product, and executives based on impact and compliance requirements.
  - Decide if external reporting or customer notification is required.
- Who should be involved:
  - Incident response lead
  - Engineering and security representatives
  - Legal/compliance advisor
  - Product manager or owner
- Expected outputs or documentation:
  - Initial incident notification record
  - Stakeholder contact list and escalation log
  - Communication timeline and update schedule

## Contain

- Objective: Limit harm from the incident while preserving evidence and enabling recovery.
- Key activities and decision points:
  - Isolate the affected AI system, model, pipeline, or data source.
  - Pause or disable dangerous features and rollback recent changes if needed.
  - Preserve logs, metrics, and system state for investigation.
  - Decide between temporary containment and longer-term mitigation actions.
- Who should be involved:
  - Engineering responders
  - Security operations
  - Data governance or privacy team if data is involved
  - Product owner for customer impact decisions
- Expected outputs or documentation:
  - Containment action log
  - Evidence preservation checklist
  - System state snapshot and rollback notes

## Fix

- Objective: Resolve the root cause, restore safe operation, and validate the fix before returning to normal service.
- Key activities and decision points:
  - Conduct root cause analysis to identify why the incident occurred.
  - Implement corrective actions or code/data/model fixes.
  - Validate the fix through testing, review, and monitoring.
  - Decide when it is safe to restore full functionality.
- Who should be involved:
  - Engineering or ML operations team
  - Quality assurance or testing team
  - Product and safety reviewers
  - Change control approver if required
- Expected outputs or documentation:
  - Root cause analysis report
  - Remediation plan and implementation notes
  - Validation results and rollback criteria

## Review

- Objective: Learn from the incident and improve processes, controls, and system resilience.
- Key activities and decision points:
  - Conduct a post-incident review with stakeholders.
  - Document lessons learned, root causes, and recommended improvements.
  - Update detection, response, and training materials.
  - Decide on follow-up actions and owners for changes.
- Who should be involved:
  - Incident response team
  - Product, engineering, and safety leads
  - Legal/compliance as needed
  - Executive sponsor or governance representative
- Expected outputs or documentation:
  - Post-incident review summary
  - Action items with owners and timelines
  - Process updates and improved controls
