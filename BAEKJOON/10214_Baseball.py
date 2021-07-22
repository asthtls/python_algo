#10214_Baseball

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    y = k = 0

    for i in range(9):
        n1, n2 = map(int, sys.stdin.readline().split())
        y += n1
        k += n2
    
    if y > k:
        print("Yonsei")
    elif k > y:
        print("Korea")
    else:
        print("Draw")
