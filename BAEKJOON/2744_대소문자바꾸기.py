#2744_대소문자바꾸기

import sys

arr = list(map(str, sys.stdin.readline()))
result = []

for i in arr:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        result.append(i.upper())
    else:
        result.append(i.lower())

result = result[:-1]

for a in result:
    print(a, end='')