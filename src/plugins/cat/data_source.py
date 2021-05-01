import httpx
from .config import Config


# https://docs.thecatapi.com/
async def get_cat_url():
    api = 'https://api.thecatapi.com/v1/images/search'
    try:
        data = eval(httpx.get(api, headers=Config.cat_headers).text)
        url = data[0]['url']
        return url
    except:
        return f'ERROR：猫图请求错误'


# https://docs.thedogapi.com/
async def get_dog_url():
    api = 'https://api.thedogapi.com/v1/images/search'
    try:
        data = eval(httpx.get(api, headers=Config.dog_headers).text)
        url = data[0]['url']
        return url
    except:
        return f'ERROR：狗图请求错误'

# {
#     "breeds": [
#
#     ],
#     "id": "MTg5OTc0Mw",
#     "url": "https://cdn2.thecatapi.com/images/MTg5OTc0Mw.jpg",
#     "width": 480,
#     "height": 343
# }
