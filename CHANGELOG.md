# CHANGELOG.md · 仓库级变更

## 仓库 · 2026-10-08 · **由 monorepo 转为索引仓库**

- **删除全部插件副本**：`plugins/c4d-mesh-face-sorter/`、`plugins/c4d-userdata-manager/`、
  `tools/oc-plugin-activator/`，以及空壳 `releases/`（仅 `.gitkeep`）与 `tips/`（219 B 占位）
- 四件套改写为**索引性质**（README 变为插件索引表；DEVELOPMENT 说明「本仓不放插件代码」）
- **`_template/` 保留** —— 新插件骨架，是本仓库唯一的非文档内容（已在 AGENTS 标为唯一例外）
- **3 个原仓库解冻**（撤销归档）并剥离「已归档 / 已并入 c4d-tools」横幅，恢复**独立开发与发版**：
  `c4d-mesh-face-sorter` · `c4d-userdata-manager` · `oc-plugin-activator`
- **`oc-plugin-activator` 不属本仓库**：它是 **Windows 工具**（非 C4D 插件），索引改挂
  [`pc-tools`](https://github.com/Simiely/pc-tools)
- **原因**：GitHub 仓库归档后 **releases / tags / Pages 亦为只读**，无法发布新版本、也无法更新落地页。
  改由「**各插件仓库独立维护 + 本仓库做索引**」，源码只保留一份。

---

## 仓库 · 2026-10-08 · （已撤销）

**建库**：仿 `ae-tools` 建 C4D monorepo **`c4d-tools`**，成为 C4D 插件/工具的唯一源码源。

并入 3 个原独立仓库：

| 模块 | 来自原仓库 | 类型 |
|---|---|---|
| `plugins/c4d-mesh-face-sorter/` | `Simiely/c4d-mesh-face-sorter` | C4D 插件 `.pyp` |
| `plugins/c4d-userdata-manager/` | `Simiely/c4d-userdata-manager` | C4D 插件 `.pyp` |
| `tools/oc-plugin-activator/` | `Simiely/oc-plugin-activator` | Windows 工具 |

- 原仓库内容全部搬入本仓，**不含**其 `.github/workflows`（不启用 CI/Pages）
- 3 个原仓库随后**归档只读**，README 顶部指向本仓
