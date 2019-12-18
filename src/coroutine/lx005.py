import time
import asyncio
async def say_after_time(delay,what):
        await asyncio.sleep(delay)
        print(what)

async def main():
        print(f"开始时间为： {time.time()}")
        await say_after_time(1,"hello")
        await say_after_time(2,"world")
        print(f"结束时间为： {time.time()}")
        
''' 直接运行 '''        
# >>> main()
# <coroutine object main at 0x1053bb7c8>       

'''  需要通过事件循环来调用'''
loop=asyncio.get_event_loop()    #创建事件循环对象
#loop=asyncio.new_event_loop()   #与上面等价，创建新的事件循环
loop.run_until_complete(main())  #通过事件循环对象运行协程函数
loop.close()


