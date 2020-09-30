def shell_sort(alist):
    n=len(alist)
    gap=n//2 #步长
    while gap >0:
        #希尔排序与普通的插入算法区别就是gap步长
        for  j in range(gap,n):
            i=j
            while i>0:
                if alist[i]<alist[i-gap]:  #判断后一个元素是否比前一个元素小
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]  #交换位置
                    i-=gap #交换一次 往前移动gap个位置
                else:
                    break
        gap//=2  #缩短gap步长
if __name__=='__main__':
    a=[1,4,6,7,2,4,34,52,12,45,93]
    shell_sort(a)
    print(a)