from .config import Config


async def get_othello_data():
    data = {
        'url': 'http://othello.zzuli.love/#/index',
        'title': 'othello黑白棋',
        'content': '欢迎使用Memories of Conflict，Made with ❤ by Kagarise',
        'image': Config.img
    }
    return data
