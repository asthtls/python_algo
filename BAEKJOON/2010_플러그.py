#2010_플러그
import sys

plug = int(sys.stdin.readline())
sum = 0

for i in range(plug):
    sum += int(sys.stdin.readline())

print(sum - (plug-1))