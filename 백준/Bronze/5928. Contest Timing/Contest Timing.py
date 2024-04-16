import sys
input = sys.stdin.readline

D,H,M = map(int ,input().strip().split())

D -= 11
H -= 11
M -= 11

if M < 0:
    H -= 1
    M += 60
if H < 0:
    D -= 1
    H += 24
if D < 0:
    print(-1)
else:
    a = D*24*60 + H*60 + M
    print(a)