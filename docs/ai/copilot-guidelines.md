# Copilot Usage Guide

## Configuration Overview
- `.copilot/config.json` defines project-level prompts and style guidelines.
- Share this configuration across the organization or team to keep Copilot outputs consistent.
- If the repository spans multiple languages, tailor guidance per file type inside the `scopes` section.

### Custom Instructions
- Custom Instructions are personal-level settings configured in VS Code or the Copilot Chat web app.
- Use the template in `docs/ai/custom-instructions.md` and explicitly state that repository rules take precedence.
- Revisit your personal instructions whenever `.copilot/config.json` or team processes change to avoid conflicts.

## Day-to-Day Recommendations
1. **Provide context**: Describe the business scenario and expected outcome before asking Copilot for help.
2. **Iterate and verify**: Review Copilot responses and refine prompts until the result satisfies requirements.
3. **Keep human oversight**: Maintainers should review safety-, performance-, or compliance-critical decisions rather than trusting generated output blindly.

## Suggested Workflows
- Use Copilot Chat to understand the template quickly:
  - `@workspace /explain` for a summary of the active file or directory.
  - `@workspace /tests` to generate or improve validation suites.
- Reuse the prompts listed in `docs/ai/prompt-library.md` for consistent interactions.
- If you adopt a spec-driven workflow, pair Copilot with tools such as Spec Kit (see `/specify`, `/plan`, etc.) and document how they integrate with your process.

## Common Scenarios
| Scenario | Suggested Prompt | Notes |
| -------- | ---------------- | ----- |
| Add a workflow | "Generate a GitHub Actions workflow that validates YAML syntax." | Define triggers and required permissions clearly |
| Update documentation | "Draft an English README section for the new security policy." | Keep terminology aligned with existing docs |
| Code review | "Review the following PR diff using the template's review checklist." | Always confirm Copilot's findings manually |

## Upgrades and Maintenance
- Track Copilot release notes and adjust configuration fields when new capabilities become available.
- Record changes in `docs/process/release-management.md` and announce them in release notes.
- Expand this guide into an internal wiki or video tutorials for team onboarding if needed.
