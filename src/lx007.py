'''
练习自定义错误的定义和使用
'''
class MyError(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message = message
    def __str__(self):
        return "程序错误啦：{}".format(self.message)

if __name__ == '__main__':
    try:
        raise MyError("测试错误")
    except MyError as e:
        print("MyError:",e)
    except BaseException as e:
        print("Base Exception:",e)
