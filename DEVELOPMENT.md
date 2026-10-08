# DEVELOPMENT.md · 仓库说明与索引

本文件是**门面 + 索引**：只放仓库级信息与入口，细节走各子目录。

## 项目概览

`c4d-tools` 是个人 C4D 插件/工具的 **monorepo**：所有 C4D 插件与外围工具的**唯一源码源**。

演进：**2026-10-08 建库** —— 把原先分散的 3 个独立仓库整合进来（原有各自独立四件套与 CI）。

## 结构

```
c4d-tools/
├─ plugins/       自研 C4D 插件（.pyp + res/）
├─ tools/         非插件类工具
├─ _template/     新插件骨架
├─ tips/          技巧知识库（先占位，后生长）
└─ releases/      发行包归档
```

`install.py` / `verify.py`（仿 ae-tools 的部署器与验收脚本）**预留**，视 C4D 部署方式二期再做。

## 迁入记录

| 模块 | 来自原仓库 | 类型 | 状态 |
|---|---|---|---|
| `plugins/c4d-mesh-face-sorter/` | `Simiely/c4d-mesh-face-sorter` | C4D 插件 `.pyp` | 稳定 |
| `plugins/c4d-userdata-manager/` | `Simiely/c4d-userdata-manager` | C4D 插件 `.pyp` | 稳定 |
| `tools/oc-plugin-activator/` | `Simiely/oc-plugin-activator` | Windows 工具 | 稳定 |

## 每次改动的动作清单

| 场景 | 动作 |
|---|---|
| 新增插件 | `plugins/<名>/` 加目录 → README「工具总览」加行 → CHANGELOG 加节 → DEVELOPMENT 加章节 |
| 发版 | 插件内版本号升级 + `CHANGELOG.md` 加节 |
| 任何提交后 | 更新 `AGENTS.md` 顶部的**文档基线行**（日期 + 新 commit hash） |
