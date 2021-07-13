#10773_제로

import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):
    x = int(sys.stdin.readline())
    if x == 0:
        del arr[-1]
    else:
        arr.append(x)

if len(arr) == 0:
    print(0)
else:
    print(sum(arr))