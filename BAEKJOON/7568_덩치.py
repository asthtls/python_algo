#7568_덩치

import sys

num = int(sys.stdin.readline())

p = [[0]*2 for i in range(num)]

for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    p[i][0] = x
    p[i][1] = y

for i in range(num):
    rank = 1
    for j in range(num):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            rank += 1

    print(rank, end=' ')