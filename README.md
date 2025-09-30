# GitHub 项目模版

此仓库提供一个以 GitHub 自动化与 Copilot 协作为核心的项目模版，帮助你快速启动新项目并保持团队流程一致。

## 功能概览
- ✅ 标准化的 Issue/PR 模板与代码所有者配置。
- ✅ 内置 GitHub Actions 工作流：YAML 语法校验、Super Linter 基础检查。
- ✅ Dependabot 自动更新 GitHub Actions 依赖。
- ✅ Copilot 配置、Custom Instructions 模板与提示语库，支持中文团队协作。
- ✅ 完整的仓库初始化清单、安全基线、分支策略与流程文档。

## 快速开始
1. 使用此仓库作为模版创建新仓库。
2. 按照 `docs/github/repo-setup-checklist.md` 完成初始化配置。
3. 根据实际项目调整 `.github/workflows/`、`dependabot.yml` 和 `.copilot/config.json`。
4. 参考 `docs/ai/custom-instructions.md` 在 Copilot 客户端配置个人 Custom Instructions。
5. 阅读 `docs/ai`、`docs/github` 与 `docs/process`，了解建议流程与最佳实践。

## 文档导航
- GitHub 配置指南：`docs/github/`
- Copilot 使用规范：`docs/ai/`
- 项目流程管理：`docs/process/`
- 贡献与行为准则：`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`

## 适配建议
- 若项目包含特定技术栈，可在 `.github/workflows/` 中追加对应的构建/测试工作流。
- 根据组织安全策略扩展 `docs/github/security-baseline.md`。
- 针对多语言团队，可在 `docs` 目录中提供英文摘要或翻译版本。

## 后续计划
- [ ] 添加常见语言（Node.js、Python 等）的一键构建工作流示例。
- [ ] 提供更丰富的 Copilot 场景提示。
- [ ] 集成更多安全扫描工具（如 CodeQL）。

欢迎通过 Issue 与 Pull Request 贡献改进意见，与我们一起完善这个模版！
