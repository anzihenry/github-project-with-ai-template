# Release Management Workflow

Use this workflow to ensure releases remain traceable and reversible when shipping from the template.

## Pre-Release Checklist
- [ ] Define the release scope by collecting merged issues and pull requests.
- [ ] Verify CI/CD pipelines are green.
- [ ] Revisit the security baseline via `docs/github/security-baseline.md` to make sure configurations stay aligned.
- [ ] Review CodeQL scan results and confirm no unresolved high/medium alerts remain—or that remediation plans exist.
- [ ] Update documentation, including the README, changelog, and deployment notes.

## Release Steps
1. **Create a release branch (optional)**: `release/<version>`.
2. **Tag the version**: follow semantic versioning or the team’s chosen scheme.
3. **Prepare release notes**:
   - Key changes and highlights
   - Breaking changes and migration steps
   - Security fixes and risk considerations
4. **Publish the release**: add notes on the GitHub Release page and upload assets if needed.
5. **Notify stakeholders**: broadcast through team channels and link to the release entry.

## Post-Release Follow-up
- Monitor key metrics or user feedback and respond promptly.
- Record lessons learned in `docs/process/post-release-retro.md` (create it if necessary).
- Execute rollback plans if critical issues surface.
- Review commit history to ensure it follows `docs/github/commit-message-guidelines.md`, simplifying changelog generation and retrospectives.

## Rollback Strategy
- Use Git tags to locate the last stable version quickly.
- Document the cause, impact, and remediation plan for the rollback.
- Summarize takeaways in an issue or discussion and update this workflow when needed.

## Ongoing Maintenance
- Reassess the release workflow each quarter and revise documentation as required.
- Confirm Copilot guidance and review checklists stay current.
