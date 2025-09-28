<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ nonebot-plugin-mhcodes ✨
[![LICENSE](https://img.shields.io/github/license/padoru233/nonebot-plugin-mhcodes.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-mhcodes.svg)](https://pypi.python.org/pypi/nonebot-plugin-mhcodes)
[![python](https://img.shields.io/badge/python-3.10|3.11|3.12|3.13-blue.svg)](https://www.python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv)](https://github.com/astral-sh/uv)
<br/>
[![ruff](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://results.pre-commit.ci/badge/github/padoru233/nonebot-plugin-mhcodes/master.svg)](https://results.pre-commit.ci/latest/github/padoru233/nonebot-plugin-mhcodes/master)

</div>

## 📖 介绍

怪物猎人集会码插件

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-mhcodes --upgrade
使用 **pypi** 源安装

    nb plugin install nonebot-plugin-mhcodes --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install nonebot-plugin-mhcodes --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"


</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

    uv add nonebot-plugin-mhcodes
安装仓库 master 分支

    uv add git+https://github.com/padoru233/nonebot-plugin-mhcodes@master
</details>

<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-mhcodes
安装仓库 master 分支

    pdm add git+https://github.com/padoru233/nonebot-plugin-mhcodes@master
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-mhcodes
安装仓库 master 分支

    poetry add git+https://github.com/padoru233/nonebot-plugin-mhcodes@master
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_mhcodes"]

</details>

<details>
<summary>使用 nbr 安装(使用 uv 管理依赖可用)</summary>

[nbr](https://github.com/fllesser/nbr) 是一个基于 uv 的 nb-cli，可以方便地管理 nonebot2

    nbr plugin install nonebot-plugin-mhcodes
使用 **pypi** 源安装

    nbr plugin install nonebot-plugin-mhcodes -i "https://pypi.org/simple"
使用**清华源**安装

    nbr plugin install nonebot-plugin-mhcodes -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>


## ⚙️ 配置

无配置

## 🎉 使用
### 指令表
| 指令  | 权限  | 需要@ | 范围  |   说明   |
| :---: | :---: | :---: | :---: | :------: |
| 查看集会码 | 群员  |  否   | 群聊  | 查看当前群组集会码 |
| 添加集会码 [集会码] | 群员  |  否   | 群聊  | 添加集会码 + 集会码 |
| 删除集会码 [集会码] | 群员  |  否   | 群聊  | 删除集会码 + 集会码 |
| 重置集会码 | 群员  |  否   | 群聊  | 重置当前群组集会码 |

每天4点自动重置集会码

### 🎨 效果图
如果有效果图的话
