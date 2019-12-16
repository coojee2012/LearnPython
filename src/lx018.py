import numpy

a = numpy.arange(1,13)
print(a)
b = a.reshape(2,3,2)
print(b)
c = b.ravel()
print(c)
d = c.flatten()
print(d)

aa = numpy.arange(0,36).reshape(3,4,3)
bb = numpy.arange(36,72).reshape(3,4,3)



cc = numpy.vstack([aa,bb])

dd = numpy.hstack([aa,bb])
print(dd)

ee = numpy.dstack([aa,bb])
print(ee)