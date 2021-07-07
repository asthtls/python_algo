#3003_킹,퀸,룩,비숍,나이트,폰

import sys

confi = [1,1,2,2,2,8]

num_li = list(map(int, sys.stdin.readline().split()))

for i in range(len(num_li)):
    print(confi[i] - num_li[i], end=' ')
