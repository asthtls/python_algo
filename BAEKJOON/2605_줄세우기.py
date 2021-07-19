#2605_줄세우기

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

arr_num = []

for i in range(n):
    arr_num.insert(i-arr[i], i+1)

for j in arr_num:
    print(j, end=' ')