from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

test = on_command("test", rule=to_me(), priority=1)


@test.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    state['message'] = str(event.get_message()).strip()
    logger.success(f'test: {event}\n')
    await test.send(f"test...{state['message']}\n test...{state['message']}\n  test...{state['message']}")
