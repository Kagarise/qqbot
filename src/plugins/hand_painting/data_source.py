import httpx

from .config import Config


async def get_hand_painting(url):
    params = {
        'url': url
    }
    try:
        data = eval(httpx.post(Config.api, json=params, timeout=20).text)
        if data['code'] == 200:
            return data['data']['url']
        else:
            return None
    except:
        return None
