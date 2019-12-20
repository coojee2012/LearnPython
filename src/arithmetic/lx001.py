import time
from utils import metric


@metric()
def findabc():
    for a in range(1001):
        for b in range(1001):
            c = 1000 - (a +b)
            if c + a + b == 1000  and a**2+b**2==c**2: 
                print('a,b,c:',a,b,c)


# findabc()

@metric()
def bubble_sort(*args):
    alist = list(args)
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist
li = [3,2,8,7,10,13,1,3,40,9,30]
print(bubble_sort(*li))

@metric()
def selection_sort(*args):
    alist = list(args)
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index], alist[i]
    return alist

print(selection_sort(*li))

@metric()
def insert_sort(*args):
    alist = list(args)
    n = len(alist)
    for j in range(1,n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else:
                break
            i -= 1
    return alist
print(insert_sort(*li))




