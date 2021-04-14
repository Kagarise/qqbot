import httpx

from .config import Config


# https://www.kancloud.cn/turing/www-tuling123-com/718227
async def get_tuling_ai_response(message):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    params = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": message
            }
        },
        "userInfo": {
            "apiKey": Config.api_key,
            "userId": Config.user_id
        }
    }
    data = eval(httpx.post(api, json=params).text)
    codes = [5000, 6000, 4000, 4001, 4002, 4003, 4005, 4007, 4100, 4200, 4300, 4400, 4500, 4600, 4602, 7002, 8008]
    if data['intent']['code'] not in codes:
        data = data['results']
        s = ''
        for val in data:
            s += f'{val["values"][val["resultType"]]}\n'
        return s.strip('\n')
    else:
        return "ERROR：请求错误"

# {'emotion':
#      {'robotEmotion':
#           {'a': 0, 'd': 0, 'emotionId': 0, 'p': 0},
#       'userEmotion':
#           {'a': 0, 'd': 0, 'emotionId': 0, 'p': 0}},
#  'intent':
#      {'actionName': '', 'code': 10004, 'intentName': ''},
#  'results':
#      [{'groupType': 1, 'resultType': 'text', 'values': {'text': '今天晚上有安排吗？'}}]}
