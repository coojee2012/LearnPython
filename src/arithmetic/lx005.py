'''
练习实现双向链表
'''

class DNode(object):
    '''
    链表的一个节点
    '''
    def __init__(self,item):
        self.item =item # 值域
        self.prev = None # 前一个节点
        self.next = None # 下一个节点的地址

class DLinkList:
    def __init__(self):
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
        头部添加元素
        '''
        node = DNode(item)
        if self.is_empty():
            self.__head = None
        else:

            node.next = self.__head # 新元素的next节点指向原来的元素
            self.__head.prev = node # 头结点的prev指向自己
            self.__head = node
   
    def append(self,item):
        '''
        尾部添加
        '''
        node = DNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur  = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = DNode(item)
            count = 0
            cur = self.__head
            while count < (pos -1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def remove(self,item):
        cur = self.__head

        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None

                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    dlist = DLinkList() # 创建空链表
    print('是否为空:',dlist.is_empty())
    print('当前长度:',dlist.length())

    dlist.tavel()

    print(dlist.search(20))
    print(dlist.search(30))

    dlist.add(20)
    dlist.add(30)
    dlist.append(40)

    print('是否为空:',dlist.is_empty())
    print('当前长度:',dlist.length())

    dlist.tavel()

    print(dlist.search(20))
    print(dlist.search(30))

    dlist.remove(30)

    print('是否为空:',dlist.is_empty())
    print('当前长度:',dlist.length())

    dlist.tavel()

    print(dlist.search(20))
    print(dlist.search(30))

    dlist.insert(-1,100)
    dlist.insert(100,200)

    dlist.insert(2,300)

    print('是否为空:',dlist.is_empty())
    print('当前长度:',dlist.length())

    dlist.tavel()






    