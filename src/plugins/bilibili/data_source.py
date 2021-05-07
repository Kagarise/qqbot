import time

from bilibili_api import user, live

from .config import Config


def get_user_info(user_id):
    time.sleep(1)
    data = user.get_user_info(uid=user_id)
    return data


def live_data(room_id):
    time.sleep(1)
    data = live.get_room_play_info(room_display_id=room_id)
    return data


def get_room_info(room_id):
    time.sleep(1)
    data = live.get_room_info(room_real_id=room_id)
    return data


def get_dd_list_status():
    datas = []
    for room_id in Config.dd_list:
        data = live_data(room_id)
        info = get_room_info(room_id)
        user = get_user_info(info['room_info']['uid'])
        datas.append({
            'name': user['name'],
            'room_id': room_id,
            'live_status': data['live_status'],
            'live_time': data['live_time'],
            'title': info['room_info']['title'],
            'img': info['room_info']['cover']
        })
    return datas
