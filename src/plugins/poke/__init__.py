from nonebot import on_notice
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

from src.plugins.poke.data_source import get_poke_response

poke = on_notice(rule=to_me(), priority=1)


@poke.handle()
async def handle(bot: Bot, event: Event):
    data = event.dict()
    logger.success(f'poke: {data}\n')
    if data['sub_type'] == 'poke':
        response = await get_poke_response()
        await poke.send(response)
