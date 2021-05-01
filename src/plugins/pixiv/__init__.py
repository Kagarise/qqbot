from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import p_search, get_illust_detail

pid = on_command("pid", rule=to_me(), priority=1)
psearch = on_command("psearch", aliases={"ps"}, rule=to_me(), priority=1)


@pid.handle()
async def handle_pid(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'pid: {event}\n')
    if args:
        state["id"] = args


@pid.got("id", prompt="请输入id")
async def handle_pid_got(bot: Bot, event: Event, state: T_State):
    id = state["id"]
    try:
        img_url = await get_illust_detail(int(id))
    except:
        await pid.send("格式：pid <id>")
        return
    if img_url is None:
        await pid.send("诶嘿，搜索出错了")
    else:
        await pid.send(Message(f'[CQ:image,file={img_url}]'))


@psearch.handle()
async def handle_ps(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'psearch: {event}\n')
    if args:
        state["key"] = args


@psearch.got("key", prompt="请输入查询关键词")
async def handle_ps_got(bot: Bot, event: Event, state: T_State):
    key = state["key"]
    try:
        img_id, img_url = await p_search(key)
    except:
        await psearch.send("诶嘿，搜索出错了")
        return
    if img_id is None or img_url is None:
        await psearch.send("诶嘿，搜索出错了")
    else:
        await psearch.send(Message(f'id:{img_id}[CQ:image,file={img_url}]'))
