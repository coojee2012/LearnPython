# -*- coding: utf-8 -*-

import  time
def createCounter():
    i = []
    def counter():
        i.append(1)
        return len(i)
    return counter

counter = createCounter()
for i in range(1,100):
    print(counter())


def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print('{} {}():'.format(text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

@log("debug")
def now():
    print('Now time is 00:00')

now()


def metric(level):
    def decorator(func):
        def wrapper(*args, **kw):
            print('{}:{} executed in {} ms'.format(level,func.__name__, time.time()))
            return func(*args, **kw)
        return wrapper
    return decorator

@metric('debug')
def test():
    return 1+1

@metric('debug')
def test2():
    return 2+2

test()
test2()
