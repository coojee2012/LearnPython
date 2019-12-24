import logging; logging.basicConfig(level=logging.INFO)
import asyncio,aiomysql
import traceback

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
                    host=kw.get('host', 'localhost'),
                    port=kw.get('port', 3306),
                    user=kw['user'],
                    password=kw['password'],
                    db=kw['database'],
                    charset=kw.get('charset', 'utf8'),
                    autocommit=kw.get('autocommit', True),
                    maxsize=kw.get('maxsize', 10),
                    minsize=kw.get('minsize', 1),
                    loop=loop)
        except:
            logobj.error('connect error.', exc_info=True)

    async def closepool(self):
        logobj.info('Closeing Mysql Pool....')
        self.pool.close()
        await self.pool.wait_closed()
    
    async def getCurosr(self):
        conn = await self.pool.acquire()
        cur = await conn.cursor()
        return conn,cur


    async def query(self, query,param=None, size=None):
        conn,cur = await self.getCurosr()
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
        conn,cur = await self.getCurosr()
        try:
            await cur.execute(sql.replace('?', '%s'),args)
            affected = cur.rowcount
            return affected
        except:
            logobj.error(traceback.format_exc())
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)


mysql = Dmysql()