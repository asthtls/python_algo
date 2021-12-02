import sys

pay = int(sys.stdin.readline())

coin = [500,100,50,10,1]
coin.sort(reverse=True)

result = {i : 0 for i in coin}

for c in coin:
    coin_cnt = pay // c
    pay -= c * coin_cnt
    result[c] = coin_cnt

print(pay)
print(result)