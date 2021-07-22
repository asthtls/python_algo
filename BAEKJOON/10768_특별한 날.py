#10768_특별한 날

import sys

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

if month == 1:
    print("Before")
elif month > 2:
    print("After")
elif month == 2:
    if day == 18:
        print("Special")
    elif day >18:
        print("After")
    else:
        print("Before")