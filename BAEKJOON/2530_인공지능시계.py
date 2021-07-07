#2530_인공지능시계

import sys

H, M, S = map(int, sys.stdin.readline().split())
r_s = int(sys.stdin.readline())

S += r_s % 60
r_s = r_s // 60

if S >= 60:
    S -= 60
    M += 1

M += r_s%60
r_s = r_s // 60 

if M >= 60:
    M -= 60
    H += 1

H += r_s%24

if H >= 24:
    H -= 24

print(H, M, S)