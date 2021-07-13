#10797_10부제

import sys

num = int(sys.stdin.readline())


# cnt = 0
# arr = []
# for i in range(5):
#     if arr[i] == num:
#         cnt += 1
# print(cnt)


arr = list(map(int, sys.stdin.readline().split()))
print(arr.count(num))