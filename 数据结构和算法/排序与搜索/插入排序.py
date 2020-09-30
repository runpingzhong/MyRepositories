def insert_sort(alist):
    n=len(alist)
    for j in range(1,n): #从1 到最后一个
        i=j #i代笔内层循环起始值
        #执行从右边的第一个元素取出第一个元素，即i位置的元素 然后将其插入到前面的正确位置
        while i>0: #移动到0就停止
            if alist[i]<alist[i-1]: #前一个元素比当前元素小 才开始交换
                alist[i],alist[i-1]=alist[i-1],alist[i]  #交换位置
                i-=1 #继续往前移动
            else:  #已经有序 停止循环
                break
if __name__=='__main__':
    a=[1,4,6,7,2,4,34,52,12,45,93]
    insert_sort(a)
    print(a)