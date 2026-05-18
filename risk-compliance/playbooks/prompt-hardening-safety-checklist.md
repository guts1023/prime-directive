# Prompt Hardening & Safety Checklist

## Purpose

A checklist for AI safety engineers, product teams, and prompt reviewers to harden prompts and prevent misuse in enterprise AI applications.

## Design-Time Checks

- Define the prompt’s purpose clearly and keep system instructions concise.
- Specify allowed behavior and explicit refusal criteria for unsafe or sensitive requests.
- Avoid using real PII, confidential business information, or proprietary data in prompt templates.
- Classify the prompt by sensitivity level before it is added to the prompt library.
- Document the prompt’s intended use case, audience, and risk profile.
- Review prompts for ambiguous or open-ended instructions that could lead to unintended output.
- Ensure prompts do not expose internal architecture or system details unnecessarily.

## Pre-Deployment Review

- Validate that prompt templates use safe default behavior and explicit refusal rules.
- Test prompts against known injection patterns and adversarial examples.
- Confirm input validation rules are defined for incoming user content.
- Check that prompt templates do not include sensitive or proprietary details.
- Ensure the prompt has been reviewed and approved by a second team member.
- Verify version control is enabled for prompt templates and changes are logged.
- Confirm the prompt’s sensitivity classification is up to date and reviewed periodically.

## Runtime and Monitoring Checks

- Enable runtime filters to block or flag unsafe outputs, including hate, violence, illegal advice, and privacy violations.
- Monitor model responses for unexpected or disallowed content.
- Log prompt usage, input context, and decision outcomes for audit and analysis.
- Use content moderation layers to inspect outputs before they are delivered to users.
- Implement alerting for high-risk prompt patterns or repeated misuse attempts.
- Periodically review prompt performance and update templates based on real-world behavior.
- Retire or modify prompts that generate unsafe, biased, or inappropriate outputs.

## Enterprise Prompt Library Controls

- Maintain a prompt inventory with sensitivity labels, ownership, and review status.
- Enforce prompt classification by data sensitivity, user audience, and impact severity.
- Require approval for new prompts and changes to existing high-sensitivity templates.
- Version prompts and keep a changelog for all edits.
- Store prompt templates in a secured repository with access controls.
- Conduct periodic prompt library audits to ensure compliance with safety policies.

## Additional Mitigations

- Use explicit system-level instructions to constrain behavior and define refusal language.
- Sanitize or normalize user inputs before incorporating them into prompts.
- Avoid concatenating raw user inputs directly into system prompts without controls.
- Separate prompt templates from runtime variables to minimize injection risk.
- Train the model to respond safely to out-of-scope or malicious inputs.

## Notes

- Treat this checklist as a living document; update it as new threats and use cases emerge.
- Apply stricter controls for prompts used in production, customer-facing, or regulated environments.
