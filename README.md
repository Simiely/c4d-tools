# c4d-tools · Cinema 4D 插件索引

> 🔖 **本仓库是索引仓库（导航中心），不放任何插件代码。**
> 每个插件的**开发、构建、发行**都在它**自己的独立仓库**里进行 —— 点下表链接直达。

## 插件一览

| 插件 | 说明 | 类型 | 最新版本 | 最近更新 |
|---|---|---|---|---|
| **[`c4d-mesh-face-sorter`](https://github.com/Simiely/c4d-mesh-face-sorter)** | 🔍 按面数 / 存储大小排列场景中的所有多边形物体 | C4D 插件 `.pyp` | [`v2.0.6`](https://github.com/Simiely/c4d-mesh-face-sorter/releases/latest) | 2026-08-24 |
| **[`c4d-userdata-manager`](https://github.com/Simiely/c4d-userdata-manager)** | 快速创建和管理用户数据（User Data），供 Xpresso / Python / 表达式直接调用 | C4D 插件 `.pyp` | [`v2.1.0`](https://github.com/Simiely/c4d-userdata-manager/releases/latest) | 2026-07-03 |

## 安装

把插件**整个子目录**（含 `.pyp` 与 `res/`）复制到 C4D 的 `plugins/` 目录：

```
C:\Program Files\Maxon Cinema 4D <版本>\plugins\
```

重启 C4D → 顶部 **扩展（Extensions）** 菜单里即可看到。

## 新插件骨架

`_template/` 是本仓库内**唯一的非文档内容** —— 新 C4D 插件的骨架
（`PluginTemplate.py` + 说明）。新建插件时把它复制到 `plugins/<插件名>/` 起手。

> ⚠️ 别把 `_template/` 放进 `plugins/` 下 —— 会被 C4D 误当成插件加载。

## 说明

- **一个插件一个仓库**：源码、Issue、Releases（含落地页）都在各自仓库；
- 本仓库只负责**索引与导航**，新增插件＝在这里加一行；
- 为什么不做 monorepo / 不归档：插件通过 **GitHub Releases 分发**、并有 **GitHub Pages 落地页**，
  而仓库一旦归档就**完全只读 —— Releases / Pages / Issue 全都动不了**。所以改为「各插件独立 + 本仓做索引」。
- 文档规范遵循 [knowledge-base 单项目规范](https://github.com/Simiely/knowledge-base)。

## 相关仓库

- 其它领域的索引：[`pc-tools`](https://github.com/Simiely/pc-tools)（Windows / PC 工具）·
  [`ae-tools`](https://github.com/Simiely/ae-tools)（After Effects）·
  [`blender-addons`](https://github.com/Simiely/blender-addons)（Blender 插件）
- 外围工具 [`oc-plugin-activator`](https://github.com/Simiely/oc-plugin-activator)
  （OctaneRender 缓存清理 / 资源部署）是 **Windows 工具、不是 C4D 插件**，
  **不属本仓库**，归 [`pc-tools`](https://github.com/Simiely/pc-tools) 索引。
