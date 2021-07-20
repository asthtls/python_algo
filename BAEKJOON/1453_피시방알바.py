#1453_피시방알바

import sys

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
arr = [0] * 101
refu = 0

for i in people:
    if arr[i] != 0:
        refu += 1
    else:
        arr[i] += 1

print(refu)