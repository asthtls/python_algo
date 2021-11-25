def Jobs(J):
    n = len(J)
    m = 4
    L = [x for x in range(10)]

    K = 1
    #print(arr)
    for i in range(n): # 작업종개수    
        min = 1
        
        for j in range(2, m):
            if L[j] < L[min]:
                min = j
        L[min] = L[min] + J[i]
        KK = K+1

    return L[min]

J = [5,2,4,3,4,7,9,2,4,1]
Job = Jobs(J)
print(Job)