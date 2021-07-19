#10807_개수세기

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    if m == arr[i]:
        cnt+=1
    else:
        continue
print(cnt)