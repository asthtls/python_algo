#13300_방배정

import sys

people,max_people = map(int, sys.stdin.readline().split())

student = [[0] * 2 for _ in range(6)]

room_sum = 0

for _ in range(people):
    sex, grade = map(int, sys.stdin.readline().split())
    student[grade-1][sex-1] += 1


for i in range(6):
    for j in range(2):
        if student[i][j] % max_people == 0:
            room_sum += student[i][j] / max_people
        else:
            room_sum += student[i][j] // max_people+1
print(int(room_sum))
