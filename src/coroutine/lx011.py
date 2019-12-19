import asyncio
async def delay(time):
    await asyncio.sleep(time)

async def timer(time,function):
    while True:
        future=asyncio.ensure_future(delay(time))
        await future
        future.add_done_callback(function)

def func(future):
    print('done')

if __name__=='__main__':
    asyncio.run(timer(2,func))