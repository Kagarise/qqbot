from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_weather_detail

weather = on_command("天气", rule=to_me(), priority=1)


@weather.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'weather: {event}\n')
    if args:
        state["city"] = args


@weather.got("city", prompt="请输入城市")
async def handle_weather_got(bot: Bot, event: Event, state: T_State):
    if state['city'] == "":
        data = await get_weather_detail()
    else:
        data = await get_weather_detail(state['city'])
    msg = ""
    for key, value in data.items():
        if value:
            msg += f'{key}:{value}\n'
    await weather.send(msg.strip())
