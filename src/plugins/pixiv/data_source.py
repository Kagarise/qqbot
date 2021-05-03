import random
import httpx

from .config import Config


# https://api.fczbl.vip/pixiv/v2.html
async def get_illust_info(id: int, mode="original", url_only=True):
    api = Config.search_api
    params = {
        'type': 'illust',
        'id': id
    }
    try:
        data = httpx.get(api, params=params).json()['illust']
        if data['meta_pages'] == []:
            url = data['meta_single_page']['original_image_url']
        else:
            url = data['meta_pages'][0]['image_urls'][mode]
        if url_only:
            return f'{Config.pic_api}{url}'
        else:
            return {
                'id': data['id'],
                'title': data['title'],
                'user_id': data['user']['id'],
                'user_name': data['user']['name'],
                'url': f'{Config.pic_api}{url}'
            }
    except:
        return None


async def p_search(key):
    api = Config.search_api
    params = {
        'type': 'search',
        'word': key,
        'bookmark_num_min': 1000
    }
    try:
        data = httpx.get(api, params=params).json()['illusts']
        id = random.choice(data)['id']
        data = await get_illust_info(id, url_only=False)
        return data
    except:
        return None


async def p_rank(rank, mode="day"):
    api = Config.search_api
    params = {
        'type': 'rank',
        'mode': mode
    }
    try:
        data = httpx.get(api, params=params).json()['illusts']
        id = data[rank]['id']
        data = await get_illust_info(id, url_only=False)
        return data
    except:
        return None


async def p_user(user_id, limit=3):
    api = Config.search_api
    params = {
        'type': 'member_illust',
        'id': user_id
    }
    try:
        data = httpx.get(api, params=params).json()['illusts']
        datas = []
        for idx in range(min(limit, len(data))):
            datas.append(await get_illust_info(data[idx]['id'], url_only=False))
        return datas
    except:
        return None
