# CHANGELOG.md · 仓库级变更

## 仓库 · 2026-10-08

**建库**：仿 `ae-tools` 建 C4D monorepo **`c4d-tools`**，成为 C4D 插件/工具的唯一源码源。

并入 3 个原独立仓库：

| 模块 | 来自原仓库 | 类型 |
|---|---|---|
| `plugins/c4d-mesh-face-sorter/` | `Simiely/c4d-mesh-face-sorter` | C4D 插件 `.pyp` |
| `plugins/c4d-userdata-manager/` | `Simiely/c4d-userdata-manager` | C4D 插件 `.pyp` |
| `tools/oc-plugin-activator/` | `Simiely/oc-plugin-activator` | Windows 工具 |

- 原仓库内容全部搬入本仓，**不含**其 `.github/workflows`（不启用 CI/Pages）
- 3 个原仓库随后**归档只读**，README 顶部指向本仓
