from time import perf_counter
import math
start = perf_counter()
pi = 0
D = 1000 * 100
for x in range(1,D+1,4):
    print(x)
    pi += (4/x-4/(x+2))

print("圆周率值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start))




     
        
