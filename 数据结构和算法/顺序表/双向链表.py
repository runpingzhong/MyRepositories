#定义节点类
class Node:
    def __init__(self,item):
        #节点
        self.elem=item
        self.pre=None
        self.next=None
class Double_link_list:
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        '判断链表是否为空'
        return self.__head==None
    def length(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count
    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print('')
    def add(self,item):
            node=Node(item)
            node.next=self.__head
            self.__head=node
            node.next.pre=node
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur
    def insert(self,pos,item):
        #param pos 从0开始
        node=Node(item)
        if pos<=0:#如果插入位置小于等于0  默认从头插入
            self.add(item)
        elif pos>=self.length():#如果插入位置大于等于链表长度 默认尾部追加
            self.append(item)
        else:
            cur=self.__head
            count=0
            while count<pos: #光标移动 找到需要添加元素的位置
                count+=1
                cur=cur.next
            #退出循环 改变链表节点的指向
            node.next=cur
            node.pre=cur.pre
            cur.pre.next=node
            cur.pre=node
    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False
    def remove(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                #先判断此节点是否是头节点
                #头节点
                if cur==self.__head:
                    self.__head=cur.next
                    if cur.next!=None:
                        #判断链表是否只有一个节点
                        cur.next.pre=None
                else:
                    cur.pre.next=cur.next
                    if cur.next:
                        cur.next.pre=cur.pre
                break
            else:
                cur=cur.next
if __name__=='__main__':
    dll=Double_link_list()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    dll.append(2)
    dll.travel()
    dll.append(10)
    dll.add(20)
    dll.travel()
    dll.remove(2)
    dll.travel()
    print(dll.search(1))
    dll.insert(1,100)
    dll.insert(1, 200)
    dll.travel()