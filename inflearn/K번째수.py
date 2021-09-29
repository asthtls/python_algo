import sys

T = int(sys.stdin.readline())

for i in range(T):
    n,s,e,k = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    arr = arr[s-1:e]
    arr.sort()
    
    print("#%d %d"%(i+1, arr[k-1]))