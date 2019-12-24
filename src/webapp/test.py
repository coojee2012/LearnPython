import asyncio
from db.Dmysql import mysql
from models.User import User


async def generator2():
    await asyncio.sleep(1)
    return 100

async def test(loop):
    await mysql.initpool(loop=loop,user='root', password='root', database='awesome')

    u = User(name='Test', email='test001@example.com', passwd='1234567890', image='about:blank')

    a = await generator2()
    print(a)
    b = await u.save()
    print(b)


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()