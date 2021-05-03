import random

from .config import Config


async def get_setu_url():
    url = f'{Config.API}{random.choice(Config.SOURCE)}'
    return url


def get_file_name():
    import os
    path = Config.LOCAL_PATH
    filelist = os.listdir(path)
    with open(Config.FILE_NAME, 'a') as f:
        f.write('[\n')
        for item in filelist:
            f.write(f'"{item}",\n')
        f.write(']')
