import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
f = 0
for i in range(n):
    output(str(i+1)+' ')
    f = 0
    if (i+1)%6 == 0:
        output('Go! ')
        f = 1

if not f:
    output('Go!')