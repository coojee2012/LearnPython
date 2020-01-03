import asyncio
from kospider.engine import Engine
from db.Dmysql import mysql
from db.Dredis import redis

def main(loop):
    print('starting kospider server')
    coros = [mysql.initpool(loop=loop), redis.init_pool(loop=loop)]
    loop.run_until_complete(asyncio.gather(*coros))
    
    engine = Engine(loop=loop)
    engine.run()

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
    print('stoped kospider server')
except BaseException as e:
    print('Main error',e)
finally:
    event_loop.close()    # 当轮训器关闭以后，所有没有执行完成的协成将全部关闭