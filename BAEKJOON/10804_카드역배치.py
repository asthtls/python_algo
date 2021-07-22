#10804_카드역배치

import sys

arr = [i for i in range(21)]

for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())

    for i in range((end-start+1)//2):
        arr[start+i], arr[end-i] = arr[end-i], arr[start+i]

for i in range(1,len(arr)):
    print(arr[i], end=' ')