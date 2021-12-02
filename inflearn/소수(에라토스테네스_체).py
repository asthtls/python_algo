# 소수 에라토스테네스 체 
import sys

def isPrime(a):
    if a<2:
        return False
    for i in range(2, a):
        if a%i == 0:
            return False
    return True

N = int(sys.stdin.readline())
cnt = 0

for i in range(N+1):
    if isPrime(i):
        cnt += 1

print(cnt)