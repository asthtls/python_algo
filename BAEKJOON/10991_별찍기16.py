#10991_별찍기16

import sys

num = int(sys.stdin.readline())

for i in range(1,num+1):
    print(' '*(num-i) + '* '*(i-1)+'*') 