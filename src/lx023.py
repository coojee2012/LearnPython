import time
from threading import *
#定义全局变量num
num=0
def test1():
    global num
    for i in range(100000):
        num+=1
    print('test1输出num:',num)

def test2():
    global num
    for i in range(100000):
        num+=1
    print('test2输出num:',num)

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
