# 贡献指南

感谢你愿意为此 GitHub 项目模版贡献力量！以下步骤与建议可帮助你快速上手并保持贡献的一致性。

## 基础要求
- 阅读 `README.md` 与 `docs/github/repo-setup-checklist.md` 了解模版结构。
- 保持所有文档使用中文撰写，确保术语统一。
- 在提交 Pull Request 前，请先创建或关联对应的 Issue。

## 开发流程
1. Fork 或克隆仓库，建议使用独立分支进行修改。
2. 如需新增配置，请确保同时更新相关文档（例如 `docs/ai`、`docs/process`）。
3. 完成修改后，运行必要的校验（例如 `act` 运行 GitHub Actions、本地 linter 等）。
4. 提交 Pull Request 时，遵循 `.github/PULL_REQUEST_TEMPLATE.md` 中的清单，并确保 CI 通过。

## 代码与文档风格
- 配置文件尽可能添加注释或链接，解释关键参数。
- Markdown 文档使用二级标题划分段落，并提供简洁的列表说明。
- 对于 Copilot 相关文件，请参考 `docs/ai/copilot-guidelines.md`。

## Issue 与讨论
- 使用模板提交 Issue，并提供必要上下文与重现步骤。
- 对于功能建议，请说明业务背景与潜在收益。

## 发布与版本
- 模版的版本发布将通过 GitHub Releases 管理，变更记录见 `docs/process/release-management.md`。
- 新增重大功能时，请附带迁移或升级指引。

如果你对贡献流程有疑问，可在讨论区发起话题或提交 Issue。再次感谢你的支持！