class Node:
    def __init__(self,item):
        self.elem=item #元素
        self.lchild=None #左孩子
        self.rchild=None #右孩子

class Tree:
    def __init__(self):
        self.root=None #根节点
    def add(self,item):
        node=Node(item)
        #判断根节点是否为空
        if self.root is None:
            self.root=node
            return
        queue=[self.root]  #用来存放节点的队列并将根节点添加到队列
        while queue:#列表不为空 就执行
            cur_node=queue.pop(0) #取出第一个元素
            if cur_node.lchild is None:
                cur_node.lchild=node #添加
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node #添加
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        #广度遍历
        if self.root is None:
            return  #如果根节点是空 直接返回
        queue = [self.root]
        while queue:
                cur_node=queue.pop(0)  #从头部弹出一个
                print(cur_node.elem)
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild) #添加队列
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)  #添加队列
    def preoder(self,node):
        # 先序遍历
        if  node is None:
            return
        print(node.elem,end=' ')    #打印根节点
        self.preoder(node.lchild)    #  递归调用 先序遍历左子树
        self.preoder(node.rchild)    #递归调用 先序遍历右子树
    def inoder(self,node):
        #中序遍历
        if node is None:
            return
        self.inoder(node.lchild) #  递归调用 中序遍历左子树
        print(node.elem,end=' ') #打印根节点
        self.inoder(node.rchild) #递归调用 中序遍历右子树

    def afteroder(self, node):
        # 后序遍历
        if node is None:
            return
        self.afteroder(node.lchild)  # 递归调用 后序遍历左子树
        self.afteroder(node.rchild)  # 递归调用 后序遍历右子树
        print(node.elem,end=' ')       #打印根节点
if __name__=='__main__':
    tree=Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    tree.preoder(tree.root)
    print('\n')
    tree.inoder(tree.root)
    print('\n')
    tree.afteroder(tree.root)