import httpx
from nonebot.log import logger


async def get_hand_painting(url):
    api = 'http://api.flora.love/v1/hand_painting'
    params = {
        'url': url
    }
    try:
        data = eval(httpx.post(api, json=params, timeout=20).text)
        if data['code'] == 200:
            return data['data']['url']
        else:
            return None
    except:
        return None
