#2566_최댓값

import sys

max_n = 0

for i in range(1, 10):
    arr = list(map(int, sys.stdin.readline().split()))
    if max(arr) > max_n : 
        max_n = max(arr)
        index_x = i 
        index_y = arr.index(max_n) + 1

print(max_n)
print(index_x, index_y)