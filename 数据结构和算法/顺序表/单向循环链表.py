#创建节点类
class Node:
    def __init__(self,item):
        self.elem=item
        self.next=None
class Single_cycle_link:
    def __init__(self,node=None):
        self.__head=node
        if node:
            node.next=node
    def is_empty(self):
        return self.__head==None
    def length(self):
        if self.is_empty():
            return 0
        else:
            cur=self.__head
            count=1
            while cur.next!=self.__head:
                count+=1
                cur=cur.next
            return count
    def travel(self):
        if self.is_empty():
            return
        cur=self.__head
        while cur.next!=self.__head:
            print(cur.elem,end='')
        #退出循环 cur指向尾节点  但是尾节点没有打印出来
        print(cur.elem)
        print('')
    def add(self,item):
        node=Node(item)
        #判断是否是空链表
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            node.next=self.__head
            self.__head=node
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            #退出循环 找到尾节点
            node.next=self.__head
            self.__head=node
            cur.next=self.__head
    def append(self,item):
        node=Node(item)
        #判断是否是空链表
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            node.next=self.__head
            cur.next=node
    def insert(self,pos,item):
        node=Node(item)
        # pos 从0开始
        if pos<=0:
            self.add(item)
        elif pos>=self.length()-1:
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<pos-1:
                count+=1
                pre=pre.next
            #当循环推出后，pre指向pos-1位置
            node.next=pre.next
            pre.next=node
    def search(self,item):
            '查找节点是否存在'
            #空链表返回False
            if self.is_empty():
                return False
            cur=self.__head
            while cur.next!=self.__head:
                if cur.elem==item:
                    return True
                else:
                    cur=cur.next
            #处理尾部节点：
            if cur.elem == item:
                return True
            return False
    def remove(self,item):
        cur=self.__head
        pre=None
        while cur.next!=self.__head:
            #空节点 不做任何操作
            if self.is_empty():
                return
            if cur.elem==item:
                #先判断此节点是否是头节点
                if cur==self.__head:
                    #找尾节点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    #退出循环 找到尾节点
                    self.__head=cur.next
                    rear.next=self.__head
                else:
                #中间节点
                    pre.next=cur.next
                return
            else:
                pre=cur
                cur=cur.next
        #退出循环 cur指向尾节点
        if cur.elem==item:
            if cur==self.__head:
                #链表只有一个节点
                self.__head=None
            else:
                pre.next=self.__head

