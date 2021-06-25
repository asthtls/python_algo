

# num = int(input())

# def Fibonacci(n):
#     if n == 0:
#         return 0
#     elif num == 1 or num == 2 :
#         return 1
#     return Fibonacci(n-1) + Fibonacci(n-2)

# print(Fibonacci(num))


num = int(input())

arr = [i for i in range(num+1)]
arr[1] = 1  # 1번까지 1  = 0, 1, 1, 2, 3, 5~~~

for i in range(2, num+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])