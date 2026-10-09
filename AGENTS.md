# AGENTS.md · 项目规则

> 📌 **文档基线**：2026-10-09（commit `9aa1e07`）撤销索引化，恢复为**总管仓库**（插件代码回仓）
> **更新文档/代码后，请更新此行**（日期 + 新 commit hash），并在 CHANGELOG 追加。

## 本仓库定位（重要）
- `c4d-tools` 是 C4D 插件的**总管仓库**：**插件的源码、文档、Issue 都在这里**。
- 插件小而发版少，**不拆成一插件一仓**；原独立仓库已**归档只读**、只作历史快照。
- **发版在本仓库**：tag 形如 `<插件名>-vX.Y.Z`。

## 技术栈
- Cinema 4D Python 插件（`.pyp`）；目标版本见各插件 README
- 自研插件：纯 Python + C4D Python SDK（`c4d`）
- 交付：`plugins/<插件名>/`（`.pyp` + `res/`）

## 约定
- 注释用中文；UI 标签 / 插件名用中文
- 版本号写在插件内，与 `CHANGELOG` 对应节一致
- 新增插件：`plugins/<名>/` → README「插件一览」加行 → CHANGELOG 加节 → DEVELOPMENT 加章节
- **公开仓库红线**：不收录凭据、个人信息、**本地绝对路径**、未公开项目细节

## 关键坑（随开发补充）
- `.pyp` 是**编译产物**：由 C4D Python SDK 编译而来；改动请保留可复现的源码/流程
- C4D 插件需在 `plugins/<名>/` 下与目录同名；`res/` 放图标与符号
- **归档仓库不能再改**：要动已归档的原仓库，必须**先取消归档** → 改 → 再归档

## 相关
- 其它总管 / 索引：[`pc-tools`](https://github.com/Simiely/pc-tools) ·
  [`ae-tools`](https://github.com/Simiely/ae-tools) ·
  [`blender-addons`](https://github.com/Simiely/blender-addons)
