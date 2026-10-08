# AGENTS.md · 项目规则

> 📌 **文档基线**：2026-10-08（commit `a199149`）建库：3 个 C4D 仓库并入
> **更新文档/代码后，请更新此行**（日期 + 新 commit hash），并在 CHANGELOG 追加。

## 技术栈
- Cinema 4D Python 插件（`.pyp`）；目标版本见各插件 README
- 自研插件：纯 Python + C4D Python SDK（`c4d`）
- 交付：`plugins/<插件名>/`（`.pyp` + `res/`）
- **例外**：`tools/oc-plugin-activator/` 是 Windows 外围工具（Python + 可打包 exe）

## 约定
- 注释用中文；UI 标签 / 插件名用中文
- 版本号写在插件内，与 `CHANGELOG` 对应节一致
- 新增插件：`plugins/<名>/` → README「工具总览」加行 → CHANGELOG 加节 → DEVELOPMENT 加章节
- **公开仓库红线**：不收录凭据、个人信息、**本地绝对路径**、未公开项目细节

## 关键坑（随开发补充）
- `.pyp` 是**编译产物**：由 C4D Python SDK 编译而来；改动请保留可复现的源码/流程
- C4D 插件需在 `plugins/<名>/` 下与目录同名；`res/` 放图标与符号
