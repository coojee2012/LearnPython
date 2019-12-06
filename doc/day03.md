# 第三天 语法基础：元祖、字典、集合、控制语句（2）

今天继续学习Python的一些基础数据结构和控制语句的语法。

学习项目及练习源码地址：[GitHub源码](https://github.com/coojee2012/LearnPython)

## 元祖tuple

元组属于不可变序列，不能修改元组中的 元素。因此，元组没有增加元素、修改元素、删除元素相关的方法。

- 元祖的创建和删除
  
  1. 通过()新建一个元祖
   
        a = (1,2,3) 或者 a = 1,2,3。如果元组只有一个元素，则必须后面加逗号。

  2. 通过内置tuple()函数创建一个新的元祖
   
        tuple()可以接收列表、字符串、其他序列类型、迭代器等生成元组。

  3. 生成器推导式创建元组

        生成器推导式与列表推导式类似，生成器推导式使用小括号。**列表推导式直接生成列表对象，生成器推导式生成的不是列表也不是元组，而是一个生成器对象。**

        **生成器对象，转化成列表或者元组。也可以使用它的__next__()方法进行遍历，或者直接作为迭代器对象来使用。使用后生成器对象元素立即清空。**

        语法：x = (i *2 for i in range(1,5))

  4. 通过del删除一个元祖
   
        ```python
        a = (1,2,3)
        type(a) # <class 'tuple'>

        b = 10,20,30
        print(b) # (10, 20, 30)

        c = (100,)
        print(c) # (100,)

        d = tuple() # 空元祖
        e = tuple('abc') # 传入字符串生成新的元祖 ('a','b','c')
        f = tuple([1,2,3]) # 列表转换为元祖 (1,2,3)
        g = tuple(range(5)) # 传入迭代器 (1,2,3,4,5)

        x = (i *2 for i in range(1,5)) # 生成器对象 <generator object <genexpr> at 0x108a39c50>
        tuple(x) # (2, 4, 6, 8)
        tuple(x) # () 已经使用了，没了
        ```
- 元祖的操作
  
  1. 元祖也是通过索引进行访问里面的元素

        注意：元祖的数据是不能修改的，只能访问

  2. 元祖也可以像列表一样进行切片访问，进行计数等

        切片后返回的是新的元祖对象

  3. 元祖对象没有sorted()方法，只能通过内置函数sorted(obj)返回一个列表
  4. zip(列表 1，列表 2，...)将多个列表对应位置的元素组合成为元组，并返回这个 zip 对象。

        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 *号操作符，可以将元组解压为列表。
   
        ```python
        a = (1,2,3)
        b = tuple('abc')

        a[0] # 1
        c = a[::-1]
        print(a) # (1, 2, 3)
        print(c) # (3, 2, 1)

        d = a + b
        print(d) # (1, 2, 3, 'a', 'b', 'c')

        d.index('a') # 3

        f = a + a
        f.count(1) # 2

        2 in f # True
        'a' in f # False

        for item in f:
            print(item) #循环打印

        max(a) # 3 只能是全是数值的元祖

        g = sorted(a) # [1, 2, 3] 返回列表
        h = sorted(a,reverse=True) # [3, 2, 1] 降序

        a.reverse() # 错误！！'tuple' object has no attribute 'reverse'
        i = reversed(a) # 返回一个迭代器 <reversed object at 0x108a79ad0>
        list(i) # [3, 2, 1]

        a1 = [1,2,3] # [1, 2, 3]
        a2 = list('abc') # ['a', 'b', 'c']
        a3 = list(range(5)) # [0, 1, 2, 3, 4]

        z = zip(a1,a2,a3) # 生成一个zip对象 <zip object at 0x108a7aa50>
        list(z) # [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2)]

        x = zip(a1,a2,a3) # 迭代器只能使用一次 ！！！！！重点
        z1,z2,z3 = zip(*x) # 不能用z,已经使用过了
        # 注意下面的输出z3
        print(z1) # (1, 2, 3)
        print(z2) # ('a', 'b', 'c')
        print(z3) # (0, 1, 2) 比之前a3的元素少了
        ```
## 字典
Python的字典对象有点像JavaScript的“对象”也是由“键值对”组成的，它是一个**无序可变序列**。字典中的每个元素都是一个“键值对”，包含:“键”和“值”。可以通过“键”实现获取、删除、更新对应的“值对象”。

字典中通过“键”获取对应的“值”。“键”是任意**不可变数据**，如:整数、浮点数、字符串、元组，且“键”不可重复。“值”可以是任意的数据。

看起来是这样的:a = {'key1':'value1','key2':2,3:[1,2,3]}

- 字典的创建

  1. 可以通过{}、dict()来创建字典对象。
  2. 通过 zip()创建字典对象
  3. 通过 fromkeys 创建值为空的字典
   
    ```python
    a = {} # 空字典
    a = {"k1":"v1","k2":2,3:"abcd"} # {'k1': 'v1', 'k2': 2, 3: 'abcd'}

    b = dict() #空字典
    b = dict(k1="vb1",k2=20,3="edf") # 错误:keyword can't be an expression,这里3不是一个有效的变量名
    b = dict(k1="vb1",k2=20,_3="edf") # {'k1': 'vb1', 'k2': 20, '_3': 'edf'}
    b = dict([("k1","v1"),("k2",3),(3,"abcd")])
    # {'k1': 'v1', 'k2': 3, 3: 'abcd'} 通过由特殊形式组成的元祖创建一个字典

    k = ['k1','k2',3,(1,2)]
    v = [1,'abc',(3,4,5),['a','b',2]]
    c = dict(zip(k,v)) # {'k1': 1, 'k2': 'abc', 3: (3, 4, 5), (1, 2): ['a', 'b', 2]} 通过zip创建 需要两个个数相等的列表或元祖或**可迭代对象--我猜的，以后需要验证

    d = dict.fromkeys(k) #{'k1': None, 'k2': None, 3: None, (1, 2): None}
    ```
- 字典的访问
  
  1. 通过["键"]访问，如果不存在会引发异常
  2. 通过字典对象的get()方法获取，如果不存这个键，返回None或自定义值
  3. 通过字典对象的items()获取所有的键值对列表迭代器
  4. 通过字典对象的keys()获取所有的键列表迭代器
  5. 通过字典对象的values()获取所有的值列表迭代器
  6. len()函数获取字典元素个数
  7. "key" in 检查字典键是否存在
   
    ```python
    a = {"key1":"v1","key2":"v2",1:1}
    a["key1"] # v1
    a["key3"] # KeyError: 'key3'
    a.get("key3") # None
    a.get("key3","键不存在") # '键不存在'
    a.items() # dict_items([('key1', 'v1'), ('key2', 'v2'), (1, 1)])
    a.keys() # dict_keys(['key1', 'key2', 1])
    a.values() # dict_values(['v1', 'v2', 1])
    "key1" in a # True
    ```
- 字典元素添加、修改、删除
  
  1. 字典["键"] = 值,如果不存在则新增，存在就更新值
  2. update():将新字典的键值覆盖或添加到旧字典
  3. 使用del(a[key])删除某个键及其值
  4. clear()删除所有键值对
  5. pop(key)删除指定键的键值对，并返回对应的“值对象”;
  6. popitem()随机删除和返回该键值对,记住**字典是无序的序列**
   
        ```python
        k = ["k1","k2","k3"]
        v = [1,2,3]
        d = dict(zip(k,v))
        d["k1"] # 1
        d["k1"] = "a"
        d["k1"] # a
        d["k4"] = 4
        d["k4"] # 4

        d.update({"k4":"v4","k5":5})
        print(d) # {'k1': 'a', 'k2': 2, 'k3': 3, 'k4': 'v4', 'k5': 5}

        del(d["k5"])
        e = d.pop("k4")
        print(e) # v4
        print(d) # {'k1': 'a', 'k2': 2, 'k3': 3}

        f = d.popitem() # ('k3', 3)
        g = d.popitem() # ('k2', 2)
        print(d) # {'k1': 'a'}

        d.clear()
        print(d) # {}
        del(d["1"]) # KeyError: '1'
        d.pop(1) # KeyError: '1'
        d.popitem() # KeyError: 'popitem(): dictionary is empty'
        ```
- **字典的核心原理**
    
    字典对象的核心是散列表。散列表是一个稀疏数组(总是有空白元素的数组)，数组的每个单元叫做bucket。每个bucket有两部分:一个是键对象的引用，一个是值对象的引用。

- **字典的特性**
  
    1. 键必须可散列
    2. 内存中开销巨大，典型的空间换时间
    3. 键查询速度很快
    4. 往字典里面添加新建可能导致扩容，导致散列表中键的次序变化。因此，不要在遍历字 典的同时进行字典的修改。


- 练习用Python代码打印如下表格,尽量用到字典和列表
  
  |班级|姓名|年龄|成绩|
  |----|----|----|----|
  |1班|张三|10|88|
  |2班|李四|9|67|
  |1班|赵钱|11|30|
  |3班|王小丫|12|99|
  |2班|李宝强|9|98|
  |1班|马云峰|11|100|

## 集合

集合是无序可变，元素不能重复。实际上，在Python中集合底层是由字典实现的。集合的所有元素都是字典中的“键”对象，因此是唯一的。

- 创建集合

    1. {}和创建字典一样的符号
    2. 内置函数set()，将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保留一个。

        ```python
        a = {1,2,3}
        type(a) # <class 'set'>
        print(a) # {1, 2, 3}

        b = set([1,2,1,3,2,4]) #{1, 2, 3, 4}
        b = set((1,1,1,1,2,2,2,3,)) # {1, 2, 3}
        b = set({"k1":1,"k2":2,3:'a'}) #{3, 'k1', 'k2'}
        ```
- 集合常用操作
  
    1. 集合对象的add()方法添加元素,添加一个重复元素无效
    2. 集合对象的remove()方法删除元素
    3. 集合对象的clear()清空整个集合
    4. 并集：| 或 对象的union()
    5. 交集：& 或 对象的intersection()
    6. 差集：- 或 对象的difference()
   
    ```python
    a = {} # <class 'dict'> 这样创建的是字典不是集合
    a = {1,2,3}
    a.add('a') # {1, 2, 3, 'a'}
    a.add(1) # {1, 2, 3, 'a'} 重复添加
    a.remove() # TypeError: remove() takes exactly one argument (0 given) 需要制定一个元素
    a.remove("v") # KeyError: 'v' 会引发一个异常
    a.remove('a') # {1, 2, 3}

    b = {1,2,4}

    c = a | b # {1, 2, 3, 4}
    c = a.union(b)
    c = a & b # {1, 2}
    c = a.intersection(b)
    c = a - b # {3}
    c = a.difference()

    ```

### 小结

到这里，Python基本的数据结构就学习完毕了。列表、字典、元祖和集合是比较基础且很常见的数据结构，在以后的学习和工作会经常遇到，需要熟练掌握这几个数据结构。对比了解过的其他开发语言，Python与他们有相同也有不同的地方，Python内置了这些数据结构相对于其他开发语言要使用起来感觉要方便许多，至少不用像Java那样需要引入ArrayList这样的包，也不用像JavaScript那样需要在ES6中才会有Set(集合)这样的数据结构。

## 控制语句

- 选择结构
  
    1. 单分支结构
        ```python
        if 条件表达式:
            语句1
            语句2
            语句3
        ```
        条件表达式：可以是逻辑表达式、关系表达式、算术表达式等等。 
        语句可以一条或多条，如果什么都不错输入pass，这个不应该出现在实际工作中。

        再强调一次：**语句需要缩进**，多条语句需要对齐

    2. 双分支结构

        ```python
        if 条件表达式 :
            语句1
            语句2 
        else:
            语句3
            语句3
        ```
    3. 多分支结构
   
         ```python
        if 条件表达式1 :
            语句1
            语句2 
        elif 条件表达式2 :
            语句1
            语句2 
        [elif 条件表达式3 :
            语句1
            语句2 
        ....]
        [else:
            语句3
            语句3]
        ```

        []内容是可选的

    4. 三元运算符
   
        真值 if (条件表达式) else 假值

        **注意：很多语言使用 条件表达式 ？ 真值 : 假值**  Python不是这样的哦
    5. 选择结构嵌套
   
        选择结构可以嵌套，**使用时一定要注意控制好不同级别代码块的缩进量**，因为缩进量决定了代码的从属关系。

        ```python
        if 条件表达式:
            语句1
            if 条件表达式:
                语句
                语句
                语句
                ...
            else:
                pass
        else:
            语句
            语句
            ...
        ```

    6. 条件判断详细

        在选择和循环结构中，条件表达式的值为 False 的情况如下:
False、0、0.0、空值None、空序列对象(空列表、空元祖、空集合、空字典、空字
符串)、空range对象空迭代对象。其余情况为 True。

        不能在条件表达式中有赋值操作符号”=“。

- 循环结构
  
  1. while循环
   
    ```python
    while 条件表达式:
        循环体语句
    ```
  2. for循环遍历可迭代对象
    ```python
    for 变量 in 可迭代对象:
        循环体语句
    ```
  3. 可迭代对象
   
   
        Python 包含以下几种可迭代对象: 
        
        1. 序列，包含:字符串、列表、元组、字典
        2. 迭代器对象(iterator)
        3. 生成器函数(generator)
        4. 文件对象
   
  4. range对象

        range对象是一个迭代器对象，用来产生指定范围的数字序列。格式为: range(start, end [,step])。生成的数值序列从start开始到end结束(不包含end)。默认从0开始。step是可选的步长，默认为 1。

  5. break语句
   
        break语句可用于while和for循环，用来结束整个循环。当有嵌套循环时，break语句只能跳出**最近一层的循环**。
        
  6. continue语句
   
        continue语句用于结束本次循环，继续下一次。多个循环嵌套时，continue也是应用于**最近的一层循环**。
  7. else语句

        while、for循环可以附带一个else语句(可选)。如果for、while语句没有被**break语句结束**，则会执行else子句，否则不执行。语法格式如下:
        ```python
        while 条件表达式: 
            循环体
        else: 
            语句块

        #或者:
        for 变量 in 可迭代对象:
            循环体 
        else:
            语句块
        ```


## 推导式

- 列表推导式
    
    列表推导式生成列表对象，语法如下:
    
    [表达式 for item in 可迭代对象 ]

    或者:

    {表达式 for item in 可迭代对象 if 条件判断}

- 字典推导式

    字典的推导式生成字典对象，格式如下:
    
    {key_expression :value_expression for 表达式 in 可迭代对象}
    
    类似于列表推导式，字典推导也可以增加if条件判断、多个for循环。

- 集合推导式

    集合推导式生成集合，和列表推导式的语法格式类似:

    {表达式 for item in 可迭代对象 }

    或者:
    
    {表达式 for item in 可迭代对象 if 条件判断}

- 生成器推导式(生成元组)
  
    **元组是推导式生成的是生成器**生成器也可以用于for in循环。生成器对象一次使用后就没有元素了。

    ```python
    a = [x for x in range(0,10)]
    print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    b = {x:x for x in range(0,3)}
    print(b) # {0: 0, 1: 1, 2: 2, 3: 3}

    c = {x for x in range(0,3)}
    print(c) # {0, 1, 2}

    d = ((x,y) for x in range(0,3) for y in range(4,7) )
    print(d) # <generator object <genexpr> at 0x108a39dd0> 生成器
    for d1 in d:
        print(d1,end=' ') 
    # (0, 4) (0, 5) (0, 6) (1, 4) (1, 5) (1, 6) (2, 4) (2, 5) (2, 6)
    # 理解下这个输出结果为什么是这样呢?是不是循环嵌套啊哈哈

    ```


### 练习

练习答案前往[GitHub源码](https://github.com/coojee2012/LearnPython)查询。

- 用for循环计算1-100的和，偶数和，奇数和 [练习](./../src/lx001.py)
- 循环嵌套打印九九乘法表[练习](./../src/lx002.py)

### 小结

这些结构和其他语言差不多，主要是要注意缩进控制代码块。记住三元操作符合大多数语言不一样，注意冒号”:“，注意条件表达式的值，循环控制需要掌握生成器和迭代器对象的灵活运用。还有循环控制else语句这个很特别，需要掌握说不定有奇效。一定要掌握和理解推导式。

明天学习函数和面向对象编程。加油！！！！