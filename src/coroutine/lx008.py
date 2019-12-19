import asyncio
import time
import threading

#定义一个异步操作
async def hello1(a,b):
    print(f"异步函数开始执行")
    await asyncio.sleep(3)
    print("异步函数执行结束")
    return a+b

#在一个异步操作里面调用另一个异步操作
async def main():
    c = await hello1(10,20)
    print(c)
    print("主函数执行")

loop = asyncio.get_event_loop()
tasks = [main()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

'''运行结果为：
异步函数开始执行（在此处要等待3秒）
异步函数执行结束
30
主函数执行
'''