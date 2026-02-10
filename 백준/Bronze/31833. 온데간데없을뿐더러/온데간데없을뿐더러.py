import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

X = int("".join(map(str, map(int, input().split()))))
Y = int("".join(map(str, map(int, input().split()))))

if X >= Y:
    output(f'{Y}\n')
elif X < Y:
    output(f'{X}\n')