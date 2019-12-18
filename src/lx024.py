import time
from threading import Thread,Lock
#定义全局变量num
num=0
#创建一把互斥锁
mutex=Lock()
def test1():
    global num
    '''
    在两个线程中都调用上锁的方法，则这两个线程就会抢着上锁，
    如果有1方成功上锁，那么导致另外一方会堵塞（一直等待）直到这个锁被解开
    '''
    
    for i in range(100):
        mutex.acquire()#上锁
        num+=1
        mutex.release()
    print('test1输出num:',num)

def test2():
    global num
    
    for i in range(100):
        mutex.acquire()  # 上锁
        num+=1
        mutex.release()
    print('test2输出num:',num)
    
    

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
