# Spec Kit 集成指南

> 将本模板与 [Spec Kit](https://github.com/github/spec-kit) 结合，构建围绕“规格驱动开发（Spec-Driven Development）”的协同流程。

## 目标与收益
- **统一的规格产出**：通过 `/constitution`、`/specify`、`/plan` 等指令生成结构化需求与技术方案，与仓库现有流程文档互补。
- **跨工具一致性**：Spec Kit 支持 GitHub Copilot、Cursor、Claude 等主流智能体，可在多工具环境中使用同一套规格。
- **自动化延伸**：结合仓库现有 CI 与隐私扫描，可实现“规格 → 代码 → 校验”的闭环体验。

## 准备工作
- Python 3.11+（推荐使用 [uv](https://docs.astral.sh/uv/) 管理）
- `git` 已安装并正确配置
- 可访问 GitHub Releases 下载 Spec Kit 依赖

```bash
# 推荐使用 uv 安装 specify CLI
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 单次试用可改用
uvx --from git+https://github.com/github/spec-kit.git specify --help
```

> macOS + zsh 环境下如遇 `uv` 未安装，可执行 `curl -LsSf https://astral.sh/uv/install.sh | sh`，然后按提示将 `uv` 加入 PATH。

## 将 Spec Kit 引入现有仓库
### 1. 备份与清理工作区
- 确保当前工作区 `git status` 干净，或在新分支中操作。
- 由于 `specify init` 会生成模板文件，建议先创建 `spec-kit` 专用目录或新分支。

### 2. 初始化 Spec Kit 结构
```bash
# 在仓库根目录执行，--here 表示复用当前目录，--ai copilot 匹配使用的智能体
specify init --here --ai copilot --force
```

初始化后将新增以下关键目录：

| 目录/文件 | 作用 | 与本模板的衔接建议 |
| --- | --- | --- |
| `memory/constitution.md` | 项目原则、守则 | 可与 `docs/process/project-lifecycle.md` 对齐，必要时互相引用 |
| `memory/specs/` | 功能规格与需求说明 | 对应 `docs/` 下的业务文档，可放在 `docs/specs/` 子目录统一管理 |
| `templates/` | 任务脚本与提示模板 | 与 `docs/ai/prompt-library.md` 对照，挑选适用场景融合 |
| `.github/workflows/specify.yml` | (可选) 自动化工作流示例 | 若有冲突需合并现有 CI 与新流程 |

> 若不想污染主目录，可在 `docs/spec-kit/` 下保留 Spec Kit 生成的 artifact，并在 `.spec-kit/config.toml` 中调整输出路径。

### 3. 配置团队协同
- 将 `memory/constitution.md` 的关键原则同步到 `docs/ai/custom-instructions.md` 的模板或团队规范中。
- 为 Copilot Chat 预设新增 Spec Kit 指令说明，帮助成员理解 `/specify`、`/plan` 与 `/implement` 的顺序与依赖。
- 在 PR 模板或评审清单中增加“规格对齐”检查项，确认实现与最新 Spec 一致。

### 4. 自动化集成
- 在 `.github/workflows/` 新建独立工作流，运行 `specify check` 确保必要工具可用。
- 结合仓库已有的 `check_sensitive_info.py`，在 Spec 文档变动时同样触发隐私扫描，避免泄露本地路径。
- 根据需要编写脚本，将 `memory/specs/*.md` 自动同步到 `docs/` 对应目录，减少手工维护。

## 推荐工作流程
1. **定义原则**：运行 `/constitution` 形成团队共识，并回写到 `docs/process/`。
2. **撰写规格**：使用 `/specify`、`/clarify` 输出明确的业务需求，提交至 `memory/specs/`。
3. **技术方案**：通过 `/plan`、`/tasks` 获取技术路线与任务分解，可选地转换为 GitHub Issues。
4. **执行实现**：依托 `/implement` 或手动完成任务，提交代码前运行本仓库的 lint + 隐私检查。
5. **回顾同步**：完成后更新 Spec、文档与发行说明，确保 `docs/` 与 `memory/` 保持一致。

## 常见问题
- **与现有文档冲突？** 建议在 Spec Kit 生成的文档顶部注明“来源于 Spec Kit”，并在 PR 中明确同步策略。
- **如何限制生成内容？** 结合仓库 `.copilot/config.json` 的风格约束，在 `/plan` 或 `/implement` 时强调“遵循仓库规范”。
- **团队成员缺少安装权限？** 可提供 `uvx` 的一次性执行脚本，或在 CI 中集中执行规格生成与校验。

## 参考链接
- [Spec Kit 官方仓库](https://github.com/github/spec-kit)
- [Spec-Driven Development Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [Specify CLI 用法](https://github.com/github/spec-kit#-specify-cli-reference)
