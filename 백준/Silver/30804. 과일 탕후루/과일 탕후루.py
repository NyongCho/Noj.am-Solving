import sys
import math
input = sys.stdin.readline

n = int(input())

fruits = list(map(int, input().split()))
cate = [0]*10
count = 0
r = 0
max = 0

for i in range(n):
    while r < n and count <= 2:
        if cate[fruits[r]] == 0:
            count += 1
        cate[fruits[r]] += 1
        if count <= 2:
            max = max if max > r-i+1 else r-i+1
        r += 1
        # print(f"{count}, {r}, {max} {cate}")
    cate[fruits[i]] -= 1
    if cate[fruits[i]] == 0:
        count -= 1
            
print(max)