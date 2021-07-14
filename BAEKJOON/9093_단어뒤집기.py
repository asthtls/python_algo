#9093_단어뒤집기

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    li = list(map(list, sys.stdin.readline().split()))
    for i in li:
        print(''.join(i[::-1]), end=" ")
    print()
    