import random
def DownHeap(A, i, heap_size):
    largest=i
    left_i=2*i
    right_i=2*i+1

    if left_i<heap_size and A[left_i]>A[largest]:
        largest=left_i
    if right_i<heap_size and A[right_i]>A[largest]:
        largest=right_i
    if largest !=i:
        A[largest], A[i]=A[i], A[largest]

# DownHeap(A, largest, heap_size)

def heap_sort(list):
    n=len(list)
    for i in range(n//2-1, -1, -1):
        DownHeap(list, i, n)
        print("*"*50)
        print("heap", list)
        print("*"*50)
    for i in range(n-1, 0, -1):
        list[0], list[i]=list[i], list[0]
        DownHeap(list, 0, i)
    return list

l=[random.randint(1, 10) for i in range(10)]
print('소트전>', l)
sorted_list=heap_sort(l)
print('소트후',sorted_list)

#
# 소트전> [8, 7, 9, 7, 3, 7, 9, 4, 9, 8]
# **************************************************
# heap [8, 7, 9, 7, 9, 7, 9, 4, 3, 8]
# **************************************************
# **************************************************
# heap [8, 7, 9, 9, 9, 7, 7, 4, 3, 8]
# **************************************************
# **************************************************
# heap [8, 7, 9, 9, 9, 7, 7, 4, 3, 8]
# **************************************************
# **************************************************
# heap [8, 9, 7, 9, 9, 7, 7, 4, 3, 8]
# **************************************************
# **************************************************
# heap [9, 8, 7, 9, 9, 7, 7, 4, 3, 8]
# **************************************************
# 소트후 [3, 7, 9, 9, 7, 7, 4, 8, 8, 9]
