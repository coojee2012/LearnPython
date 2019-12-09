import module001 # 文件名，不是路径
import module001 as a
print(module001.testClass.add(3,8))
print(module001.add(11,12))
test = module001.TeatClass('my_test')
print(test.add(10,10))
print(a.testClass.add(3,8))

print(module001.__doc__)