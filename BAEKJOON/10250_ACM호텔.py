#10250_ACM호텔

import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    floor = N%H
    room = N//H +1

    if floor == 0:
        room -= 1
        floor = H
    
    print(floor * 100 + room)
