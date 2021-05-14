from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_hand_painting

hand_painting = on_command("手绘", rule=to_me(), priority=1)


@hand_painting.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    logger.success(f'hand_painting: {event}\n')


@hand_painting.got("img", prompt="请发送一张图片")
async def handle_hand_painting_got(bot: Bot, event: Event, state: T_State):
    img = Message(state["img"])
    try:
        if img[0].type == "image":
            await hand_painting.send("转化中")
            img_url = await get_hand_painting(img[0].data["url"])
            if img_url is None:
                await hand_painting.send("出错了，请重新开始")
            else:
                await hand_painting.send(Message(f'[CQ:image,file={img_url}]'))
        else:
            await hand_painting.send("这是啥？")
    except:
        await hand_painting.send("诶嘿，出错了")
