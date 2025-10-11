# GitHub Project Template

This repository provides a project template centered on GitHub automation and Copilot collaboration, helping you bootstrap new initiatives quickly while keeping team workflows consistent.

## Feature Highlights
- ✅ Standardized issue/PR templates and CODEOWNERS configuration.
- ✅ Built-in GitHub Actions workflows for YAML validation and baseline linting via Super Linter.
- ✅ Dependabot configuration for automated GitHub Actions dependency updates.
- ✅ CodeQL security scanning workflow accompanied by English usage guidance.
- ✅ Copilot configuration, Custom Instructions template, and prompt library tailored for team collaboration.
- ✅ Comprehensive onboarding collateral: repository setup checklist, security baseline, branch policy, and lifecycle documentation.

## Quick Start
1. Use this repository as a template to create your new project.
2. Complete the initialization tasks listed in `docs/github/repo-setup-checklist.md`.
3. Adjust `.github/workflows/` (including `ci.yml`, `codeql.yml`, etc.), `dependabot.yml`, and `.copilot/config.json` to fit your stack.
4. Configure Copilot Custom Instructions following `docs/ai/custom-instructions.md`.
5. Review the guidance in `docs/ai`, `docs/github`, and `docs/process` to align with the recommended practices.

## Documentation Map
- GitHub configuration guidance: `docs/github/`
- Copilot usage and AI collaboration: `docs/ai/`
- Project lifecycle and operations: `docs/process/`
- Contribution and conduct policies: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`

> Start with `docs/github/codeql-usage.md` for CodeQL setup details.
> Refer to `docs/github/commit-message-guidelines.md` to standardize commit messages.

## Adaptation Tips
- Add stack-specific build/test workflows under `.github/workflows/` as needed.
- Extend `docs/github/security-baseline.md` to reflect your organization’s security policies.
- Provide localized documentation in the `docs` directory if the team operates in multiple languages.

## Roadmap
- [ ] Supply one-click workflow examples for popular stacks (Node.js, Python, etc.).
- [ ] Expand the prompt library with more Copilot usage scenarios.
- [ ] Broaden security scanning coverage (e.g., infrastructure-as-code, container images).

Contributions via issues and pull requests are welcome—let’s refine this template together!
