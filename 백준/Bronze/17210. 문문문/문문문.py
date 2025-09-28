import sys
input = sys.stdin.readline

N = int(input())
f = int(input())

if N < 6:
    for _ in range(N-1):
        f += 1
        print(f%2)
else:
    print('Love is open door')