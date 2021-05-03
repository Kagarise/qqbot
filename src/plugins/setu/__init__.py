from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_setu_url

setu = on_command("/setu", rule=to_me(), priority=1)


@setu.handle()
async def handle(bot: Bot, event: Event):
    logger.success(f'setu: {event}\n')
    img_url = await get_setu_url()
    await setu.send(Message(f'[CQ:image,file={img_url}]'))
