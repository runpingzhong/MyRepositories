#定义节点类
class Node(object):
    def __init__(self,elem):
        self.elem=elem #初始元素
        self.next=None #下一个节点初始指向空
'''定义链表  需要实现的功能：
    is_empty() 链表是否为空
    length() 链表的长度
    ravel() 遍历整个列表
    add(item) 链表头部增加元素
    append(item) 链表尾部增加元素
    insert(pos,item) 制定位置添加元素
    remove(item) 删除节点
    search(item) 查找节点是否存在'''
class Single_link_list(object):
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        return self.__head==None
    def length(self):
        # current游标 用来遍历节点
        current = self.__head #当前指向头节点
        count = 0
        while current != None:
            count += 1
            current=current.next  #指向下一个节点
        return count
    def travel(self):
       current=self.__head
       while current!=None:
           print(current.elem,end=' ')
           current=current.next
    def add(self,item):
        node=Node(item)
        node.next=self.__head
        self.__head=node
    def append(self,item):
        node=Node(item)
        if self.length()==0:  #判断是否为空
            self.__head=node
        else:
            current=self.__head
            while current.next!=None:
                current=current.next
            current.next=node #指向新加入的节点
    def insert(self,pos,item):
        # pos 从零开始
        if pos<=0:  #pos<=0 默认从头部添加
            self.add(item)
        elif pos>=self.length()-1:  #pos>= 列表的长度 默认尾部追加
            self.append(item)
        else:
            node=Node(item)
            pre=self.__head
            count=0
            while count<pos-1:
                count+=1
                pre=pre.next
            #当循环推出后 pre指向pos-1位置
            node.next=pre.next #插入节点的next指定pre插入位置前一个节点的next
            pre.next=node  #指定位置的前一个节点的next指向新插入的节点
    def remove(self,item):
        pre=None #前一个浮标初始指向None
        current=self.__head #当前节点初始指向第一个节点
        while current!=None:
            if current.elem==item:
                if pre==None:     #判断当前节点是不是头节点
                    self.__head=current.next
                else:
                    pre.next=current.next #上一个节点指向当前节点的下一个
                break
            else:
                pre=current #后一个节点指向当前节点
                current=current.next #当前节点指向下一个节点
    def search(self,item):
        current=self.__head
        while current!=None:
            if  current.elem==item:
                return True
            else:
                current=current.next
        return False
if __name__=='__main__':
    ll=Single_link_list()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.travel())
