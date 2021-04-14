import httpx


async def get_setu_url():
    api = 'https://api.mtyqx.cn/api/random.php?return=json'
    data = eval(httpx.get(api).text)
    if data['code'] == '200':
        return data['imgurl'].replace('\\', '')
    else:
        return 'ERROR：setu请求错误'
# {'code': '200',
# 'imgurl': 'https:\\/\\/tva4.sinaimg.cn\\/large\\/0072Vf1pgy1fodqi5vxrij31630rsu0x.jpg',
# 'width': '1515', 'height': '1000'}
