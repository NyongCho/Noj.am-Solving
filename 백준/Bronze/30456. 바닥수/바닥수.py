import sys

input = sys.stdin.readline
output = sys.stdout.write

N, L = map(int, input().strip().split())

for i in range(L-1):
    output('1')

output(f'{N}\n')