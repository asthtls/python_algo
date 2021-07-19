#2745_진법변환

import sys

n, b = sys.stdin.readline().split()

b = int(b)
result = 0

al = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(n)):
    result += 