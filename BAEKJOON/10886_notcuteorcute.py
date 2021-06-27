#10886_0=notcute/1=cute

import sys

num = int(sys.stdin.readline())

cute = 0
not_cute = 0

for i in range(num):
    n = int(sys.stdin.readline())

    if n == 0:
        not_cute+=1
    elif n == 1:
        cute+=1

if cute > not_cute :
    print('Junhee is cute!')
elif not_cute > cute :
    print('Junhee is not cute!')    
