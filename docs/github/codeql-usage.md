# CodeQL 工作流使用指南

本指南介绍如何在新项目中启用与定制 CodeQL 扫描，帮助团队持续发现潜在安全漏洞。

## 工作流概览
- 模版已在 `.github/workflows/codeql.yml` 中集成基础的 CodeQL 扫描。
- 默认触发条件：
  - 推送到 `main`/`master` 分支。
  - 针对 `main`/`master` 的 Pull Request。
  - 每周一次的定时任务（周一 UTC 03:00）。
- 默认扫描语言矩阵包含 `javascript-typescript`，可按需扩展。

## 启用步骤
1. 确保仓库在 GitHub.com 的 **Security > Code security and analysis** 中启用了 “CodeQL code scanning”。
2. 将仓库中的默认分支与团队使用的分支策略保持一致，必要时修改触发分支名单。
3. 如需更改定时任务频率或时区，更新 `schedule` 段落中的 `cron` 表达式。

## 扩展扫描语言
- 在工作流的 `matrix.language` 中追加值，例如：
  ```yaml
  matrix:
    language: ["javascript-typescript", "python", "go"]
  ```
- 参考 [CodeQL 官方文档](https://docs.github.com/en/code-security/code-scanning) 确认目标语言是否受支持。
- 若语言需要手动构建（例如 C/C++、Java），请替换或扩展 `autobuild` 步骤，添加自定义构建脚本。

## 自定义查询
- 通过 `github/codeql-action/init` 的 `packs` 或 `queries` 参数加载额外规则：
  ```yaml
  with:
    languages: ${{ matrix.language }}
    packs: codeql/<language>-security-extended@latest
  ```
- 也可在仓库中维护自定义查询集，将其路径传入 `queries` 字段。

## 结果查看与处理
- 扫描结果会显示在仓库的 **Security > Code scanning alerts** 页面。
- 建议建立响应流程：
  - 分配负责人跟进高优先级告警。
  - 在 PR 中引用告警 ID，说明修复措施。
  - 对误报可在 GitHub 界面直接标记 False Positive，或在查询中进行排除。

## 与其他安全措施的配合
- 结合 `docs/github/security-baseline.md` 提供的安全基线，确保 Dependabot、Secret Scanning 等功能已开启。
- 在 `docs/process/release-management.md` 的发布前检查项中增加“CodeQL 扫描无未解决高风险告警”。

## 常见问题
- **工作流耗时较长**：尝试减少语言数量、按需调整查询包，或设置 `fail-fast`。
- **构建失败**：禁用 `autobuild`，改用显式的 `build` 步骤；确保依赖齐全。
- **告警过多**：按优先级处理，必要时在团队中明确解决 SLA，并更新自定义查询策略。

配置完成后，请记得在 `docs/github/repo-setup-checklist.md` 中勾选相关步骤，确保新仓库也能正确运行 CodeQL。