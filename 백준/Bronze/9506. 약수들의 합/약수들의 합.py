import sys
from math import sqrt
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break

    end = int(sqrt(n))+1
    measure = []

    for i in range(1, end+1):
        if n % i == 0:
            measure.append(i)
    
    for m in measure:
        extra = n // m
        if extra not in measure:
            measure.append(extra)

    measure.sort()
    if sum(measure) == n*2:
        print(f"{n} =", end='')
        for i in measure[:-2]:
            print(f" {i} +", end='')
        print(f" {measure[-2]}")
    else:
        print(f"{n} is NOT perfect.")
