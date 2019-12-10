# 第五天 函数和面向对象(2)

今天主要学习面向对象的三大特征：封装、继承、多态以及简单的设计模式和模块化。学习项目及练习源码地址：[GitHub源码](https://github.com/coojee2012/LearnPython)

## 面向对象的三大特征

### object类
object类是所有类的父类，因此所有的类都有object类的属性和方法。类定义中没有指定父类，则默认父类是object类。
### 封装
隐藏对象的属性和实现细节，外提供必要的方法。相当于将“细节封装起来”，只对外暴露“相关调用方法”。通过Python的“私有属性、私有方法”的方式，来实现“封装”。Python没有严格的语法级别的“访问控制符”，更多的是依靠程序员自觉实现。
### 继承
继承可以让子类具有父类的特性，提高了代码的重用性。
从设计上是一种增量进化，原有父类设计不变的情况下，可以增加新的功能，或者改进已有的算法(重写也叫重载父类的方法)。
- 语法

    ```python
    class 子类类名(父类 1[，父类 2，...]):

        类体
    ```
- 定义子类时，必须在其构造函数中调用父类的构造函数。
- 子类继承了父类**除构造方法之外**的所有成员(包括属性和方法）。
- 子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为“重写“
- 子类中可以通过super关键字调用父类的方法
- 可以使用类方法mro()或类属性__mro__获取其层次
- 内置函数dir()，可以方便的看到指定对象所有的属性和方法
- 对象方法：\_\_str__()用于返回一个对于“对象的描述”，对应于内置函数str()，内置函数print()就是调用对象的这个方法的返回值。
- 看语法，Python是支持多重继承的
  
    ```python
    class Parent:
            def __init__(self,name):
                self.name = name
                print("call parent init.")
            def say_name(self):
                print('My Name Is:',self.name)
    class Children(Parent):
        def __init__(self,name,age):
            self.age = age
            Parent.__init__(self,name) # 此处不可以用super().__init__代替
        def say_age(self):
            print("I am a children,my age is:",self.age)
        def say_name(self):
            print("I am a children,my name is:",self.name)
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
    '''
    输出结果如下：
    call parent init.
    call parent init.
    My Name Is: 父亲
    I am a children,my name is: 孩子
    I am a children,my age is: 18
    <__main__.Parent object at 0x10bf69ed0>
    <__main__.Children object at 0x10bfcb1d0>
    <class '__main__.Parent'>
    <class '__main__.Children'>
    [<class '__main__.Children'>, <class '__main__.Parent'>, <class 'object'>]
    '''
    ```

### 多态
多态(polymorphism)是指同一个方法调用由于对象不同可能会产生不同的行为。
- 多态是方法的多态，属性没有多态
- 多态的存在有 2 个必要条件:继承、方法重写。
  
    ```python
    class Car:
        def __init__(self):
            print('make a car')
        def honk(self):
            print('喇叭滴滴滴')
    class BWM(car):
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
    ```
## 简单的设计模式
什么是设计模式？

前人总结的一系列解决各种场景问题的套路。

### 工厂模式
顾名思义：所谓工厂模式就是一个对象根据调用参数的不同，可以生产许多不同的对象。

```python
class StarFactory:
    def __init__(self):
        print("欢迎使用明星工厂")
    def createStar(self,name):
        if name == 'man':
            return ManStar()
        elif name == "womam":
            return WomanStar()
class ManStar:
    def __init__(self):
        print("我是一名超级男明星")
class WomanStar:
    def __init__(self):
        print("我是一名超级女明星")
```

### 单列模式
单例模式(Singleton Pattern)的核心作用是确保一个类只有一个实例，并且提供一个访问该实例的全局访问点。单例模式只生成一个实例对象，减少了对系统资源的开销。当一个对象的产生需要比较多的资源，如读取配置文件、产生其他依赖对象时，可以产生一个“单例对象”，然后永久驻留内存中，从而极大的降低开销。

- 使用__new__方法
- 类实例对象在Python的模块时是天然的单例模式

    ```python
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
    '''
    try init....
    try init....
    <__main__.Singleton object at 0x10882dad0>
    <__main__.Singleton object at 0x10882dad0>
    b 这里不是a，说明第二次改变了第一次对象的值，是一个坑
    b 
    '''

    ```
## 模块和包
使用模块化编程便于将一个任务分解成多个模块，实现团队协同开发，完成大规模程序。实现代码复用和可维护性。
### 模块
- 一个模块对应python源文件，一般后缀名是:.py
- 标准库模块

    Python 标准库提供了操作系统功能、网络通信、文本处理、文件处理、数学运算等基 本的功能。比如:random(随机数)、math(数学运算)、time(时间处理)、file(文件处理)、os(和操作系统交互)、sys(和解释器交互)等。
- 第三方模块
- 用户自动模块

#### 导入模块

[测试模块](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/module001.py)

[测试代码](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/lx005.py)
- import语句
  
    ```python
    import 模块名 # 导入一个模块
    import 模块 1，模块 2...  # 导入多个模块
    import 模块名 as 模块别名 # 导入模块并使用新名字
    ```

    import加载的模块分为四个通用类别:
    1. 使用 python 编写的代码(.py文件); 
    2. 已被编译为共享库的C、C++扩展; 
    3. 包好一组模块的包
    4. 使用C编写并链接到python解释器的内置模块;
- from...import
  
  from...import 导入的是模块中的一个函数/一个类。

- 动态导入:内置函数\_\_import__()可以实现动态导入模块
- 使用importlib模块实现动态导入
- 每个模块都有一个名称，通过特殊变量__name__可以获取模块的名称
  
   一般情况下__name__输出模块名字，对应源文件名。仅有一个例外，就是当一个模块被作为程序入口时(主程序、交互式提示符下)，它的__name__的值为“\_\_main__”。我们可以根据这个特 点，将模块源代码文件中的测试代码进行独立的处理。

- 当导入一个模块时，模块中的代码都会被执行。如果再次导入这个模块，不会再次执行。

    ```python
    import math
    print(math.__name__)

    ```
### 包
当需要把多个模块放在一起时，需要就需要用到包了
- Python中的包就是一个必须有__init__.py的目录

    1. 作为包的标识，不能删除。
    2. 用来实现模糊导入
    3. 导入包实质是执行__init__.py文件，可以在__init__.py文件中做这个包的初始化、以及需要统一执行代码、批量导入。
- 导入包
  
    ```python
    import 包名.模块名
    import 包名.子包名.模块名
    from 包名.模块名 import 函数，类，变量
    ```
- 包下面可以包含“模块(module)”，也可以再包含“子包(subpackage)”
- 如果是子包内的引用，可以按相对位置引入子模块

    ```python
    from .. import 模块文件名 # 导入上层目录中的模块文件
    from . import 模块文件名 # 导入本层目录的模块文件
    ```
- sys.path和模块搜索路径

    当导入某个模块文件时，Python解释器一般按照如下路径寻找模块文件(按照顺序寻找，找到即停不继续往下寻找):
    1. 内置模块
    2. 当前目录
    3. 程序的主目录
    4. pythonpath目录(如果已经设置了pythonpath环境变量) 
    5. 标准链接库目录
    6. 第三方库目录(site-packages目录)
    7. .pth 文件的内容(如果存在的话)

        在工程目录建立这样一个文件，一行代表一个目录

    8. sys.path.append()临时添加的目录
### 安装第三方库

pip install 模块名称

## Python的文件操作

### 文本文件和二进制文件
- 文本文件

    文本文件存储的是普通**“字符”**文本，python默认为unicode字符集(两个字节表示一个字符，最多可以表示:65536个)

- 二进制文件

    二进制文件把数据内容用**“字节”**进行存储
### 文件操作相关模块概述
Python标准库中提供了如下常用文件操作的库：
|名称|说明|
|-----|-----|
io 模块|文件流的输入和输出操作 input output
os 模块|基本操作系统功能，包括文件操作
glob 模块|查找符合特定规则的文件路径名
fnmatch 模块|使用模式来匹配文件路径名
fileinput 模块|处理多个输入文件
filecmp 模块|用于文件的比较
cvs 模块|用于 csv 文件处理
pickle 和 cPickle|用于序列化和反序列化
xml 包|用于 XML 数据处理
bz2、gzip、zipfile、zlib、tarfile|用于处理压缩和解压缩文件(分别对应不同的算法)
### 常用文件操作函数

- open()
  
    ```python
    open(文件名[,打开方式,[encoding="字符编码"]])
    ```

    打开方式有如下几种:
    |模式 |描述|
    |-----|-----|
    r|读 read 模式
    w|f = open(r"filepath","w")。写 write模式。如果文件不存在则创建;如果文件存在，则重写新内容;
    a|追加 append 模式。如果文件不存在则创建;如果文件存在，则在文件末尾追加内容
    b|二进制 binary 模式(可与其他模式组合使用)
    + |  读、写模式(可与其他模式组合使用)


- close()
  
  打开的文件对象必须显式调用 close()方法 关闭文件对象。当调用 close()方法时，首先会把缓冲区数据写入文件(也可以直接调用 flush() 方法)，再关闭文件，释放文件对象。为了确保打开的文件对象正常关闭，一般结合异常机制的finally或者with关键字实现无论何种情况都能关闭打开的文件对象。

- write(txt)

    把字符串txt写入到文件中
- writelines(txtList):
    
    把字符串列表写入文件中，不添加换行符
- with

    with关键字(上下文管理器)可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，并且可以在代码块执行完毕后自动还原进入该代码块时的现场。
- read(size)

    从文件中读取 size 个字符，并作为结果返回。如果没有 size 参数，则读取整个文件。读取到文件末尾，会返回空字符串。

- readline()
  
  读取一行内容作为结果返回。读取到文件末尾，会返回空字符串。

- readlines()

- 文件读写操作练习：[测试代码](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/lx006.py)

### os和os.path模块
os模块可以帮助我们直接对操作系统进行操作。我们可以直接调用操作系统的可执行文件、命令，直接操作文件、目录等等

- os.system

    os.system 可以帮助我们直接调用系统的命令
    ```python
    import os
    os.system("ping www.google.com")
    ```
- os.startfile

    直接运行可执行文件

## 异常和错误处理
python中，引进了很多用来描述和处理异常的类，称为异常类。异常类定义中包含了该类异常的信息和对异常进行处理的方法。
![错误类型](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/doc/error.jpeg)

### 如何定位异常
当发生异常时，Python解释器会报相关的错误信息，并会在控制台打印出相关错误信息。只需按照**从上到下**的顺序即可追溯(Trackback)错误发生的过程，最终定位引起错误的那一行代码。

### 异常处理语句
- try...except
  
    ```python
    try:
        a = 1/0
    except ZeroDivisionError:
        print("不能除零")
    except BaseException as e: # 允许多个错误捕获，更好的控制你的程序
        print(e)
    ```
- else
  
  ```python
    try:
        a = 1/1
    except ZeroDivisionError:
        print("不能除零")
    except BaseException as e: # 允许多个错误捕获，更好的控制你的程序
    else:
        print(a) # try里面的没有错误时执行
    finally:
        print("无论如何都要执行")# 通常用于释放系统资源
- finally
  
### return语句和异常处理问题
在try....except语句中最好不要用return语句，将它放在try之外。

### 常见异常汇总
|异常名称 | 说明|
|-----|-----|
ArithmeticError|所有数值计算错误的基类
AssertionError|断言语句失败
AttributeError|对象没有这个属性
BaseException|所有异常的基类
DeprecationWarning|关于被弃用的特征的警告
EnvironmentError|操作系统错误的基类
EOFError|没有内建输入,到达 EOF 标记
Exception|常规错误的基类
FloatingPointError|浮点计算错误
FutureWarning|关于构造将来语义会有改变的警告
GeneratorExit|生成器(generator)发生异常来通知退出
ImportError|导入模块/对象失败
IndentationError|缩进错误
IndexError|序列中没有此索引(index)
IOError|输入/输出操作失败
KeyboardInterrupt|用户中断执行(通常是输入^C)
KeyError|映射中没有这个键
LookupError|无效数据查询的基类
MemoryError|内存溢出错误(对于 Python 解释器不是致命的)
NameError|未声明/初始化对象 (没有属性)
NotImplementedError|尚未实现的方法
OSError|操作系统错误
OverflowError|数值运算超出最大限制
OverflowWarning|旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning|关于特性将会被废弃的警告
ReferenceError|弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError|一般的运行时错误
RuntimeWarning|可疑的运行时行为(runtime behavior)的警告
StandardError|所有的内建标准异常的基类
StopIteration|迭代器没有更多的值
SyntaxError|Python 语法错误
SyntaxWarning|可疑的语法的警告
SystemError|一般的解释器系统错误
SystemExit|解释器请求退出
TabError|Tab 和空格混用
TypeError|对类型无效的操作
UnboundLocalError|访问未初始化的本地变量
UnicodeDecodeError|Unicode 解码时的错误
UnicodeEncodeError|Unicode 编码时错误
UnicodeError|Unicode 相关的错误
UnicodeTranslateError|Unicode 转换时错误
UserWarning|用户代码生成的警告
ValueError|传入无效的参数
Warning|警告的基类
WindowsError|系统调用失败
ZeroDivisionError|除(或取模)零 (所有数据类型)

### 自定义异常类
程序开发中，有时候我们也需要自己定义异常类。自定义异常类一般都是运行时异常，通常继承Exception或其子类即可。命名一般以 Error、Exception为后缀。

- 自定义异常由 raise 语句主动抛出
- 练习自定异常[源码](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/lx007.py)

## 小结
到目前为止，Python语言的真实基础算是告一个段落。离登堂入室还有半步飞仙的距离了。接下来做的就是实战+实战+实战，将所学的知识融会贯通。之后还有关于Python高阶的学习，比如并发，异步程序，网络编程等等。


## GUI实战
话说Python搞后台服务的较多，但是跨平台的GUI开发其实也不弱，通过几个GUI的练习，巩固一下前面所学的知识。

### 常用的GUI库

- Tkinter

    tkinter(Tk interface)是Python的标准GUI库，支持跨
    平台的GUI程序开发。

- PyQT
  
    PyQt是一个创建GUI应用程序的工具包。它是Python编程语言和Qt库的成功融合。Qt库是目前最强大的库之一。[在线指南](http://code.py40.com/face)

- wxPython

    wxPython是Python语言的一套优秀的GUI图形库，允许Python程序员很方便的创建完整的、功能健全的GUI用户界面。 wxPython是作为优秀的跨平台GUI库wxWidgets的Python封装和Python模块的方式提供给用户的。
    
    就如同Python和wxWidgets一样，wxPython也是一款开源软件，并且具有非常优秀的跨平台能力，能够支持运行在32 [1]  /64位windows、绝大多数的Unix或类Unix系统、Macintosh OS X下。

