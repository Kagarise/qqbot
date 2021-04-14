import httpx

from .config import Config


# http://oddfar.com/archives/49/
async def get_quotation(type=None):
    if type is None:
        return Config.total
    else:
        api = 'https://api.oddfar.com/yl/q.php'
        params = {
            'c': type,
        }
        response = httpx.get(api, params=params).text.replace('<br>', '\n').strip()
        if response == '':
            return "ERROR：语录请求错误"
        else:
            return response

# { "code": "200", "msg": "success", "type": "2004", "text": "我点燃了火，却控制不了它。" }
