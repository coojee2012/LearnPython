import asyncio
from orm.orm import create_pool
from models.User import User


async def generator2():
    await asyncio.sleep(10)
    return 100

async def test(loop):
    await create_pool(loop=loop,user='root', password='root', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    print(u.save)
    a = await generator2()
    print(a)
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()