# CHANGELOG.md · 仓库级变更

## 仓库 · 2026-11-19 · 升级 repo-kit 2.9.0

- kit 2.7.2 → **2.9.0**；`schema/kit.lock.json` 重写（`spec_version` 2.1.3 → **2.1.4**）
- 新增能力：`AGENTS_TOO_LONG`（`AGENTS.md` > 150 行报 ERROR）。本仓 `AGENTS.md` 现 30 行，升级当天零拦截
- 2.8.1 起 `check_spec` 只比主/次版本，补丁差异（2.1.3↔2.1.4）不再报错
- `schema/taxonomy.json` 的 `version` 同步为 2.9.0（避免 `skew: taxonomy-vs-lock`）；
  仓库自有配置（`include` / `frontmatter_exempt` / `generated_files`）**未改**
- 验收：`REPO CHECK: PASS`、`KIT LOCK: PASS (v2.9.0, spec=2.1.4)`

## 仓库 · 2026-11-17 · 接入单项目规范机器层

- 接入 knowledge-base 的**单项目规范**（spec 2.1.3 / repo-kit 2.7.2，profile `link-only`）
- 新增 `schema/taxonomy.json`、`tools/repo-kit/`、`tools/update-repo-kit.ps1`、`schema/kit.lock.json` 与 CI
- 只查链接与入口（link-only）：`plugins/**/*.md` 是各插件的门面，不套页面契约；将来需要跨插件索引再升 `monorepo`
- 验收：`REPO CHECK: PASS`（ERROR=0）、`KIT LOCK: PASS (v2.7.2, spec=2.1.3)`

- `plugins/**/*.md` 走 `frontmatter_exempt.paths`，只查链接，不给插件文档套页面契约

## 仓库 · 2026-10-09 · **撤销索引化，恢复为总管仓库**

- **恢复插件代码**：`plugins/c4d-mesh-face-sorter/`、`plugins/c4d-userdata-manager/` 共 **18 个文件**，
  从本仓库历史提交 `66109db` 的树中**逐字节原样取回**（零改动，blob SHA 逐一比对）
- 四件套改回**总管性质**（README 变为「插件一览 + 源码位置 + 安装 + 发版约定」）
- **两个原独立仓库随即归档只读**，作为**历史快照**保留
- **策略变更**：插件小而发版少，不值得「一插件一仓」→ 改为「**总管仓库装全部插件、直接迭代；
  成员仓归档封存**」；只有 PC 软件（重、发版频繁）才沿用「一工具一仓 + 索引」
- `tools/oc-plugin-activator/` **不恢复** —— 它是 **Windows 工具**（非 C4D 插件），
  归 [`pc-tools`](https://github.com/Simiely/pc-tools) 索引
- **发版约定**：统一在本仓库发，tag 形如 `<插件名>-vX.Y.Z`

---

## 仓库 · 2026-10-08 · **由 monorepo 转为索引仓库**（已撤销）

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
