def consume():
    r = ''
    while True:
        n = yield r        # 断点
        if not n:
            return
        print('消费者 正在消费: {}'.format(n))
        r = '200 RMB'
        
def produce(c):
    c.send(None)    # 启动生成器
    n = 0
    while n < 5:
        n += 1
        print('生产者正在生产： {}'.format(n))
        r = c.send(n)
        print('[生产者] 消费者返回： {}'.format(r))
        print('------------')
    c.close()
c = consume()
produce(c)


def my_generator(n):
    for i in range(n):
        temp = yield i
        print(f'我是{temp}')

g=my_generator(6)

print(next(g)) #输出0， 打印结果，我是None
print(next(g)) #输出1
g.send(100)    #temp的打印结果为100
print(g.send(100))       #输出2
print(next(g)) #输出3
print(next(g)) #输出4