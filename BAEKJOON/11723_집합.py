#11723_집합

import sys

n = int(sys.stdin.readline())
li = set()

for _ in range(n):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            li = set([i for i in range(1, 21)])
        else:
            li = set()

    else:
        op, number = tmp[0], tmp[1]
        number = int(number)
        if op == 'add':
            li.add(number)
        elif op == 'check':
            print(1 if number in li else 0)
        elif op == 'remove':
            li.discard(number)
        elif op == 'toggle':
            if number in li:
                li.discard(number)
            else:
                li.add(number)
