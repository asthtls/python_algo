import sys


N,M = map(int, sys.stdin.readline().split())

cnt = [0 for i in range(N+M+3)] # 3을 더하는 이유
max = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] = cnt[i+j] + 1


for i in range(len(cnt)-2):
    if cnt[i] > max:
        max = cnt[i]

for i in range(len(cnt)-2):
    if cnt[i] == max:
        print(i, end=" ")
    


