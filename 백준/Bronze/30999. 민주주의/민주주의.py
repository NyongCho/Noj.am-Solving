import sys

input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())
half = int(m/2+0.5)
problem = 0

for _ in range(n):
    CB = input().strip()
    cnt = 0
    for i in CB:
        if i == 'O':
           cnt += 1

    if cnt >= half:
        problem += 1
output(str(problem) + '\n')