## 帮助文档
<http://kagarise.cn/2021/05/01/bot/>

- 在src/plugins下的每个package中，都应含有config.py文件，用来存储一些配置信息或私密信息。
```python
# 如下以src/plugins/cat/config.py为例
class Config(object):
    cat_api_key = 'xxxxxxxxx'
    cat_headers = {
        'x-api-key': cat_api_key
    }

    dog_api_key = 'xxxxxxxxx'
    dog_headers = {
        'x-api-key': dog_api_key
    }
```
- 具体需要的配置信息可从各包下的data_source中提供的网址自行申请获取或联系QQ：3255385205获取更多帮助