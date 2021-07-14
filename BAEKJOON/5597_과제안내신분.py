#5597_과제안내신분

import sys

li = [0 for i in range(31)]

for i in range(1,29):
    li[int(input())] += 1

for i in range(1,31):
    if li[i] == 0:
        print(i)