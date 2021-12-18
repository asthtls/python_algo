def knapsack(wg, mm, C, rowCount):
    #초기화
    k=[[0 for _ in range(C+1)] for _ in range(rowCount+1)]

    for row in range(0, rowCount):
        print(wg[row], "kg-->", end="")
        for col in range(0, C):
            if wg[row]>col:
                k[row][col]=k[row-1][col]
            else: # 여기서 문제 나옴
                v1=mm[row]+k[row-1][col-wg[row]]
                v2=k[row-1][col]
                k[row][col]=max(v1, v2) # max 에서 나옴 - v1, v2 확인
            print("%2d  " % k[row][col], end="") # 뭘 print하는지
        print()
    return k[rowCount-1][C-1] # 뭘 return 하는지 대소문자도 확인

C=10
rowCount=4
wg=[5, 4, 6, 3]
mm=[10, 40, 30, 50]

maxValue=knapsack(wg, mm, C, rowCount)
print()
print("배낭에 담는 최대값", maxValue)


