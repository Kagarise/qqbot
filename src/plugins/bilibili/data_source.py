from nonebot.log import logger
import bilibili_api
from bilibili_api import user, live

from .config import get_proxy


async def set_proxy():
    bilibili_api.request_settings = {
        "proxies": None
    }
    try:
        proxy = get_proxy()['proxy']
        proxies = {
            'http': 'http://' + proxy
        }
        bilibili_api.request_settings = {
            "proxies": proxies
        }
    except:
        logger.warning('无可用代理')


async def get_user_info(user_id):
    # await set_proxy()
    data = user.get_user_info(uid=user_id)
    return data


async def live_data(room_id):
    # await set_proxy()
    data = live.get_room_play_info(room_display_id=room_id)
    return data


async def get_room_info(room_id):
    # await set_proxy()
    data = live.get_room_info(room_real_id=room_id)
    return data


async def get_dd_list_status(dd_list):
    datas = []
    for room_id in dd_list:
        data = await live_data(room_id)
        info = await get_room_info(room_id)
        user = await get_user_info(info['room_info']['uid'])
        datas.append({
            'name': user['name'],
            'room_id': room_id,
            'live_status': data['live_status'],
            'live_time': data['live_time'],
            'title': info['room_info']['title'],
            'img': info['room_info']['cover']
        })
    return datas
