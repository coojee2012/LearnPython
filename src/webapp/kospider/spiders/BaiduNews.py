import asyncio
from kospider.Spider import Spider
from kospider.logger import get_logger
class BaiduNews(Spider):
    def __init__(self,queue):
        self.q = queue
        self.logger = get_logger('BaiduNews Spider')
    async def __start(self):
        self.logger.info('BaiduNews Spider start')
        await asyncio.sleep(10)
        self.logger.info('BaiduNews Spider end')