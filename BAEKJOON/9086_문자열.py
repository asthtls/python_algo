#9086_문자열

import sys

n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline().rstrip()
    print(str[0], str[-1], sep='')