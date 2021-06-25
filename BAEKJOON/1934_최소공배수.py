#1934_최소공배수
import sys

def gcd(a,b):
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a


def lcm(a, b):
    return a*b // gcd(a,b) 

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a,b))
