def factorial(n):
    '''
    阶乘函数练习，用递归实现，并打印.
    阶乘：
    一个正整数的阶乘是所有小于及等于该数的正整数的积，并且有0的阶乘为1。
    '''
    if n < 0:
        print('必须计算大于等于0的数')
    if n ==0 or n==1:
        return 1
    return n * factorial(n-1)

for x in range(0,11):
    print('{0}! = {1}'.format(x,factorial(x)))