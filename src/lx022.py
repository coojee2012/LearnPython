import time
from threading import *
#定义全局变量num
num=10
def test1():
    global num
    for i in range(3):
        num+=1
    print('test1输出num:',num)

def test2():
    global num
    print('test2输出num:',num)

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
