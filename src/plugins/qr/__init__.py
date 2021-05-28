from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_qr

qr = on_command("qr", aliases={'二维码'}, rule=to_me(), priority=1)


@qr.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'qr: {event}\n')
    if args:
        state["qr_data"] = args


@qr.got("qr_data", prompt="请发送一段文字")
async def handle_qr_got(bot: Bot, event: Event, state: T_State):
    try:
        tex = state['qr_data']
        url = await get_qr(tex=tex)
        if url is None:
            await qr.send("出错了，请重新开始")
        else:
            await qr.send(Message(f'[CQ:image,file={url}]'))
    except:
        await qr.send("诶嘿，出错了")
