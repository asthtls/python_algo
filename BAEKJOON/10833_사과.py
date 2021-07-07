#10833_사과

import sys

num = int(sys.stdin.readline())

cnt = 0

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    cnt += b%a
    

print(cnt)