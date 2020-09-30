def quike_sort(alist,first,last):
    if first>=last:  #终止条件
        return
    temp_value=alist[first]
    low=first
    high=last
    while low<high:
        while low<high and alist[high]>=temp_value:#如果high所指的数值大于temp_value high  并且low<high 向前移动
                high-=1
        #high所指的元素小于等于temp——value 退出循环
        alist[low]=alist[high]  #交换位置
        while low<high and alist[low]<temp_value:#如果low所指的数值小于temp_value high  并且low<high 向后移动
                low+=1
        # low所指的元素大于等于temp——value 退出循环
        alist[high]=alist[low]  #交换位置
    #从循环退出时 low==high
    alist[low]=temp_value
    quike_sort(alist,first,low-1) #递归调用  对low左边的列表执行快速排序
    quike_sort(alist,low+1,last) #递归调用 对low右边边的列表执行快速排序
if __name__=='__main__':
    a=[1,4,6,7,2,4,34,52,12,45,93]
    quike_sort(a,0,len(a)-1)
    print(a)