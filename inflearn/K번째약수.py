import sys
# K번째 약수
n, k = map(int,sys.stdin.readline().split())
# k는 1이상 n이하 
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt +=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

    