class Car:
    def __init__(self):
        print('make a car')
    def honk(self):
        print('喇叭滴滴滴')
class BWM(Car):
    def __init__(self):
        print('make a BWM car')
        Car.__init__(self)
    def honk(self):
        print('宝马来了请闪开')
class BYD(Car):
    def __init__(self):
        print('make a BYD car')
        Car.__init__(self)
    def honk(self):
        print('BYD正在向你靠近')
def honk(car):
    if isinstance(car,Car):
        car.honk()
    else:
        print("没车别哔哔哔")


bwm = BWM()
byd = BYD()
honk(bwm)
honk(byd)
honk(None)


class StarFactory:
    def __init__(self):
        print("欢迎使用明星工厂")
    def createStar(self,name):
        if name == 'man':
            return ManStar()
        elif name == "woman":
            return WomanStar()
        else:
            print("你想成为什么样的明星？")
class ManStar:
    def __init__(self):
        print("我是一名超级男明星")
class WomanStar:
    def __init__(self):
        print("我是一名超级女明星")

factory = StarFactory()
factory.createStar("man")
factory.createStar("woman")
factory.createStar("womam")