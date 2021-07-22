#2693_N번째 큰 수

import sys

n = int(sys.stdin.readline())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    print(arr[-3])