# AI Use Case Approval SOP

## Purpose

This Standard Operating Procedure (SOP) defines the process for approving new AI use cases. It ensures that all AI projects are assessed consistently for risk, documented with appropriate controls, and reviewed by the right stakeholders before deployment.

## Scope

This SOP applies to all AI or machine learning initiatives within the organization, including new systems and significant changes to existing AI products. It covers intake, risk classification, governance approvals, lifecycle checkpoints, and audit documentation.

## Roles and Responsibilities

- **Project Team**: Completes the intake form, provides use case details, and implements required controls.
- **Product Owner**: Provides business context and approves low-risk projects.
- **ML Lead**: Evaluates model-related risks and documentation requirements.
- **Security Reviewer**: Reviews data and system safeguards.
- **Legal**: Reviews regulatory and contractual implications.
- **Compliance Reviewer**: Ensures documentation and controls meet internal standards.
- **AI Ethics Board**: Approves high-risk or sensitive AI use cases.

## Procedure

### 1. Intake

1. The project team completes the AI Use Case Intake Form, including:
   - Business objective and stakeholder summary.
   - Primary and secondary stakeholders.
   - Data categories used (public, internal, personal, sensitive, regulated).
   - Expected users and impacted populations.
   - Autonomy level of the AI system.
   - Deployment environment and integration points.
   - Regulatory scope and geographic jurisdictions.
   - Intended monitoring and verification plans.
2. Submit the completed intake form to the AI governance review queue.

### 2. Risk Classification

1. Review the intake information against the three key dimensions:
   - Data sensitivity
   - Autonomy level
   - Regulatory and reputational impact
2. Assign a risk tier:
   - Low
   - Medium
   - High
3. Document the risk tier rationale in the project record.

### 3. Controls and Approvals

1. Identify required controls based on the assigned risk tier.
2. Apply required documentation and approval gates:
   - **Low risk**: basic documentation, periodic review, standard data protection controls. Approval by team lead and product owner.
   - **Medium risk**: model card, data documentation, human-in-the-loop for key steps, privacy review, security review. Approval by product owner, ML lead, security reviewer, compliance reviewer.
   - **High risk**: formal ethics board review, continuous monitoring, strict access control, external legal review, full privacy impact assessment. Approval by AI Ethics Board, legal, security, compliance, and executive sponsor.
3. Record all approvals and required follow-up actions.

### 4. RACI and Accountability

The following roles must be engaged during the approval process:

| Activity | Product | ML | Security | Legal | Compliance |
| --- | --- | --- | --- | --- | --- |
| Intake form completion | R | A | C | C | C |
| Risk tier classification | C | R | C | C | C |
| Controls definition | A | R | C | C | C |
| Approval decision | C | C | C | C | A |
| Pre-deployment review | C | R | C | C | A |
| Production monitoring plan | C | R | A | C | C |
| Incident response readiness | C | R | A | C | A |

### 5. Lifecycle Checkpoints

Ensure the following checkpoints are completed and documented:

- **Design**
  - Confirm business objective, data sources, and privacy requirements.
  - Validate scope for the approval workflow.
- **Development**
  - Ensure documentation is created for data, model, and controls.
  - Track changes that could affect risk tier or approvals.
- **Pre-deployment Review**
  - Verify all required controls are in place.
  - Confirm that reviewers have signed off on risk, privacy, security, and compliance.
- **Production Monitoring**
  - Maintain active monitoring for accuracy, bias, security, and user impact.
  - Review operational metrics periodically and escalate anomalies.
- **Incident Response**
  - Trigger incident response for model failures, data issues, or safety concerns.
  - Conduct a post-incident review and update the approval workflow.

## Audit and Recordkeeping

- Maintain a record of each use case intake and approval decision.
- Document the risk tier rationale, control requirements, and review evidence.
- Archive completed intake forms, approvals, and monitoring reports for audit and continuous improvement.

## Review and Updates

This SOP should be reviewed annually or whenever there are material changes to AI governance policies, regulatory requirements, or organizational processes.
