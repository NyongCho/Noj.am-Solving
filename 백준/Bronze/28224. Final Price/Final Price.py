import sys
input = sys.stdin.readline

n = int(input().strip())
Sum = 0

for _ in range(n):
    Sum += int(input().strip())

print(Sum)