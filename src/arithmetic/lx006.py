from utils import metric

class Node:
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    def __init__(self,root=None):
        self.root = root
    
    def add(self,elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop()
                if cur.lchild == None:
                    cur.lchild = node
                    break
                elif cur.rchild == None:
                    cur.rchild = node
                    break
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    
    @metric()
    def preorder(self,root):
        '''
        先序遍历
        '''
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)
    
    @metric()
    def inorder(self,root):
        '''
        中序遍历
        '''
        if root == None:
            return
        self.preorder(root.lchild)
        print(root.elem)
        self.preorder(root.rchild)

    @metric()
    def postorder(self,root):
        '''
        后序遍历
        '''
        if root == None:
            return
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        print(root.elem)

    @metric()
    def breadth_trval(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if(node.lchild != None):
                queue.append(node.lchild)
            if(node.rchild != None):
                queue.append(node.rchild)
if __name__ == '__main__':
    tree = Tree()
    for i in range(100):
        tree.add(i)
    tree.breadth_trval()
    tree.preorder(tree.root)
    tree.inorder(tree.root)
    tree.postorder(tree.root)

