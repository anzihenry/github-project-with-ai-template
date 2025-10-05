# Copilot 使用指南

## 配置概览
- `.copilot/config.json` 定义了项目级别的提示语与风格约束。
- 建议在组织或团队范围内同步此配置，确保生成内容保持一致。
- 若仓库语言多样，可在 `scopes` 中针对不同文件类型编写差异化指引。

### Custom Instructions
- Custom Instructions 属于个人层面的补充配置，可在 VS Code 或 Copilot Chat 网页端设置。
- 推荐参照 `docs/ai/custom-instructions.md` 提供的模板填写，并在内容中声明“以仓库规范为准”。
- 当 `.copilot/config.json` 更新或团队流程调整时，请同步校准个人指令，以免冲突。

## 日常使用建议
1. **明确上下文**：在提问或生成代码前，简要描述业务背景与预期输出。
2. **迭代验证**：对 Copilot 生成的结果进行审阅，必要时通过补充提示进行迭代。
3. **保留人工判断**：关键安全、性能或合规决策需维护者复核，避免直接信任自动生成内容。

## 推荐工作流
- 使用 Copilot Chat 快速了解模版结构：
  - `@workspace /explain` 获取当前文件或目录概览。
  - `@workspace /tests` 生成或完善验证用例。
- 使用 `docs/ai/prompt-library.md` 中的标准提示，以便重复使用。
- 若需要规格驱动开发流程，可参照 `docs/ai/spec-kit-integration.md` 引入 Spec Kit 并结合 `/specify`、`/plan` 等指令。

## 常见场景
| 场景 | 建议提示 | 注意事项 |
| ---- | -------- | -------- |
| 新增工作流 | “请帮我生成一个用于检查 YAML 语法的 GitHub Actions 工作流。” | 明确触发条件与权限设置 |
| 更新文档 | “为新加入的安全策略撰写中文 README 段落。” | 确保术语与其它文档一致 |
| 代码评审 | “根据模版的评审清单，帮我审阅以下 PR diff。” | 仍需人工确认评审结论 |

## 升级与维护
- 定期关注 Copilot 官方更新，适时调整配置字段。
- 记录在 `docs/process/release-management.md` 中，并在发布说明里同步变更。
- 对于团队培训，可将指南拓展为内部 Wiki 或视频示例。
