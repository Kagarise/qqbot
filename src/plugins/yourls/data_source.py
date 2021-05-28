import httpx

from .config import Config


async def get_yourls(url):
    params = {
        'url': url
    }
    try:
        data = eval(httpx.post(Config.api, json=params).text)
        print(data)
        if data['code'] == 200 and data['data']['url']['statusCode'] == 200:
            return data['data']['url']['shorturl'].replace('\\', '')
        else:
            return None
    except:
        return None
