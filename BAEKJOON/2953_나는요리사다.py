#2953_나는요리사다

import sys

score = []

for i in range(5):
    score.append(sum(map(int, sys.stdin.readline().split())))

print(score.index(max(score))+1, max(score))