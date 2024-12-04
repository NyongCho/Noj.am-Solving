import sys
from math import sqrt
input = sys.stdin.readline

N, L = map(int, input().split())
spots = list(map(int, input().split()))

spots.sort()
using_tape = 0
cnt = 0

for spot in spots:
    if using_tape > 0:
        if using_tape >= spot:
            continue
        else:
            using_tape = spot + L - 1
            cnt += 1
    else:
        using_tape = spot + L - 1
        cnt += 1
    # print(spot, using_tape, cnt)

print(cnt)