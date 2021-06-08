from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_yourls

yourls = on_command("yourls", aliases={"短链接"}, rule=to_me(), priority=1)


@yourls.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'yourls: {event}\n')
    if args:
        state["yourls"] = args


@yourls.got("yourls", prompt="请输入链接")
async def handle_weather_got(bot: Bot, event: Event, state: T_State):
    url = await get_yourls(state['yourls'])
    if url:
        await yourls.send(url)
        # await yourls.send(Message(
        #     f'[CQ:share,url={data["url"]},title={data["title"]},content={data["content"]},image={data["image"]}]'))
    else:
        await yourls.send("转换短链接失败")
