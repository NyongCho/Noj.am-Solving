import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())

for i in range(n):
    for j in range(n-1-i):
        output(' ')
    output('*')
    for j in range(2*i-1):
        output(' ')
    if i != 0:
        output('*')
    print()