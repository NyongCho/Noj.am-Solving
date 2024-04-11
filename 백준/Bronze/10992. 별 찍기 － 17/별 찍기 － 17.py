import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
n -=1
for i in range(n):
    for j in range(n-i):
        output(' ')
    output('*')
    for j in range(2*i-1):
        output(' ')
    if i != 0:
        output('*')
    print()

n+=1
for i in range(2*n-1):
    output('*')