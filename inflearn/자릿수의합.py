import sys

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x %10
        x = x//10
    return sum

li = list(map(int, sys.stdin.readline().split()))
tmp = 0
max = -1

for number in li:
    temp = digit_sum(number)

    if temp > max:
        max = temp
        tmp = number
print(tmp)

