import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
if n == m:
    print(2*(n-1))
else:
    if n < m:
        print((min(n,m)-1)*2+1)
    else:
        print((m-1)*2)