import sys

n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

cnt = 0
for x, y in zip(a,b):
    if x <= y:
        cnt += 1

print(cnt)