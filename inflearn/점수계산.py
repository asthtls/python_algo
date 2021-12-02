import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
cnt = 0
sum = 0
for i in range(N):
    
    if li[i] == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)