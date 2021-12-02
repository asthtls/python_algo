import sys

def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        res = res * 10 + tmp
        x = x//10
    return res

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

li = list(map(int, sys.stdin.readline().split()))

for i in li:
    temp = reverse(i)
    if isPrime(temp):
        print(temp, end=" ")
    
    
