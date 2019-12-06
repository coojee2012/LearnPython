import math
def area(x,y,z):
    '''
    根据三个点的坐标计算三角形的面积
    AB斜率：kAB=(y2-y1)/(x2-x1)
    BC斜率：kBC=(y3-y2)/(x3-x2)

    两点间的距离算法：
    (x1**2-y1**2) + (x2**2 - y2**2) 开根号求绝对值
    三角形面积计算用海伦-秦九韶公式
    已知三边是a,b,c
    令p=(a+b+c)/2
    [p(p-a)(p-b)(p-c)]开根号
    x,y,z 为表示三个坐标点的列表[x1,y1]
    '''
    def slope(k,j):
        ydiff = k[1] - j[1]
        xdiff = k[0] - j[0]
        if(xdiff == 0 or ydiff == 0):
            return 0
        return ydiff/xdiff

    # 首先判断三点是否在一条直线上
    kxy = slope(x,y)
    kyz = slope(y,z)
    if kxy == kyz:
        print("三个点在一条直线上")
        return
    # 定义一个边长计算的函数
    def length(m,n):
        result = (m[0] - n[0])**2 + (m[1] - n[1])**2
        result = math.sqrt(result)
        result = math.fabs(result)
        return result
    # 计算三个边的边长
    xy = length(x,y)
    yz = length(y,z)
    zx = length(z,x)
    p = (xy+yz+zx)/2
    s = math.sqrt(p*(p-xy)*(p-yz)*(p-zx))
    print("面积是:{0:.2f}".format(s))

print("坐标输入格式为:x,y")
a = input("请输入第一个点的坐标:")
b = input("请输入第二个点的坐标:")
c = input("请输入第三个点的坐标:")

a = a.split(',') #用,拆分点的坐标
b = b.split(',')
c = c.split(',')

a = [ int(x) for x in a ]
b = [ int(x) for x in b ]
c = [ int(x) for x in c ]

area(x=a,y=b,z=c)