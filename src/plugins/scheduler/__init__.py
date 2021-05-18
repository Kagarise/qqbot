import datetime
import random

import nonebot
from nonebot import require
from nonebot.log import logger
from nonebot.adapters.cqhttp import Message

from .config import Config
from ..pixiv.data_source import p_rank
from ..cat.data_source import get_cat_url, get_dog_url
from ..weather.data_source import get_weather_detail
from ..bilibili.data_source import get_dd_list_status

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", hour="11", minute="50", second="0", id="pr")
async def pr_on_11_50():
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        logger.success(f"{Config.me}:scheduler-pr")
        for rank in range(3):
            data = await p_rank(rank)
            msg = f'''rank:{rank + 1}
id:{data['id']}
title:{data['title']}
user_id:{data['user_id']}
user_name:{data['user_name']}''' + Message(f'[CQ:image,file={data["url"]}]')
            # await bot.call_api('send_private_msg', **{
            #     'message': msg,
            #     'user_id': Config.superuser
            # })
            await Bot_me.call_api('send_group_msg', **{
                'message': msg,
                'group_id': Config.test_group
            })
    except:
        logger.error("定时任务pr失败")


# @scheduler.scheduled_job("cron", hour="21", minute="30", id="wzdd")
# async def wzdd_on_21_30():
#     try:
#         bot = nonebot.get_bots()[Config.me]
#         logger.success(f"{bot}:wzdd")
#         msg = '王者dd' + Message('[CQ:face,id=6]')
#         await bot.call_api('send_group_msg', **{
#             'message': msg,
#             'user_id': Config.main_group
#         })
#     except:
#         logger.error("定时任务wzdd失败")


@scheduler.scheduled_job("cron", hour="7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23", minute="0", second="30",
                         id="animal")
async def animal_on_7_00_to_23_00():
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        logger.success(f"{Config.me}:scheduler-animal")
        choice = ['猫猫', '狗狗']
        choice = random.choice(choice)
        if choice == '猫猫':
            img_url = await get_cat_url()
        elif choice == '狗狗':
            img_url = await get_dog_url()
        else:
            img_url = None
        msg = f'已经{datetime.datetime.now().hour}点了，来看{choice}图叭' + Message(f'[CQ:image,file={img_url}]')
        await Bot_me.call_api('send_group_msg', **{
            'message': msg,
            'group_id': Config.test_group
        })
    except:
        logger.error("定时任务animal失败")


@scheduler.scheduled_job("cron", hour="7", minute="20", second="45", id="weather_daily")
async def weather_on_7_20():
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        logger.success(f"{Config.me}:scheduler-weather_daily")
        data = await get_weather_detail()
        msg = ""
        for key, value in data.items():
            if value:
                msg += f'{key}:{value}\n'
        msg = msg.strip()
        await Bot_me.call_api('send_group_msg', **{
            'message': msg,
            'group_id': Config.test_group
        })
    except:
        logger.error("定时任务weather_daily失败")


@scheduler.scheduled_job("cron", hour="11,18", minute="30", second="45", id="weather_now")
async def weather_on_11_30_and_18_30():
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        logger.success(f"{Config.me}:scheduler-weather_now")
        data = await get_weather_detail(daily=False)
        msg = ""
        for key, value in data.items():
            if value:
                msg += f'{key}:{value}\n'
        msg = msg.strip()
        await Bot_me.call_api('send_group_msg', **{
            'message': msg,
            'group_id': Config.test_group
        })
    except:
        logger.error("定时任务weather_now失败")


live_dd_status = dict()


@scheduler.scheduled_job("cron", second="55", id="live_dd")
async def live_dd_each_1_minute():
    dd_list = [34027, 23105590]
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        datas = await get_dd_list_status(dd_list=dd_list)
        for data in datas:
            if data['live_status']:
                if data['room_id'] not in live_dd_status or data['live_time'] != live_dd_status[data['room_id']]:
                    live_dd_status[data['room_id']] = data['live_time']
                    msg = f'''{data["name"]}开播啦！
房间号：{data["room_id"]}
标题：{data["title"]}''' + Message(f'[CQ:image,file={data["img"]}]')
                    await Bot_me.call_api('send_group_msg', **{
                        'message': msg,
                        'group_id': Config.test_group
                    })
                    logger.success(f'{Config.me}:scheduler-live_dd:{data["name"]}开播啦！')
    except:
        logger.error("定时任务live_dd失败")


main_group_dd_status = dict()


@scheduler.scheduled_job("cron", second="50", id="main_group_dd")
async def main_group_dd_each_1_minute():
    dd_list = [22314455]
    try:
        Bot_me = nonebot.get_bots()[Config.me]
        datas = await get_dd_list_status(dd_list=dd_list)
        for data in datas:
            if data['live_status']:
                if data['room_id'] not in main_group_dd_status or data['live_time'] != main_group_dd_status[
                    data['room_id']]:
                    main_group_dd_status[data['room_id']] = data['live_time']
                    msg = f'''{data["name"]}开播啦！
房间号：{data["room_id"]}
标题：{data["title"]}''' + Message(f'[CQ:image,file={data["img"]}]')
                    await Bot_me.call_api('send_group_msg', **{
                        'message': msg,
                        'group_id': Config.main_group
                    })
                    logger.success(f'{Config.me}:scheduler-main_group_dd:{data["name"]}开播啦！')
    except:
        logger.error("定时任务main_group_dd失败")
