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
            'encode': 'json'
        }
        data = eval(httpx.get(api, params=params).text)
        if data['code'] == '200':
            return data['text'].replace('<br>', '\n').strip()
        else:
            return f'ERROR：语录请求错误-{data["msg"]}'

# { "code": "200", "msg": "success", "type": "2004", "text": "我点燃了火，却控制不了它。" }
