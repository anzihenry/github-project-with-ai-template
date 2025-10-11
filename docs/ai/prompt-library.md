# Copilot Prompt Library

> Copy these prompts directly into Copilot Chat and tailor them to your scenario.

## Fundamentals
- **Understand a file’s role**:
  ```
  Read <file path> and summarize its primary responsibilities, inputs/outputs, and configuration nuances to watch.
  ```
- **Generate documentation**:
  ```
  Following the repository’s documentation style, draft an English section describing <feature/config>, including purpose, usage steps, and caveats.
  ```

## Automation Setup
- **Create a workflow**:
  ```
  Goal: Add a GitHub Actions workflow for <requirement>.
  Constraints:
  - Trigger only under <conditions>.
  - Use officially maintained actions.
  - Include inline comments explaining each step.
  ```
- **Refine dependency update policy**:
  ```
  Review .github/dependabot.yml, suggest improvements, and provide the updated configuration snippet with clear comments.
  ```

## Review Assistance
- **Pull request check**:
  ```
  Given the PR description and key diffs below, list additional questions or risks based on the contribution guide and security policy.
  ```
- **Workflow risk review**:
  ```
  Assess the following GitHub Actions workflow for security concerns, evaluate third-party actions, and recommend least-privilege adjustments.
  ```

## Documentation & Onboarding
- **New member onboarding**:
  ```
  Create a 5-step quick-start checklist for new contributors based on the repository README and docs directory.
  ```
- **Release announcement**:
  ```
  Using docs/process/release-management.md, draft a release announcement for version vX.Y.Z covering major changes, upgrade steps, and cautions.
  ```

## Custom Prompts
- Maintain shared prompts in this file and notify the team after updates.
- Tailor prompts for specific languages or frameworks by clarifying context and style expectations.
- For long-term storage inside the Copilot client, adapt the template in `docs/ai/custom-instructions.md`.
