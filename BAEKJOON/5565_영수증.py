#5565_영수증

import sys

max_value = int(sys.stdin.readline())
sum_book = 0

for i in range(9):
    n = int(sys.stdin.readline())
    sum_book += n

print(max_value - sum_book)

