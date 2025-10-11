# Repository Setup Checklist

> Complete these tasks during the first week after creating a new project from the template.

## Core Information
- [ ] Update `README.md` with the project overview, goals, key contacts, and communication channels.
- [ ] Replace `.github/CODEOWNERS` with the actual team or individuals to clarify review ownership.
- [ ] Confirm `LICENSE` aligns with project policy and update the copyright year or holder as needed.

## GitHub Configuration
- [ ] Set the default branch (typically `main`) and enable branch protection:
  - Require approval from at least one code owner before merging.
  - Block direct pushes and force pushes to the default branch.
  - Mark critical CI workflows as required status checks.
- [ ] Adjust issue/PR templates, Discussions, Projects, or other collaboration features as needed.
- [ ] Align on a commit-message convention—see `docs/github/commit-message-guidelines.md`—and enforce it with tooling.
- [ ] Configure team permissions (Maintain, Write, Read) following least-privilege principles.

## Automation and Security
- [ ] Run the workflows in `.github/workflows/` to verify they operate correctly in the new repository.
- [ ] Extend or add workflows for your stack (build, test, release, etc.).
- [ ] Update `dependabot.yml` to cover required ecosystems (npm, pip, go modules, etc.).
- [ ] Enable Dependabot Alerts, Secret Scanning, and Push Protection (where available) and confirm notification recipients.
- [ ] Review third-party GitHub Actions and pin to version tags or SHAs.
- [ ] Create required GitHub Secrets, minimize their scope, and record rotation plans.
- [ ] Follow `docs/github/codeql-usage.md` to enable and validate the `codeql.yml` workflow so it scans the default branch regularly.

## Copilot and AI Configuration
- [ ] Tailor `.copilot/config.json` to match team guidelines, tone, and scopes.
- [ ] Add project-specific prompts to `docs/ai/prompt-library.md` for easy reuse.
- [ ] Ask new members to configure personal Custom Instructions via `docs/ai/custom-instructions.md`, noting that repository rules are authoritative.
- [ ] Share `docs/ai/copilot-guidelines.md` to standardize Copilot usage and review expectations.

## Documentation and Process
- [ ] Update contact details and procedures in `CONTRIBUTING.md` and `SECURITY.md`.
- [ ] Extend `docs/process/` with project-specific development, release, or operations workflows.
- [ ] Establish initial milestones or version plans and record them in `docs/process/release-management.md`.
- [ ] Provide translations or summaries in the README if the project targets external or multilingual contributors.

Document the initialization work in a pull request so the team can track configuration changes easily.