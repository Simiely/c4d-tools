# C4D 插件骨架 C4D-PLUGIN-SKELETON

派生新 C4D 插件的起点。**不是可交付插件**，是一份带约定的骨架。

## ⚠️ 为什么它不在 `plugins/` 下

`plugins/` 下的每个一级子目录都会被当成一个可安装插件；模板放进去会被误当插件。
所以放仓库根 `_template/`。

## 派生一个新插件（三步）

1. 复制 `_template/` 到 `plugins/<插件名>/`，令插件文件与目录同名
2. 替换两个标识：`TOOL_ID`（英文标识）、`TOOL_TITLE`（中文名），补全功能与图标（`res/`）
3. 在 C4D 里编译为 `.pyp`（Script Manager → Save as .pyp），放进 C4D 的 `plugins/` 验证
