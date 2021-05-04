import datetime
import random

import nonebot
from nonebot import require
from nonebot.log import logger
from nonebot.adapters.cqhttp import Message

from .config import Config
from ..pixiv.data_source import p_rank
from ..cat.data_source import get_cat_url, get_dog_url

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", hour="11", minute="11", id="pr1")
async def pr1_on_11_11():
    try:
        bot = nonebot.get_bots()[Config.me]
        logger.success(f"{bot}:pr1")
        data = await p_rank(0)
        msg = f'''id:{data['id']}
title:{data['title']}
user_id:{data['user_id']}
user_name:{data['user_name']}''' + Message(f'[CQ:image,file={data["url"]}]')
        # await bot.call_api('send_private_msg', **{
        #     'message': msg,
        #     'user_id': Config.superuser
        # })
        await bot.call_api('send_group_msg', **{
            'message': msg,
            'group_id': Config.test_group
        })
    except:
        logger.error("定时任务pr1失败")


@scheduler.scheduled_job("cron", hour="21", minute="30", id="wzdd")
async def wzdd_on_21_30():
    try:
        bot = nonebot.get_bots()[Config.me]
        logger.success(f"{bot}:wzdd")
        msg = '''王者dd''' + Message('[CQ:face,id=6]')
        await bot.call_api('send_group_msg', **{
            'message': msg,
            'user_id': Config.main_group
        })
    except:
        logger.error("定时任务wzdd失败")


@scheduler.scheduled_job("cron", hour="12,22", id="animal")
async def animal_on_12_00_and_22_00():
    try:
        bot = nonebot.get_bots()[Config.me]
        logger.success(f"{bot}:animal")
        choice = ['猫猫', '狗狗']
        choice = random.choice(choice)
        if choice == '猫猫':
            img_url = await get_cat_url()
        elif choice == '狗狗':
            img_url = await get_dog_url()
        else:
            img_url = None
        msg = f'已经{datetime.datetime.now().hour}点了，来看{choice}图叭' + Message(f'[CQ:image,file={img_url}]')
        await bot.call_api('send_group_msg', **{
            'message': msg,
            'user_id': Config.main_group
        })
    except:
        logger.error("定时任务animal失败")
