# AGENTS.md · 项目规则

> 📌 **文档基线**：2026-10-08（commit `<本提交>`）本仓库转为**索引仓库**（插件代码退回各自独立仓库）
> **更新索引后，请更新此行**（日期 + 新 commit hash），并在 CHANGELOG 追加。

## 本仓库定位（重要）
- `c4d-tools` 是**索引仓库**：**只放文档 + 新插件骨架 `_template/`**，不放任何插件源码。
- 各插件的源码 / 构建 / 发行都在**各自的独立仓库**里，本仓库只维护一张索引表。

## 约定
- 🔴 **不要**把任何插件源码（`.pyp` / `res/`）、发行包提交进本仓库
- 🔴 **不要**归档插件仓库 —— 归档后 **Releases 与 Pages 变只读，新版发不了、落地页也改不了**
- 新增插件：README「插件一览」加一行 → CHANGELOG 加节
- 表格里的**最新版本 / 最近更新**取自各仓库的 Releases 与 push 时间，改版后记得同步
- `_template/` 是本仓库**唯一的例外**（骨架不是产物）；⚠️ 它不能放进 `plugins/` 下，会被 C4D 误当插件

## 关键坑（随开发补充）
- `.pyp` 是**编译产物**：由 C4D Python SDK 编译而来；改动请保留可复现的源码/流程
- C4D 插件目录须与插件同名；`res/` 放图标与符号

## 相关
- 其它索引仓库：[`pc-tools`](https://github.com/Simiely/pc-tools) ·
  [`ae-tools`](https://github.com/Simiely/ae-tools) ·
  [`blender-addons`](https://github.com/Simiely/blender-addons)
