#10984_내학점을구해줘

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline())
    c = 0
    g = 0

    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())

        c += int(a)
        g += float(a) * float(b)
    print(c, round(g/c, 1))