# Branch Strategy Guidelines

## Main Branch
- Treat `main` (or `master`) as the stable release branch and merge via pull requests only.
- Enable branch protection: require at least one reviewer approval and disallow direct pushes.
- Mark CI workflows as required status checks to safeguard quality.

## Feature Branches
- Naming convention: `feature/<concise-description>`.
- Keep feature branches short-lived and delete them after merging.
- For cross-team efforts, clarify owners and review scope within the related issue.

## Fix Branches
- Naming convention: `fix/<issue-number>` or `hotfix/<summary>`.
- Include a rollback plan in urgent fix pull requests.
- After the fix merges, sync the change back to `develop` or other long-lived branches.

## Release Branches (Optional)
- Naming convention: `release/<version>`.
- Freeze features targeted for the release, complete final testing, and polish documentation.
- Upon release, merge the branch into both the main branch and the long-lived development branch, then tag the release.

## Workflow Tips
- Use the pull request process for every branch to ensure changes stay transparent and auditable.
- Label PRs with purpose-driven tags (e.g., `feat`, `fix`, `docs`) to simplify retrospectives.
- Capture branch strategy outcomes and lessons learned in `docs/process/release-management.md` for future reference.
