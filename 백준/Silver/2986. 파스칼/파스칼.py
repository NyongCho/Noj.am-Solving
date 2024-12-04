import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
else:
    measure = []

    for k in range(1, int(sqrt(n))+1):
        if n % k == 0:
            measure.append(k)

    x = [] + measure

    for k in measure:
        if n%k == 0:
            x.append(n//k)

    x.sort()

    print(n - x[-2])