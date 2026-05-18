# AI Use Case Approval Workflow

## High-Level Flow Description

This workflow guides AI project teams from initial intake through final approval, production monitoring, and incident response. It starts with a standardized intake form, classifies the use case into a risk tier, assigns required controls and approvals, and tracks responsibilities across product, ML, security, legal, and compliance.

1. Intake
   - Project team completes the intake form with business objective, stakeholders, data categories, expected users, and impacted populations.
   - The intake form captures key contextual information needed for risk classification.

2. Risk Classification
   - Review the intake information against three risk dimensions: data sensitivity, autonomy level, and regulatory exposure.
   - Assign the use case to a risk tier: Low, Medium, or High.

3. Controls and Approvals
   - Map the risk tier to required controls, documentation, and approval gates.
   - For Medium and High tiers, involve more rigorous review and additional governance.

4. Roles and Responsibilities
   - Assign a RACI matrix for the approval workflow so each function understands its role in decision-making, review, and control implementation.

5. Lifecycle Checkpoints
   - Apply checkpoints at design, development, pre-deployment review, production monitoring, and incident response stages.
   - Ensure controls remain active through the lifecycle and that any incidents trigger Board or governance review.

6. Review and Audit
   - Document decisions, approvals, and follow-up actions.
   - Keep a record of intake forms, tiering rationale, required controls, and monitoring outcomes for audit and continuous improvement.

## Intake Form Fields

- Business objective and stakeholder summary
- Primary and secondary stakeholders
- Data categories used (public, internal, personal, sensitive, regulated)
- Expected users and impacted populations
- Autonomy level of the AI system
- Deployment environment and integration points
- Regulatory scope and geographic jurisdictions
- Intended monitoring and verification plans

## Risk Tier Mapping

| Risk Tier | Key Dimensions | Controls | Required Approvals |
| --- | --- | --- | --- |
| Low | Data sensitivity is limited, autonomy is advisory or support-only, regulatory exposure is minimal | Basic documentation, periodic review, standard data protection controls | Team lead and product owner approval |
| Medium | Data includes personal or sensitive categories, autonomy supports decisions, regulatory exposure exists | Model card, data documentation, human-in-the-loop for key steps, privacy review, security review | Product owner, ML lead, security reviewer, compliance reviewer |
| High | Data includes regulated or high-risk categories, autonomy enables or affects decisions, significant regulatory or reputational exposure | Formal ethics board review, continuous monitoring, strict access control, external legal review, full privacy impact assessment | AI Ethics Board, legal, security, compliance, executive sponsor |

## RACI for Approval Workflow

| Activity | Product | ML | Security | Legal | Compliance |
| --- | --- | --- | --- | --- | --- |
| Intake form completion | R | A | C | C | C |
| Risk tier classification | C | R | C | C | C |
| Controls definition | A | R | C | C | C |
| Approval decision | C | C | C | C | A |
| Pre-deployment review | C | R | C | C | A |
| Production monitoring plan | C | R | A | C | C |
| Incident response readiness | C | R | A | C | A |

## Lifecycle Checkpoints

- Design
  - Confirm business objective, data sources, and privacy requirements.
  - Validate that the use case is in scope for the approval workflow.

- Development
  - Ensure documentation is created for data, model, and controls.
  - Track changes that could affect risk tier or approvals.

- Pre-deployment Review
  - Verify that all required controls are in place.
  - Confirm that reviewers have signed off on risk, privacy, security, and compliance.

- Production Monitoring
  - Maintain active monitoring for accuracy, bias, security, and user impact.
  - Review operational metrics periodically and escalate anomalies.

- Incident Response
  - Trigger incident response when a model failure, data issue, or safety concern occurs.
  - Conduct a post-incident review and update the approval workflow as needed.

## Notes

- A standardized intake form and clear tier definitions make the workflow repeatable and auditable.
- High-risk cases require the most rigorous governance and should be revisited at each major update.
- The RACI matrix ensures that the right functions are involved and accountable throughout the lifecycle.
