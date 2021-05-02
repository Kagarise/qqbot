from .config import Config


async def get_help_data():
    data = {
        'url': 'http://kagarise.cn/2021/05/01/bot/',
        'title': 'RayBot支持功能',
        'content': '欢迎使用RayBot，Made with ❤ by Kagarise',
        'image': Config.img
    }
    return data
