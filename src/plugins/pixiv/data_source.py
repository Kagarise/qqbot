import random

import httpx

from .config import Config


# https://api.fczbl.vip/pixiv/v2.html
async def get_illust_detail(id: int, mode="medium"):
    api = Config.search_api
    params = {
        'type': 'illust',
        'id': id
    }
    try:
        data = httpx.get(api, params=params).json()
        url = data['illust']['image_urls'][mode]
        return f'{Config.pic_api}{url}'
    except:
        return None


async def p_search(key, mode="medium"):
    api = Config.search_api
    params = {
        'type': 'search',
        'word': key,
        'bookmark_num_min': 1000
    }
    try:
        data = httpx.get(api, params=params).json()['illusts']
        # data.sort(key=lambda item: item['total_bookmarks'] / item['total_view'])
        # data.reverse()
        data = random.choice(data)
        id = data['id']
        url = data['image_urls'][mode]
        return id, f'{Config.pic_api}{url}'
    except:
        return None, None
