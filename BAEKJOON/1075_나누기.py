#1075_나누기

import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

N = N // 100
tmp = N * 100
while tmp % F != 0:
    tmp += 1

print(str(tmp)[-2:])