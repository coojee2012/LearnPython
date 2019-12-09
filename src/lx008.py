from pk01 import module01
from pk01.pk0101 import module0101

import pk01.module01 as m1
print(module01.add(1,2))
print(module01.duble('a'))
print(module0101.sum(3,4))

print(m1.duble("abc"))

print(module01)
print(m1)

print(id(module01))
print(id(m1))