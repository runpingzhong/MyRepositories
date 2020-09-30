'''队列
enqueue(item) 往队列中添加一个元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 队列的长度'''
#普通队列
class Queue:
    def __init__(self):
        #初始化容器
        self.__list=[]
    def enqueue(self,item):
        #往队列中添加一个元素
        self.__list.defppend(item)
    def dequeue(self):
        #从队列头部删除一个元素
        self.__list.pop(0)
    def is_empty(self):
        #判断一个队列是否为空
        return self.__list==[]
    def size(self):
        #队列的长度
        return len(self.__list)
'''双端队列
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个元素
add_rear(item) 从队尾加入元素
remove_front(item) 从队头删除元素
remove_rear(item) 从队尾删除元素
is_empty(item) 队列是否为空
size() 队列长度'''
class Deque:
    def __init__(self):
        self.__list=[]
    def Deque(self):
        return self.__list
    def add_front(self,item):
        self.__list.insert(0,item)
    def add_rear(self,item):
        self.__list.append(item)
    def pop_front(self):
        self.__list.pop(0)
    def pop_rear(self):
        self.__list.pop()
    def is_empty(self):
        return self.__list==[]
    def size(self):
        return len(self.__list)