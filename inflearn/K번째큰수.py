import sys

N,K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = set()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            res.add(arr[i] + arr[j] + arr[k])

res = list(res)
res.sort(reverse=True)
print(res[K-1])


