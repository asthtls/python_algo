#2747_피보나치 수

num = int(input())

arr = [i for i in range(num+1)]
arr[1] = 1  # 1번까지 1  = 0, 1, 1, 2, 3, 5~~~

for i in range(2, num+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])