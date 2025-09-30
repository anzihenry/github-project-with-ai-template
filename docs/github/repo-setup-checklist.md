# 仓库初始化清单

在使用此模版创建新项目后，请按照下列步骤完成仓库初始化，确保配置一致。

## 基础信息
- [ ] 更新 `README.md`，描述项目背景、目标与使用方式。
- [ ] 替换 `CODEOWNERS` 中的默认团队或用户。
- [ ] 检查 `LICENSE` 是否符合项目要求，如需更换请同步更新。

## GitHub 配置
- [ ] 启用分支保护（至少针对 `main/master`），限制强制推送与直接合并。
- [ ] 配置默认工作流状态检查，确保 CI 通过后才能合并。
- [ ] 设置 Issue 与 PR 模板的默认选项，简化重复工作。

## 自动化与安全
- [ ] 确认 `.github/workflows/` 目录中 CI 能正常运行，并根据技术栈补充额外工作流。
- [ ] 调整 `dependabot.yml` 支持项目依赖生态（如 npm、pip、go modules）。
- [ ] 启用 Dependabot Alerts、Secret Scanning、Code Scanning（视仓库计划与权限而定）。

## Copilot 与 AI 配置
- [ ] 根据团队需求调整 `.copilot/config.json` 的指南与风格。
- [ ] 在 `docs/ai/prompt-library.md` 中加入项目特定的提示。
- [ ] 与团队沟通 Copilot 最佳实践，参考 `docs/ai/copilot-guidelines.md`。

## 文档与流程
- [ ] 根据实际流程更新 `CONTRIBUTING.md` 与 `SECURITY.md` 中的联系信息。
- [ ] 在 `docs/process` 中追加项目特定的流程说明（如发布节奏、上线规范）。
- [ ] 若项目面向外部贡献者，提供中英文对照或英文摘要（视需求而定）。

完成上述步骤后，即可将仓库作为标准化模版对外或内部团队使用。# 仓库初始化清单

> 用于从模版创建新仓库后的第一周内完成必要配置。

## 基础配置
- [ ] 更新 `README.md` 中的项目简介、负责人和联系渠道。
- [ ] 在 `.github/CODEOWNERS` 中替换为真实团队或个人。
- [ ] 检查 `.copilot/config.json` 并根据项目语言补充额外范围。

## 分支与权限
- [ ] 设置默认分支（通常为 `main`）。
- [ ] 启用分支保护规则：
  - 必须通过 CI。
  - 至少一名代码所有者批准。
  - 禁止直接向默认分支推送。
- [ ] 配置所需的团队权限（Maintain、Write、Read 等）。

## 安全与合规
- [ ] 在仓库 "Settings > Security" 中启用 Dependabot alerts、Secret scanning。
- [ ] 为需要的工作流机密创建 GitHub Secrets，并最小化权限范围。
- [ ] 审查并确认 `.github/workflows` 中的第三方 Action 版本。

## 自动化
- [ ] 启用 CI/CD 工作流（如 `CI 基础校验`）。
- [ ] 配置 Dependabot 通知邮件或 Slack 集成。
- [ ] 评估是否需要其他自动化（CodeQL、Release Drafter 等）。

## 文档
- [ ] 根据项目特点完善 `docs/` 目录，补充架构或接口说明。
- [ ] 更新 `docs/ai/prompt-library.md`，加入项目特有的提示语。
- [ ] 记录初始里程碑、版本规划与团队约定。

在完成上述步骤后，建议通过 Pull Request 记录初始化过程，确保团队成员能够追溯配置变更历史。