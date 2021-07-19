#3047_ABC

import sys

numbers = list(map(int, sys.stdin.readline().split()))
alpha = list(map(str, sys.stdin.readline()))

numbers.sort()

for i in alpha:
    if i == 'A':
        print(numbers[0], end=' ')
    elif i == 'B':
        print(numbers[1], end = ' ')
    elif i == 'C':
        print(numbers[2], end = ' ')
        
        

