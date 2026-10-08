# SPDX-License-Identifier: GPL-3.0-or-later
# C4D 插件骨架（示例结构，非完整实现）
# 派生时：替换 TOOL_ID / TOOL_TITLE，补全 Execute，配置 res/ 图标
import c4d

TOOL_ID = "PluginTemplate"     # TODO: 英文标识（用于插件 id 与文件名）
TOOL_TITLE = "示例插件"          # TODO: 中文名
PLUGIN_ID = 1000000             # TODO: 到 https://plugincafe.maxon.net/ 申请唯一 id

class PluginTemplate(c4d.plugins.CommandData):
    def Execute(self, doc):
        # TODO: 在这里写功能
        c4d.gui.MessageDialog(TOOL_TITLE + " 运行成功")
        return True

    def GetState(self, doc):
        return c4d.CMD_ENABLED

if __name__ == "__main__":
    c4d.plugins.RegisterCommandPlugin(
        id=PLUGIN_ID, str=TOOL_TITLE, info=0, icon=None, help="", dat=PluginTemplate())
