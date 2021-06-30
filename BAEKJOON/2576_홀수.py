#2576_홀수

import sys

sum = 0
min_value = sys.maxsize
for i in range(7):
    n = int(sys.stdin.readline())
    if n%2 != 0 :
        sum += n
        if min_value > n:
            min_value = n

if sum == 0:
    print(-1)
else:
    print(sum,min_value, sep='\n')