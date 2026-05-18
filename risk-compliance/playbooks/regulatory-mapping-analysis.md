# Regulatory Mapping Analysis for AI Use Case

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. All findings should be reviewed and validated by qualified legal counsel before relying on them for compliance decisions.

## Regulatory Landscape Summary

### Potentially Relevant Laws and Regulations by Jurisdiction

#### European Union

- **EU AI Act**
  - Applies to AI systems with risk levels from minimal to unacceptable.
  - Likely relevant if the use case processes personal or sensitive data, supports automated decisions, or is deployed in the EU.
- **GDPR**
  - Applies to any processing of personal data of EU residents.
  - Relevant when data categories include personal, sensitive, or behavioral data.
- **ePrivacy Directive / ePrivacy Regulation**
  - Relevant if the system processes electronic communications metadata or uses cookies/tracking in consumer-facing applications.
- **Sector-specific rules**
  - Financial services: PSD2, MiFID II, AML directives for customer onboarding or credit decisions.
  - Healthcare: GDPR plus any national healthcare data protection laws.

#### United States

- **Federal Trade Commission (FTC) Act**
  - Applies to unfair or deceptive practices, including misuse of consumer data or AI-driven decisions.
- **HIPAA**
  - Relevant for healthcare AI that processes protected health information (PHI).
- **Gramm-Leach-Bliley Act (GLBA)**
  - Relevant for financial services AI handling customer financial data.
- **State privacy laws**
  - California Consumer Privacy Act (CCPA)/California Privacy Rights Act (CPRA), Virginia CDPA, Colorado CPA, etc.
  - Relevant if the AI use case processes personal data of residents in those states.
- **Sectoral regulations**
  - Banking, healthcare, insurance, and telecommunications may impose additional AI or data controls.

#### United Kingdom

- **UK GDPR**
  - Applies to personal data processing in the UK.
- **UK AI Strategy / emerging AI regulation**
  - Monitor evolving UK AI governance guidance and proposed safety regulations.
- **Sector-specific privacy and conduct rules**
  - Financial Conduct Authority (FCA) guidance, NHS data standards, etc.

#### Other Jurisdictions

- **Canada**
  - Personal Information Protection and Electronic Documents Act (PIPEDA) / provincial privacy laws.
- **Australia**
  - Privacy Act 1988 and Australian Information Commissioner guidance on AI.
- **Brazil**
  - Lei Geral de Proteção de Dados (LGPD).
- **Singapore**
  - Personal Data Protection Act (PDPA) and AI governance principles.

### Common AI Governance Standards and Frameworks

- **NIST AI Risk Management Framework (AI RMF)**
  - Relevant for structuring risk management across Govern, Map, Measure, and Manage.
- **ISO/IEC 27001**
  - Information security management standard applicable to AI systems processing sensitive data.
- **ISO/IEC 42001**
  - Emerging AI management system standard for governance and oversight.
- **OECD AI Principles**
  - Helpful for high-level fairness, transparency, accountability, and human-centered design guidance.
- **Industry guidelines**
  - Financial services: BCBS, EU EBA, or FSB guidance on AI and machine learning.
  - Healthcare: HIPAA/HITECH guidance, FDA AI/ML software as a medical device (SaMD) considerations.

## Mapping Table

| Regulation / Standard               | Requirement or Principle                                           | How This AI Use Case May Be Affected                                                                                       | Suggested Control or Documentation                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| EU AI Act                           | Risk tiering and required safeguards for high-risk AI              | If the system is used in the EU and performs decision-support or high-impact functions, it may be classified as high-risk. | Document risk tier, implement transparency measures, and maintain conformity assessment records.                    |
| GDPR                                | Lawful basis, data minimization, transparency, data subject rights | If personal data is used, the system must document processing purposes, minimize data use, and enable rights requests.     | Create a data protection impact assessment (DPIA) and privacy notice; maintain consent/legitimate interest records. |
| ePrivacy / cookies rules            | Consent for tracking and communication metadata processing         | If the system uses behavioral data from EU web or app users, you must obtain consent and manage cookies.                   | Implement cookie consent management and data flow mapping for communications data.                                  |
| FTC Act                             | No unfair/deceptive practices, reasonable data security            | Consumer-facing AI must avoid misleading outputs and protect user data.                                                    | Define acceptable use policies; perform security and fairness testing; retain records of user disclosures.          |
| CCPA / CPRA                         | Consumer rights, disclosure, opt-out, data minimization            | If data from California residents is used, provide required privacy notices and opt-out mechanisms.                        | Maintain a CCPA compliance register and support data subject requests.                                              |
| HIPAA                               | PHI protection, minimum necessary, breach notification             | Healthcare AI using PHI must implement administrative, technical, and physical safeguards.                                 | Document HIPAA compliance controls, conduct security risk assessments, and train staff.                             |
| GLBA                                | Safeguards rule, privacy rule, pretexting protections              | Financial AI processing customer financial data must protect confidentiality and notify customers of privacy practices.    | Create an information security program and privacy policy; document vendor oversight.                               |
| NIST AI RMF                         | Risk management across Govern/Map/Measure/Manage                   | Provides a structured approach for identifying and mitigating AI risk.                                                     | Use the Prime Directive prompt library to map artifacts to NIST functions and document risk management activities.  |
| ISO/IEC 27001                       | Information security management system                             | Relevant whenever the AI system stores/processes sensitive or regulated information.                                       | Maintain ISMS documentation, asset inventories, risk assessments, and control implementation records.               |
| ISO/IEC 42001                       | AI management system requirements                                  | Relevant for organizations seeking formal AI governance certification and consistent oversight.                            | Document AI policies, risk criteria, oversight roles, and continuous improvement activities.                        |
| OECD AI Principles                  | Responsible stewardship, transparency, accountability              | Useful for framing ethical design and stakeholder obligations.                                                             | Publish an AI ethics policy and conduct ethical impact reviews.                                                     |
| Sector-specific finance guidance    | Model risk management, governance, explainability                  | If the AI use case supports financial decisions, it may need specialized controls and audit trails.                        | Document model governance, explainability controls, and validation processes.                                       |
| Sector-specific healthcare guidance | Patient safety, clinical validation, data protection               | Healthcare AI may require clinical validation and privacy safeguards.                                                      | Maintain clinical evaluation records, safety monitoring plans, and privacy impact assessments.                      |

## Notes

- This mapping is illustrative and should be tailored to the specific AI use case, data flows, jurisdictions, and industry context.
- The accuracy of applicable laws depends on the actual jurisdictions, the exact data categories used, and the business model.
- Legal review is required before finalizing any compliance program or controls.
