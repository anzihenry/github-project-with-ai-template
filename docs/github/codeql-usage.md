# CodeQL Workflow Guide

Use this guide to enable and customize CodeQL scanning in new projects so your team can continuously detect security issues.

## Workflow Overview
- The template includes a baseline CodeQL workflow at `.github/workflows/codeql.yml`.
- Default triggers:
  - Pushes to the `main`/`master` branch.
  - Pull requests targeting `main`/`master`.
  - A weekly scheduled run (Monday at 03:00 UTC).
- The default language matrix scans `javascript-typescript`; extend it as needed.

## Enablement Steps
1. On GitHub.com, ensure **Security > Code security and analysis** has “CodeQL code scanning” enabled.
2. Align the default branch and workflow triggers with your branching strategy; adjust the trigger list if necessary.
3. Update the `schedule` cron expression to change frequency or time zone.

## Extending Languages
- Add languages to `matrix.language`, for example:
  ```yaml
  matrix:
    language: ["javascript-typescript", "python", "go"]
  ```
- Consult the [CodeQL documentation](https://docs.github.com/en/code-security/code-scanning) to verify language support.
- For languages requiring manual builds (e.g., C/C++, Java), replace or augment the `autobuild` step with your own build commands.

## Custom Queries
- Load additional rules via the `packs` or `queries` options in `github/codeql-action/init`:
  ```yaml
  with:
    languages: ${{ matrix.language }}
    packs: codeql/<language>-security-extended@latest
  ```
- Maintain custom query packs in the repository and reference them through the `queries` parameter when needed.

## Reviewing and Triaging Results
- Findings appear under **Security > Code scanning alerts** in your repository.
- Establish a response workflow:
  - Assign owners to track high-priority alerts.
  - Reference alert IDs in PRs and describe remediation steps.
  - Mark false positives directly in GitHub or refine queries to exclude them.

## Complementary Security Measures
- Combine this workflow with the security baseline in `docs/github/security-baseline.md` to ensure Dependabot, Secret Scanning, and other protections stay active.
- Include a “CodeQL scan clear of high-risk alerts” item in the pre-release checklist at `docs/process/release-management.md`.

## FAQ
- **Workflow takes too long**: Reduce the language matrix, trim query packs, or enable `fail-fast`.
- **Build failures**: Disable `autobuild`, add explicit build steps, and confirm dependencies are available.
- **Too many alerts**: Prioritize by severity, define resolution SLAs, and refine custom queries when patterns emerge.

After completing setup, check off the corresponding step in `docs/github/repo-setup-checklist.md` to confirm CodeQL is operational in the new repository.