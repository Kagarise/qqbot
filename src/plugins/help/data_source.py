from .config import Config


async def get_help_data():
    data = {
        'url': 'http://kagarise.cn/2021/05/01/bot/',
        'title': 'Rainbow支持功能',
        'content': '欢迎使用Rainbow，Made with ❤ by Kagarise',
        'image': Config.img
    }
    return data
