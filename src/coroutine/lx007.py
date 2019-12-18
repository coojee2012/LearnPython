import asyncio
import time
from functools import partial

async def get_url():
    print('start get url')
    await asyncio.sleep(2)          # await 后面跟的必须是一个await对象
    print('end get url')
    return 'stack'

def test(url,future):
    print(url,'hello, stack')

if __name__ == '__main__':
    start = time.time()
    
    loop = asyncio.get_event_loop()

    # loop.run_until_complete(get_url())      # 只是提交了一个请求，时间2s

    tasks = [get_url() for i in range(10)]

    # get_future = asyncio.ensure_future(get_url())
    # 获得返回值用法1，源码上依然是先判断loop，然后调用create_task

    # get_future = loop.create_task(get_url())
    # 方法2，还可以继续添加函数，执行逻辑
    # get_future.add_done_callback(partial(test, 'Stack'))
    # 函数本身在获得调用时需要一个任意形数，参数即是 get_future 本身,否则报错
    # 如果函数需要传递参数，需要通过 偏函数 partial 模块来解决，以及函数的形参需要放在前面


    loop.run_until_complete(asyncio.wait(tasks))  # 提交了10次，时间也是2s
     # loop.run_until_complete(asyncio.gather(*tasks)) 效果同上
     # gather 和 wait 的区别
     # gather是更高一级的抽象，且使用更加灵活，可以使用分组，以及取消任务
    print(time.time() - start)
    # print(get_future.result())          # 接收返回值