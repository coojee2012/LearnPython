import numpy

a = numpy.arange(10)
print(a)
print([1,2,3])

a = numpy.array([1,2,3,4,5])
print(a)
print('数组的纬度:',a.shape)

a = numpy.array([[1,2],[3,4],[5,6]])
print(a)
print('数组的纬度:',a.shape) # (3,2) 元祖 

a = numpy.array([1,2,3,4,5],dtype=complex)
print(a) # [1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]

a = numpy.array([1,2,3,4,5],dtype=str)
print(a) # ['1' '2' '3' '4' '5']

a = numpy.array([1,2,3,4,5],dtype=float)
print(a) # [1. 2. 3. 4. 5.]

# 下面一行会报错，无法执行类型转换
# a = numpy.array(['a','ab','abc'],dtype=float)

a = numpy.random.random()
print(a) # 0.06455816280746518

a = numpy.random.random(size=5) # 默认纬度为1，返回5个元素
print(a) # [0.27491128 0.88209578 0.51427515 0.29271653 0.68469252]

a = numpy.random.random(size=(3,2)) # 元祖第一个是纬度，第二个元素的个数
print(a) # [[0.03223149 0.30336649] [0.8409066  0.8987153 ] [0.83928391 0.68419613]]

a = numpy.random.randint(4)
print(a)

a = numpy.random.randint(4,10)
print(a)

a = numpy.random.randint(4,10,size=(3,4,2))
print(a) # 第一纬度3个元素，第二纬度4个元素,第三纬度2个元素 随机数在最里面的纬度

a = numpy.random.normal(loc=3,scale=4,size=(2,2))
print(a)

x = numpy.zeros(5)
print(x)
x = numpy.zeros((5,),dtype=int)
print(x)
x = numpy.zeros((2,2),dtype=str)
print(x)


x = numpy.ones((5,),dtype=int) # 
print(x)
x = numpy.ones((2,2),dtype=str) #[['1' '1']['1' '1']]
print(x)


b = numpy.empty((5,),dtype=int)
print(b)
b = numpy.empty((2,2),dtype=str) 
print(b)

a = numpy.arange(10)
b = a[2:7:1]
c = a[3:]
print(a,b,c) # [0 1 2 3 4 5 6 7 8 9] [2 3 4 5 6] [3 4 5 6 7 8 9]


