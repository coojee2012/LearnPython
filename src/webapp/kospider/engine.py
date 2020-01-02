import os
import sys
import socket
import asyncio
import aiohttp
import types
from datetime import datetime
import re
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


from kospider.Spider import Spider
from kospider.Seed import Seed
from kospider.logger import get_logger

MAX_TASKS = 100
class Engine:
    def __init__(self,loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.max_tasks = MAX_TASKS
        self.conn = aiohttp.TCPConnector(family=socket.AF_INET,
                                         verify_ssl=False,
                                         use_dns_cache=True)
        self.session = aiohttp.ClientSession(loop=self.loop, connector=self.conn)
        self.q = asyncio.Queue(loop=loop, maxsize=MAX_TASKS)
        self.logger = get_logger('engine')
    

    def run(self):
        self.logger.info('Spider Engine started!')
        start_time = datetime.now()
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.crawler())
            # self.session.close()
        except KeyboardInterrupt:
            for task in asyncio.Task.all_tasks():
                task.cancel()
            loop.run_forever()
        finally:
            end_time = datetime.now()
            self.logger.info('Time usage: {}'.format(end_time - start_time))

    async def crawler(self):
        await self.init_spiders()
        workers = [asyncio.Task(self.worker(), loop=self.loop)
                   for _ in range(self.max_tasks)]
        await self.q.join()

        for w in workers:
            w.cancel()
        
    async def worker(self):
        try:
            while True:
                task = await self.q.get()
                if isinstance(task,Spider):
                    await task.start()
                elif isinstance(task,Seed):
                    data = await self.fetch(**task)
                    await task.callback(data)
                self.q.task_done()

                """告诉队列 处理完毕"""
        except asyncio.CancelledError:
            pass

    async def init_spiders(self):
        old_path = os.path.dirname(os.path.abspath(__file__))
        print('old_path',old_path)
        for dirName, subdirList, fileList in os.walk('/Users/lynn/xcode/LearnPython/src/webapp/kospider/spiders'):
            sys.path.append(dirName)
            for fname in fileList:
                if re.match(r'[_,a-z,A-Z]+.py$', fname):
                    mod_name = fname.split('.')[0]
                    mod = __import__(mod_name, globals(), locals())
                    for attr in dir(mod):
                        print(attr)
                        if attr != mod_name: # 定义蜘蛛的文件名必须和类名一致
                            continue
                        fn = getattr(mod, attr)
                        # Python如何判断fn是一个类呢？
                        spider = fn(self.q)
                        self.q.put_nowait(spider)
                                 
            if len(subdirList) > 0:
                subdirList = subdirList[1:]
        sys.path.append(old_path)

    async def fetch(self, url,  headers=None, data_type='normal', proxy=None,**kw):
        try:
            print("url is {} proxy {}".format(url, proxy))
            async with self.session.get(url, headers=headers, proxy=proxy) as r:
                print("get {} status_code is {}".format(url, r.status))
                if r.status == 200:
                    if data_type == 'image':
                        data = await r.read()
                    else:
                        data = await r.text()
                    return data
                else:
                    print("get {} is err: {}".format(url, r.status))
                    return None
        except Exception as e:
            print("err is {}".format(e))
            return None