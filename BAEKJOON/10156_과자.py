#10156_과자

import sys

k, n, m = map(int,sys.stdin.readline().split())

if k * n < m:
    print('0')

elif k * n >=  m:
    print(k*n - m)


