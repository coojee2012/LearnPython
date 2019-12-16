from multiprocessing import Process,Queue,set_start_method
import time,random,os

set_start_method('spawn',True)
def consumer(q):
   
    while True:
        res=q.get()
        if not res:
            break
        time.sleep(random.randint(1,3))
        print('{} 吃 {}'.format(os.getpid(),res))
 
def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('生产了 {} {}'.format(os.getpid(),res))
    q.put(None) # 告诉消费者包子没了
if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))
 
    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))
 
    #开始
    p1.start()
    c1.start()

    p1.join()
    print('包子做完了')
    # q.put(None) 主进程也可以告诉包子没了
    c1.join()
    print('包子吃完了')
    print('主进程结束了')