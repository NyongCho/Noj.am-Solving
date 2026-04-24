import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
hull = deque()

def bad(l1, l2, l3):
    m1, c1 = l1; m2, c2 = l2; m3, c3 = l3

    return (c1 - c3) * (m2 - m1) <= (c1 - c2) * (m3 - m1)

def add_line(m, c):
    while len(hull) >= 2 and bad(hull[-2], hull[-1], (m, c)):
        hull.pop()

    hull.append((m, c))

def query(x):
    while len(hull) >= 2 and hull[0][0] * x + hull[0][1] >= hull[1][0] * x + hull[1][1]:
        hull.popleft()

    return hull[0][0] * x + hull[0][1]

add_line(b[0], dp[0])

for k in range(1, n):
    dp[k] = query(a[k])
    add_line(b[k], dp[k])

print(dp[n - 1])