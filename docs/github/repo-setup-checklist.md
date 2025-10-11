# 仓库初始化清单

> 用于从模版创建新仓库后的第一周内完成必要配置。

## 基础信息
- [ ] 更新 `README.md`：填写项目简介、目标、主要联系人和常用渠道。
- [ ] 将 `.github/CODEOWNERS` 替换为真实的团队或个人，确保评审责任明确。
- [ ] 审核 `LICENSE` 是否与项目策略一致，必要时同步更新版权年份与主体。

## GitHub 配置
- [ ] 设置默认分支（通常为 `main`），并启用分支保护：
  - 至少一名代码所有者审批后才能合并。
  - 禁止直接推送到默认分支，限制强制推送。
  - 将关键 CI 工作流设为必需状态检查。
- [ ] 根据需要调整 Issue/PR 模板、Discussion、Projects 等协作功能。
- [ ] 与团队确认提交信息规范，建议遵循 `docs/github/commit-message-guidelines.md` 并配合工具校验。
- [ ] 配置团队权限（Maintain、Write、Read），遵循最小权限原则。

## 自动化与安全
- [ ] 运行 `.github/workflows/` 中的 CI 检查，确认能够在新仓库正常执行。
- [ ] 根据项目技术栈扩展或新增工作流（例如构建、测试、发布）。
- [ ] 调整 `dependabot.yml` 覆盖所需的依赖生态（npm、pip、go modules 等）。
- [ ] 启用 Dependabot Alerts、Secret Scanning、Push Protection（若计划支持），并确认通知接收人。
- [ ] 审查第三方 GitHub Actions，固定版本为带 SHA 的引用或稳定 tag。
- [ ] 建立必需的 GitHub Secrets，限制权限并记录轮换计划。
- [ ] 参考 `docs/github/codeql-usage.md` 启用并验证 `codeql.yml` 工作流，确保默认分支定期完成扫描。

## Copilot 与 AI 配置
- [ ] 根据团队需求调整 `.copilot/config.json` 的指南、风格与作用域。
- [ ] 在 `docs/ai/prompt-library.md` 中加入项目特定提示语，供团队复用。
- [ ] 指引新成员按照 `docs/ai/custom-instructions.md` 配置个人 Custom Instructions，说明“以仓库规范为准”。
- [ ] 阅读并分享 `docs/ai/copilot-guidelines.md`，统一 Copilot 使用方式和审查标准。

## 文档与流程
- [ ] 更新 `CONTRIBUTING.md`、`SECURITY.md` 中的联系邮箱与流程，确保真实可用。
- [ ] 在 `docs/process/` 目录补充或调整项目特有的开发、发布、运维流程。
- [ ] 建立最初的里程碑、版本规划存档，并记录在 `docs/process/release-management.md`。
- [ ] 若面向外部贡献者，可提供英文摘要或在 README 中链接多语言版本。

完成上述步骤后，建议使用 Pull Request 记录初始化过程，便于团队回顾与追踪配置变更。