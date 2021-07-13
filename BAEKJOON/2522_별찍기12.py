#2522_별찍기12

import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
    print(' '*(num-i) + '*'*(i))

for j in range(1, num):
    print(' '*(j) + '*'*(num-j))
    
    