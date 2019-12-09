class Parent:
        def __init__(self,name):
            self.name = name
            print("call parent init.")
        def say_name(self):
            print('My Name Is:',self.name)
class Children(Parent):
    def __init__(self,name,age):
        self.age = age
        Parent.__init__(self,name)
    def say_age(self):
        print("I am a children,my age is:",self.age)
    def say_name(self):
        super().say_name()
        print("I am a children,my name is:",self.name)
    def __str__(self):
        return "I am a children"
p = Parent("父亲")
c = Children("孩子",18)
p.say_name()
c.say_name()
c.say_age()
print(p)
print(c)
print(type(p))
print(type(c))
print(Children.mro())
print(Children.__mro__)
print(c.__str__())

