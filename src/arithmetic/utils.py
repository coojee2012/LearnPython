import time
def metric():
    def decorator(func):
        def wrapper(*args, **kw):
            t1 = time.time()
            res = func(*args, **kw)
            t2 = time.time()
            print('函数{}执行了:{}ms'.format(func.__name__, t2 - t1))
            return res
        return wrapper
    return decorator