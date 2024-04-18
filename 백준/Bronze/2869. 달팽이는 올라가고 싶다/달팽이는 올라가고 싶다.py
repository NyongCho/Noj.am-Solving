import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
print(int(1+math.ceil((V-A)/(A-B))))