#2501_약수구하기

import sys

n, k = map(int, sys.stdin.readline().split())

li = []

for i in range(1,n+1):
    if n % i == 0:
        li.append(i)

if len(li) >= k:
    print(li[k-1])
else:
    print(0)