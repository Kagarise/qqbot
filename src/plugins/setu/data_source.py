from .config import Config

import random


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


if __name__ == "__main__":
    # get_file_name()
    # print(linecache.getline(Config.FILE_NAME, Config.FILE_CNT))
    pass
