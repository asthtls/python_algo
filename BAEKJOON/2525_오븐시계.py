#2525_오븐시계

import sys

H, M = map(int, sys.stdin.readline().split())

C = int(sys.stdin.readline())

H += C // 60
M += C % 60

if M >= 60:
    H += 1
    M -= 60
if H>= 24:
    H -= 24

print(H,M)