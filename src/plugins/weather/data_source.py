import httpx

from .config import Config


async def get_weather_detail(city="郑州", daily=True, now=True):
    params = {
        'key': Config.api_key,
        'location': city
    }
    data = dict()
    data['城市'] = city
    if daily:
        await get_daily(data, params)
    if now:
        await get_now(data, params)
    return data


async def get_daily(data, params):
    try:
        daily_data = eval(httpx.get(Config.daily, params=params).text)['results'][0]['daily'][0]
        data['天气'] = f'{daily_data["text_day"]}/{daily_data["text_night"]}'
        data['气温'] = f'{daily_data["low"]}℃~{daily_data["high"]}℃'
    except:
        data['天气'] = None
        data['气温'] = None


async def get_now(data, params):
    try:
        now_data = eval(httpx.get(Config.now, params=params).text)['results'][0]['now']
        data['实时'] = f'{now_data["text"]}/{now_data["temperature"]}℃'
    except:
        data['实时'] = None

# def get_suggestion(data, params):
#     try:
#         suggestion_data = eval(httpx.get(Config.now, params=params).text)['results'][0]['suggestion']
#     except:
#         pass
