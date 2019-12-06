# 第四天 函数和面向对象

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

    别个整理的一个常用三方库思维导图:![](https://cdn.jsdelivr.net/gh/coojee2012/LearnPython/doc/public_lib.jpeg)

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
- 未完待续

### 变量和变量的作用域

