import sys
input = sys.stdin.readline

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

y = b[0] - a[0] + 1
z = b[0] - a[0]

if a[0] <= b[0] :
    if (a[1] == b[1] and a[2] <= b[2]) or (a[1] < b[1]):
        x = y - 1
    else:
        x = y - 2

print(x)
print(y)
print(z)