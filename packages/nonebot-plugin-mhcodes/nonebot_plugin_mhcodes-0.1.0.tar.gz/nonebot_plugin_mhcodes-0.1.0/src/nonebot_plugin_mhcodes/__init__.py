from nonebot import logger, require, on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

from .utils import (
    code_added,
    code_removed,
    get_group_codes,
    reset_all_codes_for_group,
    reset_all_codes_daily
)


usage = """
添加集会码 [集会码]
查看集会码
删除集会码 [集会码]
重置集会码
每天4点自动重置集会码
"""

__plugin_meta__ = PluginMetadata(
    name="怪物猎人集会码插件",
    description="记录怪物猎人集会码",
    usage=usage,
    type="application",
    homepage="https://github.com/padoru233/nonebot-plugin-mhcodes",
    supported_adapters={"~onebot.v11"},
    extra={"author": "padoru233"},
)

add_code = on_command(
    "添加集会码",
    priority=5,
    block=True,
)

@add_code.handle()
async def handle_add_code(event: GroupMessageEvent, args: Message = CommandArg()):
    group_id = str(event.group_id)
    code = args.extract_plain_text().strip()

    if not code:
        await add_code.finish("集会码不能为空，请输入有效的集会码。")
        return

    if code_added(group_id, code):
        await add_code.finish(f"集会码 {code} 已添加到当前群组。")
    else:
        await add_code.finish(f"集会码 {code} 已存在于当前群组。")

remove_code = on_command(
    "删除集会码",
    priority=5,
    block=True,
)

@remove_code.handle()
async def handle_remove_code(event: GroupMessageEvent, args: Message = CommandArg()):
    group_id = str(event.group_id)
    code = args.extract_plain_text().strip()

    if not code:
        await remove_code.finish("集会码不能为空，请输入有效的集会码。")
        return

    if code_removed(group_id, code):
        await remove_code.finish(f"集会码 {code} 已从当前群组删除。")
    else:
        await remove_code.finish(f"集会码 {code} 不存在于当前群组。")

get_codes = on_command(
    "查看集会码",
    priority=5,
    block=True,
)

@get_codes.handle()
async def handle_get_codes(event: GroupMessageEvent):
    group_id = str(event.group_id)
    codes = get_group_codes(group_id)

    if codes:
        message = "当前集会码：\n" + "\n".join(f"{i}. {code}" for i, code in enumerate(codes, 1))
    else:
        message = "当前没有集会码。"

    await get_codes.finish(message)

reset_code = on_command(
    "重置集会码",
    priority=5,
    block=True,
)

@reset_code.handle()
async def handle_reset_code(event: GroupMessageEvent):
    group_id = str(event.group_id)

    if reset_all_codes_for_group(group_id):
        await reset_code.finish("当前群组的集会码已全部重置。")
    else:
        await reset_code.finish("当前群组没有集会码需要重置。")

@scheduler.scheduled_job("cron", hour=4, minute=0, id="reset_mh_codes_daily")
async def daily_reset_job():
    logger.info("开始执行每日集会码重置任务...")
    reset_all_codes_daily()
    logger.info("每日集会码重置任务完成。")
