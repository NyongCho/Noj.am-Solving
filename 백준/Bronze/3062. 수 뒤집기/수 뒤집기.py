import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())

def reverse(num):
    x = 0

    while num != 0:
        x = x*10 + num%10
        num //= 10

    return x

for _ in range(n):
    m = int(input().strip())
    r = reverse(m)
    
    s = r+m
    sr = reverse(s)

    if s == sr:
        print('YES')
    else:
        print('NO')