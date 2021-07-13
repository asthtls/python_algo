#10808_알파벳개수

import sys

num = list(sys.stdin.readline())

ap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(ap)):
    cnt = num.count(ap[i])
    print(cnt, end=' ')