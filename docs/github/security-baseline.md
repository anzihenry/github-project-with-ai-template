# Security Baseline Guide

Follow this guide after creating a project from the template to harden security quickly.

## Identity and Access Control
- Apply least-privilege access: grant write or admin rights only when necessary.
- Enforce two-factor authentication for administrators and encourage the rest of the team to enable it.
- Review team and integration permissions at least quarterly.

## Dependencies and Supply Chain
- Keep `.github/dependabot.yml` enabled so GitHub Actions dependencies stay current.
- Pin critical actions by version or SHA; avoid floating references such as `@master`.
- If your project introduces language-specific dependencies (npm, pip, etc.), add matching Dependabot configurations.

## Secrets and Credentials
- Do not commit secrets to the repository; manage them via GitHub Secrets or environment variables.
- Rotate credentials on a schedule and enable audit logging where available.
- Use fine-grained PATs for automation accounts and scope them to required repositories only.

## Detection and Response
- Enable GitHub security features:
  - Dependabot alerts
  - Secret scanning
  - Push Protection (when available)
- Turn on CodeQL Code Scanning and ensure `.github/workflows/codeql.yml` runs successfully with timely alert triage.
- Integrate security notifications with your collaboration tools so the team can act quickly.
- Define an incident response process and reference the contact details in `SECURITY.md`.

## Copilot Security Considerations
- Use `.copilot/config.json` to highlight sensitive areas and remind users to handle secrets with care.
- Manually review any generated configuration or scripts for security implications.
- Update the guidance in `docs/ai` regularly as new security strategies or case studies emerge.

## Continuous Improvement
- Include this baseline in the pre-release checklist found in `docs/process/release-management.md`.
- Conduct a security baseline review ahead of each release to confirm nothing drifted.
- Track CodeQL alerts over time and summarize action items during retrospectives.
- Encourage the team to propose security enhancements and document follow-up in issues.
