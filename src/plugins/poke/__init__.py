import random

from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config(**global_config.dict())

from nonebot import on_notice
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

poke = on_notice(rule=to_me(), priority=1)


@poke.handle()
async def handle(bot: Bot, event: Event):
    data = event.dict()
    logger.success(f'poke: {data}\n')
    if data['sub_type'] == 'poke':
        await poke.send(random.choice(["你再戳！", "欸很烦欸！你戳你🐴呢", "别戳了别戳了再戳就坏了555", "我爪巴我爪巴,球球别再戳了", "差不多得了😅"]))
