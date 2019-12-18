'''
死锁样例
'''
import time
from threading import Thread,Lock
import threading
mutexA=threading.Lock()
mutexB=threading.Lock()

class MyThread1(Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name,'执行开始')
            time.sleep(1)
            if mutexB.acquire():
                print(self.name,'执行结束')
                mutexB.release()
            mutexA.release()


class MyThread2(Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name,'执行开始')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name,'执行结束')
                mutexA.release()
            mutexB.release()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    # t1.join() 这样就不会死锁了 ：）
    t2.start()
    # t2.join()
