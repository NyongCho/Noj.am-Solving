import sys

input = sys.stdin.readline
output = sys.stdout.write

n, k = map(int, input().split())

remain = n - k
sum = 0

for i in range(k):
    sum += int(input())

output(f'{(sum + remain * (-3)) / n :.4f} {(sum + remain * 3)/n:.4f}')
