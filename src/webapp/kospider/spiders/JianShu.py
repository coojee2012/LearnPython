import asyncio
from kospider.Spider import Spider
from kospider.Seed import Seed


dict_filter = {
    # 旅行·在路上
    # '5AUzod': "电影",
    # 简书电影
    '1hjajt': "电影",
    # # # 美妆·护肤·穿搭
    '025246642a19': "时尚",
    # # # 美食
    'qqfxgN': "美食",
    # # # 电竞·游戏
    '0856231c8e98': "游戏",
    # # # 萌宠
    '88b891fe2acb': "体育",
    # # # 设计
    '3063e24c8622': "时尚",
    # # # 运动&健身
    'snqjhw': "体育",
    # # 摄影
    '7b2be866f564': "旅游"
}

headers_ = {
    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +",
    "Referer": "http://www.jianshu.com"
}

class JianShu(Spider):
    def __init__(self,queue):
        self.q = queue

    async def start(self):
        print('JianShu Spider start')
        await asyncio.sleep(0.3)
        for url in dict_filter:
            seed = Seed('http://www.jianshu.com/c/{}'.format(url),self.next_parse,headers=headers_)
            self.q.put_nowait(seed)
        print('JianShu Spider end')

    async def next_parse(self,data):
        print(data)