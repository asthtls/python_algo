# 그리디는 최적화문제를 해결하기위한 알고리즘
# 가장 큰값이나 작은값 찾아내는것 구할수있다. 거리와 관련된것
# 지난시간 동전
# 최소신장 트리 알아보자

#최소신장트리는 한가지 제약조건:사이클이 없이 모든 점들을 연결시켜야함
#선들이 간성이고 숫자가 가중치인데 이것을 합치면 최소가중치거리가 된다
#최소의 트리는 작은 간선연결
#크러스컬, 프림 정의 실질적은 크리스컬..
#크리스컬:가중치가 가장작은간선이 사이클을 만들지않을때만 추가시킴'욕심내어:그리드.크러스컬'
#프림:임의 점 선택 후 n-1개 간선 하나씩 추가.

#KruckalMST 알고리즘설명
#v가?  e가 새로만든 간선

#가중치기준으로 정렬해서 최소 가까운거 연결해야하므로 가까운것 연결
#사이클이 되지않도록 만들어서(돌지않게) 한줄은 제외시킴
#모든점을 지나야한다 가장작은 거리값을 선택하게끔 처리


#프림:(A먼저선택)마지막에 선택된 정점, 최소비용
class mSets:
    def __init__(self,n):
        self.parent=[-1]*n
        self.set_size=n

    def find(self,id):
        while(self.parent[id]>=0):
              id=self.parent[id]
        return id
    def union(self,s1,s2): #병합 
        self.parent[s1]=s2
        self.set_size-=1 # 하나씩 감소 

def test(V, m):#m:양쪽갈리는노드
    n = len(V) #리스트 길이 가져옴

    #정점만들었으면 초기화
    dsets = mSets(n) #클래스이름, 객체초기화
    E = [] #초기화결과 저장, 간선리스트 저장하는곳

    # 간선 만드는 작업 
    for i in range(n-1):
        for j in range(i+1, n):
            if m[i][j] != None: # 가중치가있으면
                E.append((i,j,m[i][j])) #튜플위치 #가중치저장
    E.sort(key=lambda e:e[2]) # sort됨
    #하나씩추가또는합칠껀데 카운트함

    ecount = 0
    for i in range(len(E)):
        #트리 좌우로 정점을 한 집합으로 찾기위해
        e = E[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])
        #두 루트를 비교 
        if uset != vset:
            dsets.union(uset, vset)#간선값 10진수 
            print("추가 (%s, %s, %d)"%(V[e[0]], V[e[1]], e[2]))
            ecount+=1 # 간선추가
            if ecount==n-1:
                break
    
ver = ["A","B","C","D","E","F","G","H"]
#A노드,B노드... 
weight=[[None,5,3,None,7,None,None,None],
        [5,None,None,4,1,None,None,None],
        [3,None,None,None,4,3,None,6],
        [None,4,None,None,None,None,3,None],
        [7,1,4,None,None,None,8,2],
        [None,None,3,None,None,None,None,1],
        [None,None,None,3,8,None,None,5],
        [None,None,6,None,2,1,5,None]]

test(ver, weight)



