
from multiprocessing import Process,set_start_method,Pool
set_start_method('spawn',True)

import os
import time

num=1
def work1():
    global num
    num+=5
    print('子进程1运行，num:',num)

def work2():
    global num
    num += 10
    print('子进程2运行，num：',num)

if __name__=='__main__':
    print('父进程开始运行')
    p1=Process(target=work1)
    p2=Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程结束')