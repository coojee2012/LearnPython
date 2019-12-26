import logging; logging.basicConfig(level=logging.INFO)
import asyncio,aioredis
import traceback
from config import config

class Dredis:
    _reids_pool = None

    async def init_pool(self, loop):
        if not self._reids_pool:
            self._reids_pool = await aioredis.create_pool(
                address=(config.redis.host, config.redis.port),
                db=config.redis.db, 
                password=config.redis.password,
                minsize=config.redis.minsize, 
                maxsize=config.redis.maxsize, 
                loop=loop)
        else:
            logging.info('redis pool had inited')
    
    def get_pool(self):
        return self._reids_pool

    async def close(self):
        if self._reids_pool:
            logging.info('closing redis pool')
            self._reids_pool.close()
            await self._reids_pool.wait_closed()

    async def get_value(self,key):
        with await aioredis.commands.Redis(self._reids_pool) as redis:
            await redis.get(key)

    async def cache_set(self,*args, **kwargs):
        """redis set 命令封装"""
        with await aioredis.commands.Redis(self._reids_pool) as redis:
            await redis.set(*args, **kwargs)


    async def cache_get(self,*args, **kwargs):
        """redis get 命令封装"""
        with await aioredis.commands.Redis(self._reids_pool) as redis:
            return await redis.get(*args, **kwargs)


    async def cache_del(self,*args, **kwargs):
        """redis del 命令封装"""
        with await aioredis.commands.Redis(self._reids_pool) as redis:
            return await redis.delete(*args, **kwargs)

redis = Dredis()