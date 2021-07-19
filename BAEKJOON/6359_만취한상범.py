#6359_만취한상범

# import sys

# n = int(sys.stdin.readline())

# for _ in range(n):
#     m = int(sys.stdin.readline())
#     d = [0] * (n+1)

#     for i in range(1, n+1):
#         for j in range(i, n+1, i):
#             d[j] += 1
#     cnt = 0
#     for i in range(1, n+1):
#         if d[i] % 2 == 1:
#             cnt +=1

#     print(cnt)

import sys
from math import floor

n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    print(floor(m ** 0.5))