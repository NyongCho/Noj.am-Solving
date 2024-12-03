import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
cnt = 0

for n in range(1, N+1):
    sn = str(n)
    for d in sn:
        if d == str(M):
            cnt += 1

print(cnt)