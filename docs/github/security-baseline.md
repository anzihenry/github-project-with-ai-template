# 安全基线指南

本指南帮助你在使用模版创建新项目时，快速完成安全加固。

## 身份与访问控制
- 使用最小权限原则：仅为必要成员授予写入或管理员权限。
- 对管理员启用双重认证，并鼓励团队成员开启。
- 定期复查团队与集成的访问权限，至少每季度一次。

## 依赖与供应链
- 保持 `.github/dependabot.yml` 生效，确保 GitHub Actions 依赖及时更新。
- 对关键 Action 使用固定版本号或 SHA，避免 `@master` 等漂移引用。
- 若项目包含语言依赖（npm、pip 等），建议增加相应的 Dependabot 配置块。

## 机密与凭证
- 避免将密钥写入仓库，统一通过 GitHub Secrets 或环境变量管理。
- 周期性轮换密钥，并启用使用日志审计（如 GitHub Audit Log）。
- 对自动化机器人账号使用细粒度 PAT，并限制在必要仓库范围内。

## 检测与响应
- 启用以下 GitHub Security 功能：
  - Dependabot alerts
  - Secret scanning
  - Push Protection（如组织或企业版可用）
- 将安全通知与团队协作工具集成，确保及时处理。
- 制定安全事件处理流程，参考 `SECURITY.md` 中的联系方式。

## Copilot 相关安全
- 在 `.copilot/config.json` 中定义敏感区域提示，提醒使用者谨慎处理密钥或个人信息。
- 对自动生成的配置或脚本，务必人工审查其安全性。
- 定期更新 `docs/ai` 中的指南，纳入最新的安全策略与案例。

## 持续改进
- 将安全基线纳入 `docs/process/release-management.md` 的发布检查中。
- 每次版本发布前执行一次安全基线回顾，确保配置未偏离。
- 鼓励团队提交安全改进建议，并通过 Issue 跟踪落实。
