# Commit Message 规范（Conventional Commits）

> 本文档基于目前广泛采用的 [Conventional Commits](https://www.conventionalcommits.org/) 规范，帮助团队保持一致、可读、可自动化处理的提交信息。

## 核心格式
每条提交信息结构如下：
```
<type>(<scope>): <subject>

<body>

<footer>
```

- `type`：提交类型（详见下文推荐枚举）。
- `scope`（可选）：影响范围，如模块、目录、组件。
- `subject`：一句话描述变更，使用中文或与仓库语言一致的简体中文，避免句号结尾。
- `body`（可选）：补充背景、实施细节或变更动机，段落之间空一行。
- `footer`（可选）：
  - 引用 Issue：`Refs #123` / `Fixes #123`
  - 提供破坏性变更说明：`BREAKING CHANGE: 描述`。

## 推荐类型
| type | 说明 | 示例 |
| ---- | ---- | ---- |
| `feat` | 新功能或特性 | `feat(api): 新增项目初始化接口` |
| `fix` | 缺陷修复 | `fix(ci): 修复 lint 步骤缓存路径` |
| `docs` | 文档更新（README、指南等） | `docs(github): 编写 commit 规范` |
| `style` | 格式、样式调整（不影响逻辑） | `style: 调整 Markdown 列表缩进` |
| `refactor` | 重构，既不是新功能也不是修复缺陷 | `refactor(prompt): 精简默认提示` |
| `perf` | 性能优化 | `perf(ci): 缩短工作流下载时间` |
| `test` | 测试相关变更 | `test(workflow): 覆盖 actionlint 场景` |
| `build` | 构建系统或依赖调整 | `build: 更新 node 版本要求` |
| `ci` | CI/CD 配置变更 | `ci(codeql): 扩展 Python 分析` |
| `chore` | 其他杂项，通常不影响生产代码 | `chore: 更新 CODEOWNERS 占位` |
| `revert` | 回滚特定提交 | `revert: feat(api): 新增项目初始化接口` |

> 如需新增类型，请在团队内约定，并更新本文件与相关工具配置。

## 编写建议
- **精炼摘要**：保持 50 个字符以内，描述“做了什么”，无需描述“为什么”，原因可写在 body。
- **中文优先**：配合团队语言，确保阅读体验一致；如需英文可在 body 中补充。
- **破坏性改动**：必须添加 `BREAKING CHANGE:` 段，说明升级策略。
- **关联 Issue**：使用统一格式 `Fixes #123` 或 `Refs #123` 方便自动化处理。

## 示例
```
feat(workflow): 添加 CodeQL 安全扫描

补充 codeql.yml 工作流，默认扫描 javascript-typescript 语言。
同时更新 README 与安全基线文档，提醒团队启用。

Refs #45
```
```
docs(ai): 编写 custom instructions 指南

- 新增 docs/ai/custom-instructions.md
- 更新 prompt-library.md，提醒可结合新指南使用
```
```
refactor: 调整仓库初始化清单

BREAKING CHANGE: checklist 增加 CodeQL 步骤，旧项目需补充相关配置。
```

## 流程与工具
- 将本规范纳入 `docs/github/repo-setup-checklist.md`，提醒新仓库遵循。
- 可结合以下工具实现自动化校验：
  - [commitlint](https://commitlint.js.org/)：在 CI 或 pre-commit 钩子中校验提交信息。
  - [husky](https://typicode.github.io/husky/) 或其他 Git hooks 管理工具。
- 在 PR 评审清单中加入检查项，确保提交历史保持一致。

## 常见问答
- **是否需要 scope？** 建议在团队盛行多个模块或语言时填写；如果不确定，可省略。
- **为何推荐英文类型 + 中文描述？** 这是目前较普遍的实践，类型用于自动化（英文简短规范化），subject/body 使用中文更易读。
- **如何处理多个主题？** 拆分为多次提交，每次提交聚焦单一目标。

如需扩展更多示例或结合具体技术栈的建议，请在讨论后补充到本文件。