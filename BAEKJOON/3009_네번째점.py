#3009_네번째점

import sys

x_li = []
y_li = []


for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_li.append(x)
    y_li.append(y)

for i in range(3):
    if x_li.count(x_li[i]) == 1:
        answer_x = x_li[i]     
    if y_li.count(y_li[i]) == 1:
        answer_y = y_li[i]

print(answer_x, answer_y)
