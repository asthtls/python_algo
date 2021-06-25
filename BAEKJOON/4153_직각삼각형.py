#4153_직각삼각형


while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    max_value = max(num)
    num.remove(max_value)
    if num[0]**2 + num[1]**2 == max_value**2:
        print('right')
    else:
        print('wrong')
    
