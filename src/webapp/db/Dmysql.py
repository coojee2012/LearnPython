import logging; logging.basicConfig(level=logging.INFO)
import asyncio,aiomysql
import traceback
from config import config
'''
mysql 异步版本
'''

logobj = logging.getLogger('mysql')
class Dmysql:
    def __init__(self):
        self.coon = None
        self.pool = None

    async def initpool(self,loop,**kw):
        try:
            logobj.debug("will connect mysql~")
            self.pool = await aiomysql.create_pool(
                    host = config.mysql.host,
                    port = config.mysql.port,
                    user = config.mysql.user,
                    password = config.mysql.password,
                    db = config.mysql.database,
                    charset = config.mysql.charset,
                    autocommit = config.mysql.autocommit == 'True',
                    maxsize = int(config.mysql.maxsize),
                    minsize = int(config.mysql.minsize),
                    loop = loop)
        except:
            logobj.error('connect error.', exc_info=True)

    async def closepool(self):
        logobj.info('Closeing Mysql Pool....')
        self.pool.close()
        await self.pool.wait_closed()
    
    async def getCurosr(self,reDict=None):
        conn = await self.pool.acquire()
        cur = None
        if reDict:
            cur = await conn.cursor(aiomysql.DictCursor)
        else:
            cur = await conn.cursor()
        return conn,cur


    async def fetchone(self,sql, args=(), size=None):
        """封装select，查询单个，返回数据为字典"""
        logobj.info(sql, args)
        conn,cur = await self.getCurosr(reDict=True)
        try:
            await cur.execute(sql.replace('?', '%s'),args or ())
            return await cur.fetchone()
        except:
            logobj.error(traceback.format_exc())
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)

    async def query(self, query,param=None, size=None):
        """封装query，查询多个，返回数据为列表"""
        conn,cur = await self.getCurosr(reDict=True)
        try:
            await cur.execute(query.replace('?', '%s'),param or ())
            if size:
                return await cur.fetchmany(size)
            return await cur.fetchall()
        except:
            logobj.error(traceback.format_exc())
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)

    async def execute(self,sql, args):
        """封装insert, delete, update"""
        conn,cur = await self.getCurosr()
        try:
            await cur.execute(sql.replace('?', '%s'),args)
            affected = cur.rowcount
            return affected
        except:
            logobj.error(traceback.format_exc())
            await conn.rollback()
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)


mysql = Dmysql()