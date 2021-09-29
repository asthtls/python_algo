# 버블정렬
print("버블정렬")
def bubbleSort(A):
    n=len(A)
    for pas in range(0,n-1): #1,n-1로 하면 마지막이 90,60이 되므로 한번더 수행
        for i in range(1,n-pas):
            if(A[i-1]>A[i]):
                tmp=A[i]
                A[i]=A[i-1]
                A[i-1]=tmp
    return A


AA=[90,30,50,20,40,10,80,60,70]
print("bubbleSort 정렬 전>",AA)
A=bubbleSort(AA)
print("bubbleSort 정렬 후>",A)

# 결과
# bubbleSort 정렬 전> [90, 30, 50, 20, 40, 10, 80, 60, 70]
# bubbleSort 정렬 후> [10, 20, 30, 40, 50, 60, 70, 80, 90]
#---------------------------------------------------------------
# 선택정렬
print("선택정렬")
def selectSort(A):
    n=len(A)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if(A[min]>A[j]):
                min=j
        tmp=A[i]
        A[i]=A[min]
        A[min]=tmp
    return A

AA=[90,30,50,20,40,10,80,60,70]
print("selectSort 정렬 전>",AA)
A=selectSort(AA)
print("selectSort 정렬 후>",A)
# 결과
# selectSort 정렬 전> [90, 30, 50, 20, 40, 10, 80, 60, 70]
# selectSort 정렬 후> [10, 20, 30, 40, 50, 60, 70, 80, 90]

#---------------------------------------------------------------
# 삽입정렬
print("삽입정렬")
def insertSort(A):
    n=len(A)
    for i in range(1,n):
        for j in range(i,0,-1):
            if(A[j-1]>A[j]):
                tmp=A[j-1]
                A[j-1]=A[j]
                A[j]=tmp
    return A


AA=[90,30,50,20,40,10,80,60,70]
print("insertSort 정렬 전>",AA)
A=insertSort(AA)
print("insertSort 정렬 후>",A)

#---------------------------------------------------------------
# 쉘 정렬

def ShellSort(A):
    n = len(A)
    h = n//2
    while h > 0:
        for i in range(h, n):
            tmp = A[i]
            j = i-h
            while j >= 0 and A[j] > tmp:
                A[j + h] = A[j]
                j -= h
            A[j+h] = tmp

        h //= 2
    return A
AA=[90,30,50,20,40,10,80,60,70]
print("정렬전 > ", AA)
A = ShellSort(AA)
print("정렬후 > ", A)  