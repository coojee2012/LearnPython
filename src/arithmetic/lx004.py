'''
练习实现单向链表
'''

class SingelNode(object):
    '''
    单向链表的一个节点
    '''
    def __init__(self,item):
        self.item =item # 值域
        self.next = None # 下一个节点的地址

class SingelList:
    def __init__(self,node=None):
        if node!=None:
            headNode = Node(node) #头节点
            self.__head = headNode
        else:
            self.__head = None
    def is_empty(self):
        return self.__head == None
    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count
    
    def tavel(self):
        '''
        遍历
        '''
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")
    def add(self,item):
        '''
        头部添加
        '''
        node = SingelNode(item)
        node.next = self.__head
        self.__head = node
   
    def append(self,item):
        '''
        尾部添加
        '''
        node = SingelNode(item)
        if self.is_empty():
            self.__head = node
        else:
            curNode = self.__head
            while curNode.next != None:
                curNode  = curNode.next
            curNode.next = node
    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingelNode(item)
            count = 0
            pre = self.__head
            while count < (pos -1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    singleList = SingelList() # 创建空链表
    print('是否为空:',singleList.is_empty())
    print('当前长度:',singleList.length())

    singleList.tavel()

    print(singleList.search(20))
    print(singleList.search(30))

    singleList.add(20)
    singleList.add(30)
    singleList.append(40)

    print('是否为空:',singleList.is_empty())
    print('当前长度:',singleList.length())

    singleList.tavel()

    print(singleList.search(20))
    print(singleList.search(30))

    singleList.remove(30)

    print('是否为空:',singleList.is_empty())
    print('当前长度:',singleList.length())

    singleList.tavel()

    print(singleList.search(20))
    print(singleList.search(30))

    singleList.insert(-1,100)
    singleList.insert(100,200)

    singleList.insert(2,300)

    print('是否为空:',singleList.is_empty())
    print('当前长度:',singleList.length())

    singleList.tavel()






    