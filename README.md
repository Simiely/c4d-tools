# c4d-tools · Cinema 4D 插件集

个人 **Cinema 4D** 插件的**总管仓库** —— 所有 C4D 插件的**唯一源码源**，直接在这里迭代开发。
原独立仓库已**归档只读**，只作为历史快照保留（见文末「相关仓库」）。

## 插件一览

| 插件 | 源码位置 | 类型 | 最新版本 |
|---|---|---|---|
| **网格面排序器** Mesh Face Sorter | [`plugins/c4d-mesh-face-sorter/`](./plugins/c4d-mesh-face-sorter) | C4D 插件 `.pyp` | v2.0.6 |
| **用户数据管理器** User Data Manager | [`plugins/c4d-userdata-manager/`](./plugins/c4d-userdata-manager) | C4D 插件 `.pyp` | v2.1.0 |

> 🔍 排序器：按面数 / 存储大小排列场景中的所有多边形物体。
> 用户数据管理器：快速创建和管理用户数据（User Data），供 Xpresso / Python / 表达式直接调用。

## 目录结构

```
c4d-tools/
├─ README.md · AGENTS.md · DEVELOPMENT.md · CHANGELOG.md   四件套文档
├─ plugins/       C4D 插件（.pyp + res/）→ 复制到 C4D 的 plugins 目录
└─ _template/     新 C4D 插件骨架（⚠️ 不能放 plugins/ 下，会被 C4D 误当插件）
```

## 安装

把插件**整个子目录**（含 `.pyp` 与 `res/`）复制到 C4D 的 `plugins/` 目录：

```
C:\Program Files\Maxon Cinema 4D <版本>\plugins\
```

重启 C4D → 顶部 **扩展（Extensions）** 菜单里即可看到。

## 发版约定

插件**统一在本仓库发版**：tag 形如 `<插件名>-vX.Y.Z`（例 `c4d-mesh-face-sorter-v2.0.6`），
Release 附件放打包好的插件 zip。原独立仓库已归档，**不再发版**。

## 新插件骨架

`_template/` 是本仓库内**唯一的非插件内容** —— 新 C4D 插件的骨架
（`PluginTemplate.py` + 说明）。新建插件时把它复制到 `plugins/<插件名>/` 起手。

> ⚠️ 别把 `_template/` 放进 `plugins/` 下 —— 会被 C4D 误当成插件加载。

## 说明

- **一个总管管全部 C4D 插件**：源码、Issue 都在本仓库。插件体积小、发版少，不值得「一插件一仓」；
- 新增插件：`plugins/<名>/` → README「插件一览」加行 → CHANGELOG 加节；
- 文档规范遵循 [knowledge-base 单项目规范](https://github.com/Simiely/knowledge-base)。

## 相关仓库

| 原独立仓库 | 处理 | 对应内容 |
|---|---|---|
| `c4d-mesh-face-sorter` | 📦 已归档（只读） | `plugins/c4d-mesh-face-sorter/` |
| `c4d-userdata-manager` | 📦 已归档（只读） | `plugins/c4d-userdata-manager/` |

> 归档只为**封存历史快照** —— 归档不会删除已发布的 Release（下载链接仍可用），只是不能再发新版。
>
> 另有 [`oc-plugin-activator`](https://github.com/Simiely/oc-plugin-activator)（OctaneRender 缓存清理 / 资源部署）
> 是 **Windows 工具、不是 C4D 插件**，不属本仓库，归 [`pc-tools`](https://github.com/Simiely/pc-tools) 索引。
>
> 其它领域：[`pc-tools`](https://github.com/Simiely/pc-tools)（PC 工具索引）·
> [`ae-tools`](https://github.com/Simiely/ae-tools)（After Effects）·
> [`blender-addons`](https://github.com/Simiely/blender-addons)（Blender 插件）
