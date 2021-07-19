#5596_시험점수

import sys

m1 = sum(map(int, sys.stdin.readline().split()))
m2 = sum(map(int, sys.stdin.readline().split()))

if m1 > m2:
    print(m1)
else:
    print(m2)
 