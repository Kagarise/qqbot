from .data_source import get_cat_url

from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

cat = on_command("cat", aliases={'来张猫图', '来张猫猫图', '猫图', '猫猫图'}, rule=to_me(), priority=1)


@cat.handle()
async def handle(bot: Bot, event: Event):
    logger.success(f'cat: {event}\n')
    img_url = await get_cat_url()
    await cat.send(Message(f'[CQ:image,file={img_url}]'))
