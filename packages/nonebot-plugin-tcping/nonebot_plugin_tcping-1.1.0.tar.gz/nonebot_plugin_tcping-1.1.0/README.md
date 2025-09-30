## 介绍

这是一个 nonebot2 插件, 用于TCP端口连通性测试工具，支持域名和IP地址测试


## 安装方法

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-tcping

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-tcping
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-tcping
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-tcping
</details>


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_tcping"]

</details>

# ...
<!-- 此处填写插件的其他介绍 -->
## 使用方法

在.env.prod中添加
"""
#tcping
tcping_url = https://v2.api-m.com/api/tcping

#撤回消息的默认时间
recal_time=10
"""
### 指令格式

1. 发送指令 `tcping <域名或IP地址> <端口号>` 即可测试该端口是否连通
2. 插件会返回测试结果, 如端口连通则返回 `端口 <端口号> 连通`, 否则返回 `端口 <端口号> 不连通`
