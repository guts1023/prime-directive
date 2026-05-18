# AI Risk Scoring Model

## Narrative Explanation

This AI risk scoring model uses a tiered approach to evaluate systems based on the sensitivity of data they handle, their autonomy level, and the regulatory or reputational impact of their use. Each dimension is scored independently, then combined into an overall risk tier. The model also maps each tier to required documentation, governance approval, and monitoring expectations so that controls scale with risk.

## Scoring Rubric and Tier Thresholds

| Dimension | Score 1 | Score 2 | Score 3 | Score 4 | Score 5 |
| --- | --- | --- | --- | --- | --- |
| Data Sensitivity | Public, non-sensitive | Internal use only | Personal data | Sensitive personal / financial | Regulated / highly sensitive data |
| Autonomy Level | Advisory / informational only | Decision-support with human review | Semi-autonomous decisions with human oversight | Automated decisions in low-risk contexts | Fully automated decisions affecting individuals or groups |
| Regulatory / Reputational Impact | Minimal impact, internal use | Low impact, limited external use | Moderate impact with some regulatory touchpoints | High impact, regulated sector or public-facing | Very high impact, critical infrastructure, safety, or legal exposure |

### Risk Tier Thresholds

- **Low risk:** total score 3–6
- **Medium risk:** total score 7–10
- **High risk:** total score 11–13
- **Very high risk:** total score 14–15

## Tier-to-Controls Mapping

| Risk Tier | Required Documentation | Required Governance | Monitoring Expectations |
| --- | --- | --- | --- |
| Low | Basic project summary; data classification note | Product owner or team lead approval | Periodic review during development and deployment; basic health checks |
| Medium | Model card, data documentation, privacy note, risk assessment | Product owner, ML lead, security review | Regular monitoring of performance and safety metrics; quarterly review |
| High | Comprehensive model card, data sheet, DPIA/PiA, risk mitigation plan | Formal review by security, compliance, legal, and ML governance | Continuous or frequent monitoring; monthly metric reviews; alerting for anomalies |
| Very high risk | Full governance package, external validation records, incident playbook | AI Ethics Board or equivalent executive governance body approval | Continuous monitoring with automated alerts, weekly reporting, and incident escalation procedures |

## Notes

- Scores are additive across dimensions. For example, a use case with sensitive personal data (4), semi-autonomous decisions (3), and high regulatory impact (4) would total 11, placing it in the high-risk tier.
- The model is intentionally simple to support repeatable scoring while ensuring higher-risk systems receive stronger documentation and oversight.
- Adjust thresholds and controls based on organizational context, industry, and regulatory requirements.
