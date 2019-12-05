'''
打印九九乘法表
'''
for x in range(1,10):
    for y in range(x,10):
        print('{0:^3}x{1:^3}={2:^4}'.format(x,y,x*y),end=" ")
    print("")