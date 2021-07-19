#15969_행복

import sys

n = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))

print(max(score) - min(score))

