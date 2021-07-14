#1076_저항

import sys

c1 = sys.stdin.readline().strip()
c2 = sys.stdin.readline().strip()
c3 = sys.stdin.readline().strip()

colors = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

print((colors[c1]*10+colors[c2]) * (10 ** colors[c3]))