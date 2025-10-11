# Commit Message Guidelines (Conventional Commits)

> This document follows the widely adopted [Conventional Commits](https://www.conventionalcommits.org/) standard to keep commit history consistent, readable, and automation-friendly.

## 核心格式
Every commit message uses the following structure:
```
<type>(<scope>): <subject>

<body>

<footer>
```

- `type`: the category of change (see the recommended list below).
- `scope` (optional): the area affected, such as a module, directory, or component.
- `subject`: a single-line summary describing **what** changed (avoid ending with a period).
- `body` (optional): background details, implementation notes, or motivation; separate paragraphs with blank lines.
- `footer` (optional):
  - Reference issues: `Refs #123` / `Fixes #123`
  - Declare breaking changes: `BREAKING CHANGE: description`

## Recommended Types
| type | Purpose | Example |
| ---- | ------- | ------- |
| `feat` | New feature or capability | `feat(api): add project bootstrap endpoint` |
| `fix` | Bug fix | `fix(ci): correct linter cache path` |
| `docs` | Documentation updates | `docs(github): write commit guide` |
| `style` | Formatting or stylistic changes (no logic) | `style: adjust Markdown list indent` |
| `refactor` | Code restructuring without new features or fixes | `refactor(prompt): simplify default prompts` |
| `perf` | Performance improvements | `perf(ci): speed up workflow downloads` |
| `test` | Test-related changes | `test(workflow): cover actionlint scenario` |
| `build` | Build system or dependency updates | `build: bump Node.js requirement` |
| `ci` | CI/CD configuration changes | `ci(codeql): extend Python analysis` |
| `chore` | Miscellaneous tasks not affecting production code | `chore: update CODEOWNERS placeholder` |
| `revert` | Revert a specific commit | `revert: feat(api): add project bootstrap endpoint` |

> If you introduce new types, agree on them as a team and update this guide plus tooling configurations.

## Writing Tips
- **Keep subjects concise**: Aim for 50 characters or less, describing what changed; explain the rationale in the body.
- **Use consistent language**: Match the repository’s primary language (typically English for this template).
- **Flag breaking changes**: Include a `BREAKING CHANGE:` section describing the migration path.
- **Reference issues**: Stick to a consistent format such as `Fixes #123` or `Refs #123` for automation.

## Examples
```
feat(workflow): add CodeQL security scan

Add codeql.yml workflow with javascript-typescript as the default matrix.
Also update the README and security baseline docs to highlight the change.

Refs #45
```
```
docs(ai): 编写 custom instructions 指南

- add docs/ai/custom-instructions.md
- update prompt-library.md to reference the new guide
```
```
refactor: reorganize repository setup checklist

BREAKING CHANGE: checklist now includes a CodeQL step; existing projects must adopt the configuration.
```

## Process and Tooling
- Reference this guide in `docs/github/repo-setup-checklist.md` so new repositories follow it.
- Enforce the rules automatically with tools such as:
  - [commitlint](https://commitlint.js.org/) via CI or pre-commit hooks.
  - [husky](https://typicode.github.io/husky/) or other Git hook managers.
- Add checklist items to PR templates to keep commit history consistent.

## FAQ
- **Is scope required?** Use it when multiple modules or languages coexist; otherwise, omit it.
- **Why keep types in English with localized subjects?** Types power automation and stay short; write subjects in the repository’s primary language for readability.
- **How to handle multiple topics?** Split the work into separate commits so each message focuses on a single change.

Add more examples or stack-specific guidance after team discussions to keep this document relevant.