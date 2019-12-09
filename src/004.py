class Singleton:
    __obj = None
    __hasInited = False
    def __init__(self,name):
        print("try init....")
        self.name = name
        if Singleton.__hasInited == False:
            Singleton.__hasInited = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def say_name(self):
        print(self.name)
        
a = Singleton("a")
b = Singleton("b")
print(a)
print(b)
a.say_name()
b.say_name()