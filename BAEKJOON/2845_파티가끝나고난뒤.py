#2845_파티가끝나고난뒤

import sys

l, p = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
for i in li:
    print(i - l*p, end = ' ')
