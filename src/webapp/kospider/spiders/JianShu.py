import asyncio,re
from kospider.Spider import Spider
from kospider.Seed import Seed
from kospider.selectors import Xpath
from kospider.logger import get_logger

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
    '7b2be866f564': "旅游",
    'e048f1a72e3d': "简书大学堂"
}

headers_ = {
    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +",
    "Referer": "http://www.jianshu.com"
}

class JianShu(Spider):
    def __init__(self,queue):
        self.q = queue
        self.logger = get_logger('JianShu Spider')

    async def start(self):
        self.logger.info('JianShu Spider start')
        await asyncio.sleep(0.3)
        for url in dict_filter:
            seed = Seed('http://www.jianshu.com/c/{}'.format(url),self.next_parse,headers=headers_)
            self.q.put_nowait(seed)
            await asyncio.sleep(1)
        self.logger.info('JianShu Spider end')

    async def next_parse(self,data):
        try:
            selector = Xpath('//*[@class="content"]/a/@href')
            urls = selector.parse_detail(data)
            for url in urls:
                # 添加到url列表中
                _url = 'http://www.jianshu.com' + url
                seed = Seed('http://www.jianshu.com{}'.format(url),self.parser,headers=headers_)
                self.q.put_nowait(seed)
            #print(urls)
        except BaseException as e:
            self.logger.error(e)

    async def parser(self,data):
        try:
            # print('jianshu parser',data)
            title = Xpath('//section/h1/text()').parse_detail(data)[0]    
            content = Xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article',r_type='elstr').parse_detail(data)[0]        
            content = re.sub(' src=".*?"', '', content)
            content = content.replace('data-original-src="//', 'src="https://')
        
            content = content.replace('图片发自简书App', '')
            # print(title)
            # print(content)
        except BaseException as e:
            self.logger.error(e)