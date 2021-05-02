from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from nonebot.adapters.cqhttp import Message

from .data_source import get_help_data

help = on_command("help", aliases={"帮助"}, rule=to_me(), priority=1)


@help.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    logger.success(f'help: {event}\n')
    data = await get_help_data()
    await help.send(
        Message(f'[CQ:share,url={data["url"]},title={data["title"]},content={data["content"]},image={data["image"]}]'))
