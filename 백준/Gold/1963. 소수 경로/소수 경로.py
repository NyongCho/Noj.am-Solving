import sys
from collections import deque
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
    a,b = map(int, input().strip().split())
    pq = deque()
    pq.append([a,0])
    add = [1,-1,10,-10,100,-100,1000,-1000]
    visited = [0 for _ in range(10000)]
    while pq:
        current_n, c_cnt = pq.popleft()
        if current_n == b:
            print(c_cnt)
            break

        for u in range(4):
            sn = current_n - (current_n//(10**u))%10 * (10**u)
            if u == 3:
                s = 1
            else:
                s = 0
            for i in range(s, 10):
                tn = sn + i*(10**u)
                
                if 1000 <= tn <= 9999 and ar[tn] == 0 and visited[tn] == 0:
                    visited[tn] = 1
                    pq.append([tn,c_cnt+1])

