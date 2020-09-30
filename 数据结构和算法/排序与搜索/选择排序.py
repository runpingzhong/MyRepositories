def select_sort(alist):
    n=len(alist)
    for j in range(n-1):  #j:0~n-2
        min_index = j  # 初始设定第一个位置的值就是最小值
        for i in range(j+1,n): #遍历列表
            if alist[i]<alist[min_index]:  #比较
                min_index=i  #如果当前数值小于最小值 更新最小值下标
        alist[j],alist[min_index]=alist[min_index],alist[j] #退出循环之后  交换位置
if __name__=='__main__':
    a=[1,4,6,7,2,4,34,52,12,45,93]
    select_sort(a)
    print(a)