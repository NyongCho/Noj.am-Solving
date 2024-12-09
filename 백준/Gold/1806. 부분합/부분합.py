import sys
from math import sqrt
input = sys.stdin.readline

n, m = map(int, input().strip().split())

nums = list(map(int, input().strip().split()))

s = 0
length = len(nums)
r = 0
min_len = length
f = 0


for i, k in enumerate(nums):
    while r < length and i <= r and s < m:
        s += nums[r]
        r += 1
    if min_len >= r - i and s >= m:
        f = 1
        min_len = r - i
            # print(i, r)
    
    s -= k

if f == 0 or m == 0:
    print(0)
else:
    print(min_len)