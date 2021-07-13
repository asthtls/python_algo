#2490_윷놀이

import sys


li= [0]*4

for i in range(3):
    li= list(map(int,input().split()))
    if li.count(1) == 0:
        print('D')
    elif li.count(1) == 1:
        print('C')
    elif li.count(1) == 2:
        print('B')
    elif li.count(1) == 3:
        print('A')
    elif li.count(1) == 4:
        print('E')

