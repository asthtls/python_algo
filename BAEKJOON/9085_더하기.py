#9085_더하기

import sys

t = int(sys.stdin.readline())

nums = []

for i in range(t):
    n = int(sys.stdin.readline())
    nums.append(sum(list(map(int, sys.stdin.readline().split()))))        

for i in range(len(nums)):
    print(nums[i])
