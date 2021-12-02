import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

min = sys.maxsize

ave = sum(li)/N
ave += 0.5
ave = int(ave)

for idx, x in enumerate(li):
    temp = abs(x - ave)

    if temp < min: # 절댓값을 기준으로 가장 가까운 값의 위치 확인 및 score로 어떤 값인지 score로 저장
        min = temp
        score = x
        rep = idx + 1
    
    elif temp == min: # 동일한 경우 큰 값의 위치가 나오게 조건문
        if x > score:
            score = x
            rep = idx + 1

print(ave, rep)