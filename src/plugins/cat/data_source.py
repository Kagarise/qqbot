import httpx
from .config import Config


# https://docs.thecatapi.com/authentication
async def get_cat_url():
    api = 'https://api.thecatapi.com/v1/images/search'
    data = eval(httpx.get(api, headers=Config.headers).text)
    try:
        url = data[0]['url']
        return url
    except:
        return f'ERROR：猫图请求错误'

# {
#     "breeds": [
#
#     ],
#     "id": "MTg5OTc0Mw",
#     "url": "https://cdn2.thecatapi.com/images/MTg5OTc0Mw.jpg",
#     "width": 480,
#     "height": 343
# }
