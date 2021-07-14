#2506_점수계산

import sys

n = int(sys.stdin.readline())
cnt = 0
sum = 0

li = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if li[i] == 1:
        cnt += 1
        sum += cnt

    else:
        cnt = 0

print(sum)