#5554_심부름가는길

import sys

sum_va = 0
for i in range(4):
    sum_va += int(sys.stdin.readline())


x = sum_va//60
sum_va = sum_va % 60
y = sum_va 

print(x, y, sep='\n')    
