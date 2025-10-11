# Custom Instructions Setup Guide

> Use this handbook to configure personal Custom Instructions in GitHub Copilot clients (VS Code, the Copilot Chat web app, etc.) and keep them aligned with the `.copilot/` project settings.

## Why Custom Instructions Matter
- **Capture personal preferences**: Document your preferred language, output format, or frequently used commands so you spend less time repeating them.
- **Augment team conventions**: When `.copilot/config.json` defines shared rules, Custom Instructions can record your role-specific responsibilities or recurring scenarios.
- **Reuse across projects**: Your settings follow you to other repositories, keeping Copilot tailored to your workflow everywhere.

## Configuration Steps
### VS Code Client
1. Open the command palette (`Ctrl/Cmd + Shift + P`) and run “Copilot: Open Custom Instructions”.
2. Fill in the two text areas (“What should Copilot know about you?” and “How should Copilot respond?”).
3. Paste or adapt the templates below and save—changes take effect immediately.

### GitHub.com Copilot Chat (Web)
1. Visit [https://github.com/copilot](https://github.com/copilot) and sign in.
2. In the left navigation, choose **Custom Instructions**.
3. Enter or update the text fields and save.

> The configuration syncs to your Copilot account, so all editors pick up the same instructions.

## Suggested Templates
### 1. Personal Preferences (“What should Copilot know about you?”)
```
I communicate primarily in English and prefer concise commands and explanations.
Common stack: GitHub Actions, Markdown documentation, and the workflows recommended by this template.
Default to the guidance in the repository `docs/` directory; if anything conflicts, defer to repository rules.
Generate shell commands that run on macOS with zsh by default.
Avoid exposing machine-specific details (username, hostname, absolute paths); substitute generic placeholders when needed.
```

### 2. Response Expectations (“How should Copilot respond?”)
```
Reply in English with a friendly, structured tone and emphasize actionable steps.
Respect the style guidance in `.copilot/config.json`:
- Use clear sections or bullet lists in Markdown.
- Explain background and caveats when suggesting workflows or configuration changes.
- Flag documentation and test updates when public interfaces change.
When details are missing, list the information you need before proceeding.
```

Add role-specific notes as needed (e.g., security review responsibilities, log formatting preferences).

## Working with `.copilot/config.json`
- The repository file captures team-wide conventions while Custom Instructions record personal additions; both apply simultaneously.
- If conflicts arise, Copilot blends both inputs, but explicitly reminding Copilot to prioritize repository rules helps.
- Revisit your personal instructions whenever `.copilot/config.json` changes.

## Privacy and Sensitive Data
- Review AI-generated content to ensure it does not disclose personal data, hostnames, API tokens, or local file paths.
- When referencing local paths or commands, swap user- or host-specific details with placeholders such as `<USER>` or `<HOST>`.
- If a response still leaks sensitive details, edit or scrub it before committing.
- The repository CI bundles `.github/scripts/check_sensitive_info.py`; run `python3 .github/scripts/check_sensitive_info.py` locally before committing for an early check.
- Document stricter filtering requirements in `.copilot/` or elsewhere when you need them and explain their priority inside Custom Instructions.

## Team Collaboration Tips
- When completing `docs/github/repo-setup-checklist.md`, remind newcomers to configure their Custom Instructions.
- Encourage teammates to share reusable prompts in `docs/ai/prompt-library.md`.
- If roles are well defined, note ownership or approval responsibilities within each person’s instructions.

## Frequently Asked Questions
- **Can we export or reuse templates?**
  - Copilot does not yet provide scripted import/export. Store recommended text inside this repository so teammates can copy it manually.
- **How should multilingual teams proceed?**
  - Ask teammates to note their preferred language in personal instructions and specify the default language in repository guidance; maintain localized templates when necessary.
- **How do I confirm the instructions are active?**
  - Ask Copilot Chat “What do you know about me?” or “Draft a PR summary that follows the repository rules” and check whether the response reflects your instructions.

## Maintenance and Updates
- Update this document and its templates whenever you release a new version or adjust your workflow.
- Log changes in the release checklist within `docs/process/release-management.md` so everyone stays informed.
