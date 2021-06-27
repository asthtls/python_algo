#2875_대회or인턴

import sys

def max_team(n,m,k):
    cnt = 0
    while n+m-3 >= k and n>= 2 and m >= 1:
        n-=2
        m-=1
        cnt+=1
    return cnt


n,m,k = map(int, sys.stdin.readline().split())
print(max_team(n,m,k))