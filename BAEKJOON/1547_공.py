#1547_공

import sys

n = int(sys.stdin.readline())
cup = [1,2,3]


for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    tmp_x = cup.index(x)
    tmp_y = cup.index(y)

    cup[tmp_x], cup[tmp_y] = cup[tmp_y], cup[tmp_x]\

print(cup[0])