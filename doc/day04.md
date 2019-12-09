# 第四天 函数和面向对象

学习项目及练习源码地址：[GitHub源码](https://github.com/coojee2012/LearnPython)

## 函数

Python中的函数必须先定义才能调用。
### Python中函数的分类
- 内置函数
  
    内置函数对象在解释器运行时会自动创建。前面用到的len(),sorted()等都是内置函数。

- 标准库函数

    标准函数在import模块时，解释器会执行模块中的def语句。

    别个整理的一个标准库思维导图：![标准库](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/doc/stand_lib.jpeg)

- 第三方库函数

    第三方库函数对象创建和标准库一致，在import模块时创建。

    别个整理的一个常用三方库思维导图:![三方库](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/doc/public_lib.jpeg)

- 自定义函数
  
### 用def关键字创建一个函数
在Python中函数也是一个对象！Python中，定义函数的语法如下: 
```python
def 函数名([参数列表]): # 无形参函数须保留()
    '''函数说明文档''' # 函数说明性注释是一个好习惯， help(函数名.__doc__)可以打印输出函数的文档说明
    函数体
    [return]
    # 如果函数体中包含return语句，则结束函数执行并返回值; 
    # 缺省返回None
    # 使用列表、元组、字典、集合等返回多个值

```
不需要指定函数返回类型。

```python
def printStars(n):
    '''
    打印小星星
    '''
    print('*' * n)
print(id(printStars)) # 4564978720 函数也是一个对象
print(type(printStars)) # <class 'function'>

print(printStars) # <function printStars at 0x110180c20>
help(printStars.__doc__) #查看函数文档

printStars(5)  # *****
printStars(10) # **********

c = printStars # 一切都是对象。通常情况下不需要这样做，举例说明不要忘记()，否则就是赋值操作了。
print(id(c))   # 4564978720 
c(5)  # *****
c(10) # **********
```

### 函数的参数

- 形参和实参原则上应该个数一致
    
    定义函数时，多个形参用,号分开，不需要指定参数类型。

- 一切对象都可以作为参数传递
  
    序列：字典，列表...函数，类等等都可以作为参数传递。

- Python中参数的传递都是“引用传递”

    1. 传递一个可变对象
   
        字典、列表、集合、自定义的对象等。

        在函数内部所有对该类型变量的操作，都会修改外部实参对象的结果。

    2. 传递一个不可变对象

        数字、字符串、元组、布尔值、function等

        在函数内部对该类型变量进行“赋值操作”时，由于不可变对象无法修改，系统会新创建一个对象并引用到该变量。**在赋值操作之前，该变量依然是原对象的引用。**
        ```python
        a = [1,2,3] # 可变
        b = 100 # 不可变
        
        def test(m,n):
            print(id(m)) # 4414439168 和 a地址一样
            print(id(n)) # 4393233264 和 b地址一样

            m.append(4)
            n += 1

            print(id(m)) # 4414439168 没有变化
            print(id(n)) # 4393233296 新的对象
            print(m) # [1, 2, 3, 4]
            print(n) # 101

        print(id(a)) # 4414439168
        print(id(b)) # 4393233264
        test(a,b)
        print(a) # [1, 2, 3, 4] 变化了
        print(b) # 没有变
        ```
    3. 传递不可变对象时发生拷贝属于浅拷贝
   
        - 浅拷贝
            
            不拷贝子对象的内容，只是拷贝子对象的引用
        - 深拷贝

            会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象
        
        传递不可变对象包含的子对象是可变对象
        **方法内修改了这个可变对象，源对象也发生了变化。**

        掌握浅拷贝和深拷贝的要点。在进行参数传递时，根据需要考虑传递什么方式的拷贝参数。
    
- 参数定义的几种类型
  
    1. 位置参数

        函数调用时，实参默认按位置顺序传递，需要个数和形参匹配。按位置传递的参数，称为: “位置参数”。

        传递个数不匹配时将引发异常。

    2. 带有默认值的参数

        定义函数时，可以为某些参数设置默认值，这样这些参数在传递时就是可选的。称为“默认值参数”。 **默认值参数放到位置参数后面。**
    3. 参数命名传递
   
        在函数调用时，可以按照形参的名称传递参数，称为“命名参数”，也称“关键字参数”。这样可以不用按照函数定义时参数的位置进行函数调用。

    4. 可变参数
   
        在函数定义时，可以定义可变参数。
        
        1. \*param(一个星号)，将多个参数收集到一个**“元组”**对象中。
   
        2.  \*\*param(两个星号)，将多个参数收集到一个**“字典”**对象中。
   
        **可变参数一般定义在形参的最后一个位置。**

    5. 强制命名参数
   
        如果定义函数时，非要在“可变参数”后面增加新的参数，**必须在调用的时候强制使用“命名参数”方式进行函数调用**，否则会引发异常。

### 变量和变量的作用域

变量起作用的范围称为变量的作用域，不同作用域内同名变量之间互不影响。在Python中变量分为:全局变量、局部变量。

- 全局变量

    1. 定义在模块中，函数和类之外的变量就是全局变量。作用域为定义的模块，从定义位置开始直到模块结束。
    2. 应尽量避免全局变量的使用。影响通用性和阅读性。
    3. 一般将常量定义成全局变量。
    4. 函数内要改变全局变量的值，使用global声明一下。
   
- 局部变量
    
    1. 定义在函数内部的变量，包括形参
    2. 类里面还有类变量
    3. 局部变量的引用速度比全局变量快
    4. 局部变量和全局变量同名，函数体内优先使用
    5. 函数在执行时解释器会创建栈桢（stack frame),局部变量名存放在栈桢中（对象依然放在堆中），函数执行完毕时，栈桢回收。
    6. locals()查看局部变量
    7. globals()查看全局变量
   
- **效率建议**
    
    1. 模块中import的函数或类属于全局变量
    2. 复杂的循环运算时，将全局变量转换成局部变量进行运算
    
    ```python
    import math
    def test():
        b = math.sqrt # 转成局部变量
        for x in range(10000000):
            b(300)
    ```

- lambda表达式和匿名函数

    lambda表达式可以用来声明匿名函数。lambda函数是一种简单的、在同一行中定义函数 的方法。lambda函数实际生成了一个函数对象。lambda表达式只允许包含一个表达式，不能包含复杂语句，该表达式的计算结果就是函数的返回值。

    lambda 表达式的基本语法如下:

    lambda arg1,arg2,arg3... : <表达式>

    arg1/arg2/arg3 为函数的参数。<表达式>相当于函数体。运算结果是:表达式的运算结果。

    ```python
    fn = lambda x,y,z:(x+y)*z
    print(type(fn)) # <class 'function'>
    fn(1,2,3) # 9

    a = (lambda z:z**3,lambda z:z+z,lambda z,n:z*n) #将lambda表达式作为元祖的元素
    b = (a[0](3),a[1](4),a[2]('*',10))
    print(b) # (27, 8, '**********')
    ```
- eval()函数
  
    不想看这个，一般都不建议使用

- 递归函数

    在Python中，递归函数会创建大量的函数对象，导致过量的消耗内存和运算能力。在处理大量数据时，谨慎使用。[阶乘练习源码](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/lx003.py)

- 嵌套函数

    顾名思义，在函数内部定义的函数的方式叫嵌套函数。

    1. 封装 - 数据隐藏
   
        外部无法访问“嵌套函数”。

    2. DRY原则
   
        嵌套函数，可以让我们在函数内部避免重复代码。 

    3. 闭包
   
        
    使用关键字nonlocal在嵌套函数中使用外层函数的变量，和global一样的原理。

    **LEGB规则：Local-->Enclosed-->Global-->Built in**

    如果某个变量名映射在局部(local)命名空间中没有找到，接下来就会在闭包作用域(enclosed)进行搜索，如果闭包作用域也没有找到，Python就会到全局(global)命名空间中进行查找，最后会在内建(built-in)命名空间搜索(如果一个名称在所有命名空间中都没有找到，就会产生一个NameError)。

### 小结

在Python中函数的定义和大部分变成语言道理是一样的，注意函数返回值问题，这个和Java、C++等不太一样。参数的定义和传递也有差异。命名参数调用函数比较特别，也非常有用。掌握可变参数的出传递和使用。

- 练习

    输入三角形三个顶点的坐标，若有效则计算三角形的面积;如坐标无效，则给出提示。
    
    [练习源码](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/src/lx004.py)遇到很多坑，填了，可以自己先写写再看。

## Python中面向对象编程

不解释什么是面向对象或面向对象编程，以及不解释什么是面向过程或面向过程编程。请君在google百度一下相关概念。

### 类的定义

**记住：Python中“一切皆对象”。类也称为“类对象”，类的实例也称为“实例对象”。**

定义类的语法格式如下: 

```python
class 类名: # 建议首字母大写的驼峰命名规则，如：ArrayList
    类体
```

类是抽象的，也称之为“对象的模板”。需要通过类这个模板，创建类的实例对象，然后才能使用类定义的功能。当解释器执行class语句时，就会创建一个类对象。

- \_\_init__()类的构造函数

    构造方法用于执行“实例对象的初始化工作”，即对象创建后，初始化当前对象的相关属性，无返回值。

    1. 在Python中构造函数名称是固定的必须是__init__()
    2. 第一个参数必须是self,指向对象本身，参数名预定成俗就是self.
    3. 构造函数通常用来初始化实例对象的实例属性
    4. 不定义__init__方法，系统会提供一个默认的__init__方法。如果我们定义了带参的__init__方法，系统不创建默认的__init__方法。
   
- \_\_new__()用于创建对象，一般不需要重定义
- 类的调用方法
  
    myObj = ClassName([构造参数])

### 类的实例属性和实例方法

- 实例属性
  
  实例属性是从属于**实例对象**的属性，也称为“实例变量”。他的使用有如下几个要点: 
  1. 实例属性一般在__init__()方法中通过如下代码定义:

        ```python
        self.实例属性名 = 初始值
        ```

        不能写return,默认返回的是实例化好的对象。

  2. 在类的其他实例方法中，通过self进行访问:

        ```python
        self.实例属性名
        ```
  3. 创建实例对象后，通过实例对象访问:

        ```python
        obj01 = 类名() #创建对象，调用__init__()初始化属性 
        
        obj01.实例属性名 = 值 #可以给已有属性赋值，也可以新加属性
        ```
- 实例方法

    实例方法是从属于**实例对象**的方法。实例方法的定义格式如下:
    ```python
     def 方法名(self [, 形参列表]):
            函数体
     #方法的调用格式如下:
     对象.方法名([实参列表])
    ```
    1. 定义实例方法时，第一个参数必须为self。self指当前的实例对象。 
    2. 调用实例方法时，不需要也不能给self传参。self由解释器自动传参。

- dir(obj)可以获得对象的所有属性、方法
- obj.\_\_dict__ 对象的属性字典
- pass空语句
- isinstance(对象,类型)判断“对象”是不是“指定类型”

```python
class Test:
    def __init__(self,name,age): # self必须的
        self.name = name
        self.age = age
    def getMyName(self): # self必须的
        return self.name
    def getMyAge(self):
        return self.age

testObj = Test("张三",18) # 调用类，实例化一个”实例对象“

print(id(Test)) # 140614954454304
print(Test) # <class '__main__.Test'>
print(type(Test))  # <class 'type'>
print(id(testObj)) # 4340153616
print(type(testObj)) # <class '__main__.Test'>

print(testObj.getMyName())
print(testObj.getMyAge())
print(Test.getMyName(testObj)) # 解释器是这个干的，方法是共享的
print(dir(Test))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getMyAge', 'getMyName']
'''
print(dir(testObj))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'getMyAge', 'getMyName', 'name']
'''
# 多了name 和  age

print(Test.__dir__) # <method '__dir__' of 'object' objects> 注意类是objects的对象
print(testObj.__dir__) # <built-in method __dir__ of Test object at 0x109bf3e90>
print(isinstance(testObj,Test)) # True

```
    实例对象和类对象共享类方法。

### 类对象、类属性、类方法、静态方法

- 类对象

    解释器遇到class关键字时就创建了一个类对象。

- 类属性
  
    类属性是**从属于“类对象”**的属性，也称为“类变量”。由于，类属性从属于类对象，**可以被所有实例对象共享**。
    
    类属性的定义方式:
    
    ```python
    class 类名:
        类变量名 = 初始值 
    ```
    
    在类中或者类的外面，我们可以通过:“类名.类变量名”来读写。

- 类方法

    类方法是**从属于“类对象”的方法**。
    
    类方法通过装饰器@classmethod来定义，格式如下: 
    ```python
    @classmethod
    def 类方法名(cls [，形参列表]):
        函数体
    ```

    1. @classmethod必须位于方法上面一行
    2. 第一个参数：cls必须有;**cls指的就是“类对象”本身**;
    3. 调用类方法格式:“类名.类方法名(参数列表)”。**参数列表中，不需要也不能给cls传值。**
    4. **类方法中访问实例属性和实例方法会导致错误**
    5. 子类继承父类方法时，传入cls是子类对象，而非父类对象

- 静态方法

    “类对象”无关的方法，称为“静态方法”。“静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了**“类的名字空间里面”，需要通过“类调用”**。
    
    静态方法通过装饰器@staticmethod 来定义，格式如下:
    ```python
     @staticmethod
     def 静态方法名([形参列表]): 
         函数体
    ```

    要点如下:

    1. @staticmethod必须位于方法上面一行
    2. 调用静态方法格式:“类名.静态方法名(参数列表)” 
    3. **静态方法中访问实例属性和实例方法会导致错误**


### __del__方法(析构函数)和垃圾回收机制

__del__方法称为“析构方法”，用于实现对象被销毁时所需的操作。
Python实现自动的垃圾回收，当对象没有被引用时(引用计数为 0)，由垃圾回收器调用__del__方法。可以通过del语句删除对象，从而保证调用__del__方法。系统会自动提供__del__方法，一般不需要自定义析构方法。

### __call__方法和可调用对象

    定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用。

### 方法重载

    Python方法没有重载!!!

    类体中定义了多个重名的方法，只有最后一个方法有效。

    **可以根据参数的动态性或参数的可变性，实现一个方法的多种用途。**
### 方法的动态性

Python是动态语言，**可以动态的为类添加新的方法，或者动态的修改类的已有的方法。**

```python
class Test:
    def __init__(self,name):
        self.name = name
    def add(self,a,b):
        print("old method:{0} {1}".format(a+b,self.name))

def count(obj):
    print("count {}".format(obj.name))
def add(obj,a,b):
    print("new method:{0} {1}".format(a+b,obj.name))

test = Test('zhangsan')
test.add(1,2)

Test.count = count
test.count()

Test.add =add
test.add(11,22)
```
### 私有属性和私有方法

**Python对于类的成员没有严格的访问控制限制，**这与其他面向对象语言有区别。关于私有属性和私有方法，有如下要点:

  1. 通常约定，两个下划线开头的属性是私有的(private)。其他为公共的(public)。 
  2. 类内部可以访问私有属性(方法)
  3. 类外部不能直接访问私有属性(方法)
  4. 类外部可以通过“_类名__私有属性(方法)名”访问私有属性(方法)
   
方法本质上也是属性!只不过是可以通过()执行而已。所以，私有方法和私有属性是一样的。

```python
class Test:
    __address = '上海1弄1号'
    def __init__(self,name):
        self.name = name
        self.__age = 29
        self.__address = "上海100弄1号"
    def __mockAge(self):
        print("my age is {}".format(18))
    def getAge(self):
        self.__mockAge()
    def __realAge(self):
        print("my age is {}".format(self.__age)) 
    
test = Test("张三")
print(test._Test__age)
test.getAge()
test._Test__realAge()
print(Test._Test__address) # 和对象属性重复怎么办？注意调用者
```

### @property装饰器

@property可以将一个方法的调用方式变成“属性调用”。只能调用，但不能设置值。要修改值需要用 @salary.setter装饰一个同名方法，才能进行设置。

```python
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
```

### 小结

时间过得太快，今天的就学了这些东西。Python在面向对象编程方面很有创新，但是编程思维和大多数语言一致，只是在应用的时候要好好掌握这些基础的东西，才能用面向对象的思维干活。

下次将进一步学习Python面向对象编程的三大特征：继承，多态，设计模式等...
