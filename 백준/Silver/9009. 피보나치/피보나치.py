import sys
input = sys.stdin.readline

a,b,c = 0,1,0
fibo = []

while c < 1000000000:
    c = a + b
    a = b
    b = c
    fibo.append(c)
fibo.reverse()
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    i = 0
    r = []
    while n > 0:
        for e in range(i, 44):
            if fibo[e] <= n:
                n -= fibo[e]
                r.append(fibo[e])
                i = e
                break
    for i in range(len(r)-1, 0, -1):
        print(r[i], end=' ')
    print(r[0])
