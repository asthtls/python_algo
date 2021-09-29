from queue import Queue


def radix_sort(A):
    q=[]
    for i in range(10):
        q.append(Queue())
        n=len(A)
        factor=1

    for d in range(4):
        for i in range(n):
            q[(A[i]//factor) % 10].put(A[i])
        j=0
        for b in range(10):
            while not q[b].empty():
                A[j]=q[b].get()
                j+=1
        factor *=10
        print("step", d+1, A)


import random
data = []
for i in range(10):
    data.append(random.randint(1, 99))
radix_sort(data)
print("radix: ", data)
