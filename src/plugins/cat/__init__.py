from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_cat_url, get_dog_url

cat = on_command("cat", aliases={'来张猫图', '来张猫猫图', '猫图', '猫猫图', '来份猫图', '来份猫猫图', '来一张猫猫图', '来一张猫图', '来一份猫猫图', '来一份猫图'},
                 rule=to_me(), priority=1)
dog = on_command("dog", aliases={'来张狗图', '来张狗狗图', '狗图', '狗狗图', '来份狗图', '来份狗狗图', '来一张狗狗图', '来一张狗图', '来一份狗狗图', '来一份狗图'},
                 rule=to_me(), priority=1)


@cat.handle()
async def cat_handle(bot: Bot, event: Event):
    logger.success(f'cat: {event}\n')
    img_url = await get_cat_url()
    await cat.send(Message(f'[CQ:image,file={img_url}]'))


@dog.handle()
async def dog_handle(bot: Bot, event: Event):
    logger.success(f'dog: {event}\n')
    img_url = await get_dog_url()
    await dog.send(Message(f'[CQ:image,file={img_url}]'))
