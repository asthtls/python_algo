import heapq

def heap_tree(freq, alpha):
    n = len(alpha)
    h = []

# (키, 값) 삽입:
    for i in range(n):
        heapq.heappush(h, (freq[i],alpha[i]))
        print(freq[i], alpha[i])
        print("h : ",h)


# 병합
    for i in range(1, n):
        test1 = heapq.heappop(h) # 가장 작은 트리
        test2 = heapq.heappop(h) # 다음 작은 트리
        heapq.heappush(h, (test1[0] + test2[0], test1[1] + test2[1]))
        print(test1, '+', test2)
        

alpha = ["a","b","c","d","e"]
freq = [6,4,3,5,1]
heap_tree(freq, alpha)
# 단답식 힙 나옵니다.!