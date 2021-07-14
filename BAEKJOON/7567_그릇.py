#7567_그릇

import sys


arr = list(sys.stdin.readline().rstrip())
cnt = 0

for i in range(len(arr)):
    if i == 0:
        cnt += 10
    elif arr[i] == arr[i-1]:
           cnt += 5
    else:
        cnt += 10

print(cnt)

