#1373_2진수8진수

import sys

num = sys.stdin.readline()

tmp = int(num,2)

print(oct(tmp)[2:])