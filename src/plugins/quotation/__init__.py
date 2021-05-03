from nonebot import on_command
from nonebot.log import logger
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

from .data_source import get_quotation
from .config import Config

quotation = on_command("quotation", aliases={'语录'}, rule=to_me())
twqh = on_command("土味情话", rule=to_me(), priority=1)
jsyl = on_command("精神语录", rule=to_me(), priority=1)
wyyrp = on_command("网易云热评", rule=to_me(), priority=1)
crxh = on_command("//成人笑话", rule=to_me(), priority=1)
qpdh = on_command("奇葩对话", rule=to_me(), priority=1)
tgrj = on_command("舔狗日记", rule=to_me(), priority=1)
djt = on_command("毒鸡汤", rule=to_me(), priority=1)
pyqwa = on_command("朋友圈文案", rule=to_me(), priority=1)
mrbd = on_command("//骂人宝典", rule=to_me(), priority=1)
dh = on_command("动画语录", rule=to_me(), priority=1)
mh = on_command("漫画语录", rule=to_me(), priority=1)
yx = on_command("游戏语录", rule=to_me(), priority=1)
wx = on_command("文学语录", rule=to_me(), priority=1)
yc = on_command("原创语录", rule=to_me(), priority=1)
lzwl = on_command("//来自网络", rule=to_me(), priority=1)
ys = on_command("影视语录", rule=to_me(), priority=1)
sc = on_command("诗词语录", rule=to_me(), priority=1)
wyy = on_command("网易云", rule=to_me(), priority=1)
zx = on_command("哲学语录", rule=to_me(), priority=1)
djl = on_command("//抖机灵", rule=to_me(), priority=1)


@quotation.handle()
async def handle_quotation(bot: Bot, event: Event):
    logger.success(f'quotation: {event}\n')
    response = await get_quotation()
    await quotation.send(response)


@twqh.handle()
async def handle_twqh(bot: Bot, event: Event):
    logger.success(f'quotation-twqh: {event}\n')
    response = await get_quotation(Config.mp['土味情话'])
    await twqh.send(response)


@jsyl.handle()
async def handle_jsyl(bot: Bot, event: Event):
    logger.success(f'quotation-jsyl: {event}\n')
    response = await get_quotation(Config.mp['精神语录'])
    await jsyl.send(response)


@wyyrp.handle()
async def handle_wyyrp(bot: Bot, event: Event):
    logger.success(f'quotation-wyyrp: {event}\n')
    response = await get_quotation(Config.mp['网易云热评'])
    await wyyrp.send(response)


@crxh.handle()
async def handle_crxh(bot: Bot, event: Event):
    logger.success(f'quotation-crxh: {event}\n')
    response = await get_quotation(Config.mp['成人笑话'])
    await crxh.send(response)


@qpdh.handle()
async def handle_qpdh(bot: Bot, event: Event):
    logger.success(f'quotation-qpdh: {event}\n')
    response = await get_quotation(Config.mp['奇葩对话'])
    await qpdh.send(response)


@tgrj.handle()
async def handle_tgrj(bot: Bot, event: Event):
    logger.success(f'quotation-tgrj: {event}\n')
    response = await get_quotation(Config.mp['舔狗日记'])
    await tgrj.send(response)


@djt.handle()
async def handle_djt(bot: Bot, event: Event):
    logger.success(f'quotation-djt: {event}\n')
    response = await get_quotation(Config.mp['毒鸡汤'])
    await djt.send(response)


@pyqwa.handle()
async def handle_pyqwa(bot: Bot, event: Event):
    logger.success(f'quotation-pyqwa: {event}\n')
    response = await get_quotation(Config.mp['朋友圈文案'])
    await pyqwa.send(response)


@mrbd.handle()
async def handle_mrbd(bot: Bot, event: Event):
    logger.success(f'quotation-mrbd: {event}\n')
    response = await get_quotation(Config.mp['骂人宝典'])
    await mrbd.send(response)


@dh.handle()
async def handle_dh(bot: Bot, event: Event):
    logger.success(f'quotation-dh: {event}\n')
    response = await get_quotation(Config.mp['动画'])
    await dh.send(response)


@mh.handle()
async def handle_mh(bot: Bot, event: Event):
    logger.success(f'quotation-mh: {event}\n')
    response = await get_quotation(Config.mp['漫画'])
    await mh.send(response)


@yx.handle()
async def handle_yx(bot: Bot, event: Event):
    logger.success(f'quotation-yx: {event}\n')
    response = await get_quotation(Config.mp['游戏'])
    await yx.send(response)


@wx.handle()
async def handle_wx(bot: Bot, event: Event):
    logger.success(f'quotation-wx: {event}\n')
    response = await get_quotation(Config.mp['文学'])
    await wx.send(response)


@yc.handle()
async def handle_yc(bot: Bot, event: Event):
    logger.success(f'quotation-yc: {event}\n')
    response = await get_quotation(Config.mp['原创'])
    await yc.send(response)


@lzwl.handle()
async def handle_lzwl(bot: Bot, event: Event):
    logger.success(f'quotation-lzwl: {event}\n')
    response = await get_quotation(Config.mp['来自网络'])
    await lzwl.send(response)


@ys.handle()
async def handle_ys(bot: Bot, event: Event):
    logger.success(f'quotation-ys: {event}\n')
    response = await get_quotation(Config.mp['影视'])
    await ys.send(response)


@sc.handle()
async def handle_sc(bot: Bot, event: Event):
    logger.success(f'quotation-sc: {event}\n')
    response = await get_quotation(Config.mp['诗词'])
    await sc.send(response)


@wyy.handle()
async def handle_wyy(bot: Bot, event: Event):
    logger.success(f'quotation-wyy: {event}\n')
    response = await get_quotation(Config.mp['网易云'])
    await wyy.send(response)


@zx.handle()
async def handle_zx(bot: Bot, event: Event):
    logger.success(f'quotation-zx: {event}\n')
    response = await get_quotation(Config.mp['哲学'])
    await zx.send(response)


@djl.handle()
async def handle_djl(bot: Bot, event: Event):
    logger.success(f'quotation-djl: {event}\n')
    response = await get_quotation(Config.mp['抖机灵'])
    await djl.send(response)
