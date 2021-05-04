import nonebot
from nonebot.log import default_format, logger
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)

nonebot.load_builtin_plugins()
nonebot.load_plugin('nonebot_plugin_apscheduler')
# nonebot.load_plugin('nonebot_plugin_songpicker2')
nonebot.load_plugin('nonebot_plugin_picsearcher')
nonebot.load_plugin('nonebot_plugin_biliav')
nonebot.load_from_toml("pyproject.toml")

logger.add("./logs/{time}.log",
           rotation="00:00",
           retention='1 week',
           enqueue=True,
           diagnose=False,
           level="SUCCESS",
           format=default_format,
           encoding='utf-8'
           )

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")
