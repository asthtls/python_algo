#2455_지능형기차

import sys

people = 0
m_people = []
for _ in range(4):
    p_out, p_in = map(int, sys.stdin.readline().split())

    people += p_in
    people -= p_out

    m_people.append(people)

print(max(m_people))    
