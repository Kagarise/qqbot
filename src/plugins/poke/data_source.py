import random
from .config import Config


async def get_poke_response():
    return random.choice(Config.response)
