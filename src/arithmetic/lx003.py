from timeit import Timer

def append_test():
    li = []
    for i in range(10000):
        li.append(i)
def insert_test():
    li = []
    for i in range(10000):
        li.insert(0,i)

timer1 = Timer('append_test()','from __main__ import append_test')
print('append:',timer1.timeit(1000))

timer2 = Timer('insert_test()','from __main__ import insert_test')
print('insert:',timer2.timeit(1000))