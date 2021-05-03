from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message

from .data_source import get_illust_info, p_search, p_rank, p_user

pid = on_command("pid", rule=to_me(), priority=1)
psearch = on_command("psearch", aliases={"ps"}, rule=to_me(), priority=1)
prank = on_command("prank", aliases={"pr"}, rule=to_me(), priority=1)
puser = on_command("puser", aliases={"pu"}, rule=to_me(), priority=1)


@pid.handle()
async def handle_pid(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'pid: {event}\n')
    if args:
        state["id"] = args


@pid.got("id", prompt="请输入id")
async def handle_pid_got(bot: Bot, event: Event, state: T_State):
    try:
        id = state["id"]
        data = await get_illust_info(int(id), url_only=False)
    except:
        await pid.send("格式：pid <id>")
        return
    try:
        await pid.send(f'''id:{data['id']}
title:{data['title']}
user_id:{data['user_id']}
user_name:{data['user_name']}''' + Message(f'[CQ:image,file={data["url"]}]'))
    except:
        await pid.send("诶嘿，搜索出错了")


@psearch.handle()
async def handle_ps(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'psearch: {event}\n')
    if args:
        state["key"] = args


@psearch.got("key", prompt="请输入查询关键词")
async def handle_ps_got(bot: Bot, event: Event, state: T_State):
    try:
        key = state["key"]
        data = await p_search(key)
        await psearch.send(f'''id:{data['id']}
title:{data['title']}
user_id:{data['user_id']}
user_name:{data['user_name']}''' + Message(f'[CQ:image,file={data["url"]}]'))
    except:
        await psearch.send("诶嘿，搜索出错了")


@prank.handle()
async def handle_pr(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'prank: {event}\n')
    if args:
        state["rank"] = args


@prank.got("rank", prompt="请输入排名（1-20）")
async def handle_pr_got(bot: Bot, event: Event, state: T_State):
    try:
        rank = int(state["rank"]) - 1
        if 0 <= rank < 20:
            data = await p_rank(rank)
            await prank.send(f'''id:{data['id']}
title:{data['title']}
user_id:{data['user_id']}
user_name:{data['user_name']}''' + Message(f'[CQ:image,file={data["url"]}]'))
        else:
            await prank.send("plz:\nrank∈[1,20] ∩ rank∈N*")
    except:
        await prank.send("诶嘿，搜索出错了")


@puser.handle()
async def handle_pu(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.success(f'puser: {event}\n')
    if args:
        state["user_id"] = args


@puser.got("user_id", prompt="请输入用户id")
async def handle_pu_got(bot: Bot, event: Event, state: T_State):
    try:
        user_id = int(state["user_id"])
        datas = await p_user(user_id)
        if datas == []:
            await puser.send("uid不存在或该uid无illust")
            return
        await puser.send(f'将展示{len(datas)}幅作品')
        for data in datas:
            await puser.send(f'''id:{data['id']}
title:{data['title']}''' + Message(f'[CQ:image,file={data["url"]}]'))
    except:
        await puser.send("诶嘿，搜索出错了")
