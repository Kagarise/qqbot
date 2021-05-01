import random

from .data_source import get_tuling_ai_response

from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

tuling_ai = on_command("", rule=to_me(), priority=5)


@tuling_ai.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    state['message'] = str(event.get_message()).strip()
    logger.success(f'tuling_ai: {event}\n')
    if state['message'] == "":
        await tuling_ai.send(random.choice(["怎么了？", "咋住了？", "又想看涩图了？", "我是你爹"]))
    else:
        response = await get_tuling_ai_response(state['message'])
        await tuling_ai.send(response)
