import time
from utils import metric

test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
@metric()
def binld_search(alist,item):
    first = 0
    last = len(alist)
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid] :
            last = mid - 1
        else:
            first = mid + 1
    return False

print(binld_search(test_list,5))
print(binld_search(test_list,10))


@metric()
def binld_search2(alist,item):
    first = 0
    last = len(alist)
    mid = (first+last)//2
    if alist[mid] == item:
        return True
    else:
        if item < alist[mid]:
            return binld_search2(alist[:mid],item)
        else:
            return binld_search2(alist[mid:],item)

print(binld_search2(test_list,5))
print(binld_search2(test_list,10))



