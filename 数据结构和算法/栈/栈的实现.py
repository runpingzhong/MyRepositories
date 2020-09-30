'''
栈的操作
stack() 创建一个新的栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''
class Stack:
    '''栈'''
    def __init__(self):
        #生成容器
        self.__list=[]
    def push(self,item):
        # 添加一个新的元素item到栈顶
        self.__list.append(item)
    def pop(self):
        # 弹出栈顶元素
        if self.__list:
            return self.__list.pop()
        else:
            return None
    def peek(self):
        # 返回栈顶元素
        return self.__list[-1]
    def is_empty(self):
        # 判断栈是否为空
        return len(self.__list)==0
    def size(self):
        # 返回栈的元素个数
        return len(self.__list)
if __name__=='__main__':
    s=Stack()
    s.push(1)
    print(s.peek())