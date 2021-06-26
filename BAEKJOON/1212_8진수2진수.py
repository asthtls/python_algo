#1212_8진수2진수

import sys

num = sys.stdin.readline()

tmp = int(num,8)
print(bin(tmp)[2:])


