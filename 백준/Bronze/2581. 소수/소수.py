import sys
import math
input = sys.stdin.readline
output = sys.stdout.write

s = [1 for _ in range(10001)]

for i in range(2, int(math.sqrt(10000))+1):
    if s[i] == 1:
        for j in range(2, 10001):
            if (i*j > 10000):
                break
            s[i*j] = 0


m = int(input().strip())
n = int(input().strip())
sm = 0
mm = -1

s[0] = s[1] = 0

for i in range(n, m-1, -1):
    if s[i] == 1:
        sm += i
        mm = i

if mm == -1:
    print('-1')
else:
    print(sm)
    print(mm)