def merge_sort(alist):
    n=len(alist)
    if n<=1: #拆分到只剩一个元素
        return alist
    mid=n//2
    #left 采用归并排序后形成的有序的新的列表
    left=merge_sort(alist[:mid])  #拆分
    #right 采用归并排序后形成的有序的新的列表
    right=merge_sort(alist[mid:])  #拆分
    #将两个有序的子序列合并成一个新的整体
    left_pointer,right_pointer=0,0
    result=[]
    while left_pointer<len(left) and right_pointer<len(right):
        if left[left_pointer]<right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer+=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1
    #结束循环
    result+=left[left_pointer:]   #剩余部分追加
    result+=right[right_pointer:]    #剩余部分追加
    return result  #返回列表
if __name__=='__main__':
    a=[1,4,6,7,2,4,34,52,12,45,93]
    b=merge_sort(a)
    print(a)
    print(b)