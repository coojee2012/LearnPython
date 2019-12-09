'''
这是一个用来测试的模块
'''
class TeatClass:
    '''
    一个测试模块中的类
    '''
    def __init__(self,name):
        self.name = name
    def add(self,a,b):
        print("对象name:",self.name)
        return a + b
def add(a,b):
    '''
    测试模块中的加法
    '''
    return a + b

testClass = TeatClass('test')
print("我被导入了，名字是：",__name__)
if __name__ == "__main__":
    print(add(1,2))
    print(testClass.add(3,5))

