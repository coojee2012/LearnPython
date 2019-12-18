import time
import threading
from queue import Queue

class Producer(threading.Thread):
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)

    def run(self):
        self.product()
    def product(self):
        queue,msg = self._args
        print(msg)
        while True:
            if queue.qsize() < 1000:
                for i in range(10):
                    queue.put('包子-{}'.format(i))
            else:
                print("生产完了！")
                break
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)
    def run(self):
        self.consumer()
    def consumer(self):
        queue,msg = self._args
        print(msg)
        while True:
            if queue.qsize() > 0:
                baozi = queue.get()
                print('我吃了包子：{}'.format(baozi))
            else:
                print("消费完了！")
                break
            time.sleep(0.5)


if __name__ == '__main__':
    queue = Queue()
    producer = Producer(None,'Producer',(queue,'邻家包子铺'))
    producer.start()
    
    time.sleep(1)
    consumer = Consumer(None,'Consumer',(queue,'大口吃包子'))
    consumer.start()
    