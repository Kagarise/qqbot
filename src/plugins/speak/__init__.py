from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_aip

speak = on_command("speak", aliases={'语音'}, rule=to_me(), priority=1)


@speak.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'speak: {event}\n')
    if args:
        state["tex"] = args


@speak.got("tex", prompt="请发送一段文字")
async def handle_aip_got(bot: Bot, event: Event, state: T_State):
    try:
        tex = state['tex']
        url = await get_aip(tex)
        if url is None:
            await speak.send("出错了，请重新开始")
        else:
            await speak.send(Message(f'[CQ:record,file={url}]'))
    except:
        await speak.send("诶嘿，出错了")
