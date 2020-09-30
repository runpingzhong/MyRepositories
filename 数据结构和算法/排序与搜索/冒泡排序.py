def bubble_sort(alist):
    n=len(alist)
    for j in range(n-1):
        for i in range(n-1-j):  #从头走到尾
            count=0  #记录交换的次数
            if alist[i]>alist[i+1]:#判断前一个元素是否大于后一个元素
                count+=1
                alist[i],alist[i+1]=alist[i+1],alist[i]  #两个元素交换位置
            if count==0: #没有进行交换 列表是有序表 直接退出循环
                return
if __name__=='__main__':
    a=[1,4,6,7,2,34,52,12,45,93]
    bubble_sort(a)
    print(a)