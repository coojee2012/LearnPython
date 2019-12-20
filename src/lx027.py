# -*- coding: utf-8 -*-
from functools import reduce
def normalize(name):   
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y: x*y,L)
print(prod([1,2,3,4,5]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
def str2float(s):
    strs = s.split('.')
    a1 = list(map(lambda x: DIGITS[x],strs[0]))
    a2 = list(map(lambda x: DIGITS[x],strs[1]))
    r1 = reduce(lambda x,y: x*10+y,a1)
    r2 = reduce(lambda x,y: x*10+y,a2) 
    return r1 + r2*10**(0-len(a2))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

t1 = _odd_iter()
while next(t1) < 100:
    print(next(t1))

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

def is_palindrome(n):
    nstr = list(map(str,n))
    rstr = filter(lambda x: x == x[::-1],nstr)
    return list(map(int,rstr))

print(is_palindrome(range(1,1000)))