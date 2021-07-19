#2789_유학금지

import sys

arr = sys.stdin.readline()

change = "CAMBRIDGE"
for i in change:
    arr = arr.replace(i, "")


print(arr)