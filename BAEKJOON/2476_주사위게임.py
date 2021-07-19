#2476_주사위게임

import sys

n = int(sys.stdin.readline().rstrip())
money = 0

for i in range(n):
    n1,n2,n3 = map(int, sys.stdin.readline().split())
    
    if n1 == n2 == n3:
        money = max(money, 10000+n1*1000)
    elif n1 == n2:
        money = max(money, 1000+n1*100)
    elif n1 == n3:
        money = max(money, 1000+n1*100)
    elif n2 == n3:
        money = max(money, 1000+n2*100)
    else:
        money = max(money, max(n1,n2,n3)*100)

print(money)
