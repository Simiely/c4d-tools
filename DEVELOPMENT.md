# DEVELOPMENT.md · 仓库说明

本文件是**门面 + 手册**：仓库级信息与入口，插件细节走各插件自己的文档。

## 定位

`c4d-tools` 是个人 C4D 插件的**总管仓库**：**插件的全部源码都在这里**，直接迭代开发。
每个插件在 `plugins/<插件名>/` 下自成一目录（`.pyp` + `res/` + 四件套）。

## 结构

```
c4d-tools/
├─ README.md · AGENTS.md · DEVELOPMENT.md · CHANGELOG.md   四件套
├─ plugins/
│  ├─ c4d-mesh-face-sorter/     .pyp + res/ + 四件套
│  └─ c4d-userdata-manager/     .pyp + res/ + 四件套
└─ _template/     新 C4D 插件骨架（本仓库唯一的非插件内容）
```

## 演进

- **2026-10-08 建库**：仿 `ae-tools` 建 monorepo `c4d-tools`，把 3 个独立仓库
  （2 个 C4D 插件 + 1 个 Windows 工具）搬入，原仓库归档。
- **2026-10-08（同日调整）转为索引仓库**：当时担心归档冻结 Releases / Pages。
- **2026-10-09 撤销索引化，恢复总管**：确认插件**体积小、发版少**，
  「一插件一仓 + 索引」属过度拆分 → 收回代码、直接迭代；原独立仓库**归档封存**。
  （PC 软件不同：重、发版频繁，仍走「一工具一仓 + `pc-tools` 索引」。）

## 每次改动的动作清单

| 场景 | 动作 |
|---|---|
| 改插件 | 直接改 `plugins/<名>/` 下的源码 → 更新该插件的 CHANGELOG |
| 发版 | 在本仓库打 tag `<插件名>-vX.Y.Z` + 发 Release（附件放插件 zip） |
| 新增插件 | `plugins/<名>/`（可从 `_template/` 起手）→ README 加行 → CHANGELOG 加节 |
| 任何提交后 | 更新 `AGENTS.md` 顶部的**文档基线行**（日期 + 新 commit hash） |
