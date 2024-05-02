import sys
input = sys.stdin.readline

a = list(map(int, input().strip().split()))
m = float('inf')
t = 0

for n in range(a[1], a[2]+1):
    diff = abs(a[0] - n)

    if diff < m:
        m = diff
        t = n

print(t)