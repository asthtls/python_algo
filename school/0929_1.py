# 퀵정렬

def QuickSort(A, left, right):
    if(left < right):
        mid = partition(A, left, right)
        QuickSort(A, left, mid-1)
        QuickSort(A, mid+1, right)

def s_sort(A, k):
    A.sort()
    return A[k-1]

# def Selection(A, left, right, k):
#     pos = partition(A, left, right)

#     if(post+1 == left+k):
def Selection(A,left,right,k):
    
    pos = partition(A,left,right)
    
    if(pos+1==left+k):
        return A[pos]
    
    elif(pos+1>left+k):
        return Selection(A,left,pos-1,k)
    
    else:
        return Selection(A,pos+1,right,k-(pos+1-left))
        

def partition(A, left, right):
    L = left+1
    H = right
    pivot = A[left] # 피봇설정
    
    while(L <= H):
        while L <= right and A[L] < pivot:
            L+=1
        while H > left and A[H] > pivot:
            H -= 1
        if L < H:
            A[L], A[H] = A[H], A[L]
    A[left], A[H] = A[H], A[left]
    return H

# 출력
d = [40,8,9,2,30,60,15,55,3]
print("처음값 : ", d)
# QuickSort(d, 0, len(d)-1)
Selection(d,0,len(d)-1,7)
print("7번째 값 : ",s_sort(d,7))
# print("정렬후 : ",d)
