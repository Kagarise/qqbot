from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_othello_data

othello = on_command("othello", aliases={"黑白棋", "来局黑白棋", "来一局黑白棋"}, rule=to_me(), priority=1)


@othello.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    logger.success(f'othello: {event}\n')
    data = await get_othello_data()
    await othello.send(
        Message(f'[CQ:share,url={data["url"]},title={data["title"]},content={data["content"]},image={data["image"]}]'))
