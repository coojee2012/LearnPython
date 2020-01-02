import asyncio
from kospider.Spider import Spider

class BaiduNews(Spider):
    def __init__(self,session):
        self.session = session
    async def start(self):
        print('BaiduNews Spider start')
        await asyncio.sleep(10)
        print('BaiduNews Spider end')
        pass