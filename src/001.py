class Test:
    def __init__(self):
        self.__age = 18 # 不能直接访问了
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,n):
        if n > 100 or n < 0:
            print("age must in [0-100]")
            return
        self.__age = n
test = Test()
myAge = test.age
print('my age is:{}'.format(myAge))
test.age = 300
myAge = test.age
print('my age is:{}'.format(myAge))
test.age = 50
myAge = test.age
print('my age is:{}'.format(myAge))