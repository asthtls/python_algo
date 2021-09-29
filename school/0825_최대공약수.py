# 0825_2장_최대공약수
import sys
x, y = map(int,sys.stdin.readline().split())
def gcd(a, b):
    while b!= 0: # b가 0이 되기 전까지 반복
        k = a % b
        a = b
        b = k
    return a
print(x,"와",y,"의 최대 공약수는 = ", gcd(x, y))
