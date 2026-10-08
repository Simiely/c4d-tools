# c4d-tools

个人 **Cinema 4D** 插件 / 工具集（monorepo）—— 所有 C4D 插件与外围工具的**唯一源码源**。
仿 [**ae-tools**](https://github.com/Simiely/ae-tools) 的标准维护：一个仓库管全部、单一源码源、四件套文档、自写与工具分目录。

## 目录结构

```
c4d-tools/
├─ README.md · AGENTS.md · DEVELOPMENT.md · CHANGELOG.md   四件套文档
├─ plugins/      自研 · C4D 插件（.pyp + res/）→ 放进 C4D 的 plugins 目录
├─ tools/        非插件类工具（Windows 工具等）
├─ _template/    新 C4D 插件骨架（⚠️ 不能放 plugins/ 下，会被误当插件）
├─ tips/         C4D 使用技巧知识库
└─ releases/     发行包归档
```

## 工具总览

| 工具 | 源码位置 | 类型 | 状态 | 原独立仓库 |
|---|---|---|---|---|
| 网格面排序器 Mesh Face Sorter | [`plugins/c4d-mesh-face-sorter/`](./plugins/c4d-mesh-face-sorter) | C4D 插件 `.pyp` | 稳定 | `Simiely/c4d-mesh-face-sorter` |
| 用户数据管理器 User Data Manager | [`plugins/c4d-userdata-manager/`](./plugins/c4d-userdata-manager) | C4D 插件 `.pyp` | 稳定 | `Simiely/c4d-userdata-manager` |
| OC 插件激活工具 OC Plugin Activator | [`tools/oc-plugin-activator/`](./tools/oc-plugin-activator) | Windows 工具（Python / exe） | 稳定 | `Simiely/oc-plugin-activator` |

## 安装

### C4D 插件（`plugins/` 下的两项）
1. 把对应插件**整个子目录**（含 `.pyp` 与 `res/`）复制到 C4D 的 `plugins/` 目录
   - Windows 默认：`C:\Program Files\Maxon Cinema 4D <版本>\plugins\`
2. 重启 C4D → 顶部 **扩展（Extensions）** 菜单里即可看到

### OC 插件激活工具（`tools/oc-plugin-activator`）
详见该目录内的 README（Windows 下运行 `oc_tool.py` 或打包好的 exe）。

## 文档规范

按 [knowledge-base](https://github.com/Simiely/knowledge-base) 的**单项目文档规范**维护四件套：
`README`（用户）/ `AGENTS`（AI 与协作者）/ `DEVELOPMENT`（开发者）/ `CHANGELOG`（变更）。

## 相关仓库

本仓库为 C4D 插件/工具的**唯一维护处**。原独立仓库的内容均已并入本仓库，原仓库归档只读：

| 原仓库 | 处理 | 对应内容 |
|---|---|---|
| `c4d-mesh-face-sorter` | 已归档（只读） | `plugins/c4d-mesh-face-sorter/` |
| `c4d-userdata-manager` | 已归档（只读） | `plugins/c4d-userdata-manager/` |
| `oc-plugin-activator` | 已归档（只读） | `tools/oc-plugin-activator/` |
