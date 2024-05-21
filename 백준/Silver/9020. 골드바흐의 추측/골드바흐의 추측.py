import sys
input = sys.stdin.readline

T = int(input().strip())
ar = [0 for _ in range(10001)]
ar[0] = ar[1] = 1

for i in range(2,10001):
    if ar[i] == 0:
        n = i*2
        while n <= 10000:
            if ar[n] == 0:
                ar[n] = 1
            n += i

for i in range(T):
    x = int(input().strip())
    diff = 10000
    p = []
    for j in range(2, 10001):
        if ar[j] == 0:
            tmp = x - j
            if ar[tmp] == 0:
                if diff > abs(j-tmp):
                    diff = abs(j-tmp)
                    p = [j, tmp]
    print(*p)