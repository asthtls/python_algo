#11050_이항계수1

import sys
from math import factorial as ft

n, k = map(int, sys.stdin.readline().split())
print(ft(n) // (ft(k)*ft(n-k)))