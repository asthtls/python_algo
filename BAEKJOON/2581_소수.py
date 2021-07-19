#2581_소수

import sys

n_min = int(sys.stdin.readline().rstrip())
n_max = int(sys.stdin.readline().rstrip())

prime = []

for i in range(n_min, n_max+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0 :
            cnt+=1
            if cnt >2:
                break
    if cnt == 2:
        prime.append(i)

if len(prime) == 0:
    print('-1')
else:
    print(sum(prime))
    print(min(prime))