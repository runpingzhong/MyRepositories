'''
条件：操作的对象必须是排好序的
     支持下标索引
'''
#递归版本
def binary_search(alist,item):
    n=len(alist)
    if n>0:
        mid=n//2 #找出中间位置索引值
        if alist[mid]==item:  #判断中间位置上的值是否等于需要查找的值
            return True
        elif item<alist[mid]:
            return binary_search(alist[:mid],item)  #递归调用
        else:
            return binary_search(alist[mid+1:],item) #递归调用
    #没有找到
    return False
#非递归版本
def binary_search_2(alist,item):
    n=len(alist)
    first=0
    last=n-1
    mid=(first+last)//2
    while first<=last:
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            last=mid-1
        else:
            first=mid+1
    return False
if __name__=='__main__':
    l=[1,2,3,4,5,10,12,49,70]
    print(binary_search(l,5))
    print(binary_search(l,2000))