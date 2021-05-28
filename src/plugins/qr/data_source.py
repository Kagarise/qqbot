import httpx

from .config import Config


async def get_qr(tex):
    params = {
        'tex': tex
    }
    try:
        data = eval(httpx.post(Config.api, json=params, timeout=5).text)
        if data['code'] == 200:
            return data['data']['url']
        else:
            return None
    except:
        return None
