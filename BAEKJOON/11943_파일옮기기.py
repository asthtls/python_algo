#11943_파일옮기기

import sys

a,b = map(int, sys.stdin.readline().split())
c,d = map(int, sys.stdin.readline().split())

print(min(a+d, b+c))