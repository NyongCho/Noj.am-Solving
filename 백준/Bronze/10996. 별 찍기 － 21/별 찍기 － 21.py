import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
for i in range(n*2):
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0:
                output('*')
            else:
                output(' ')

    else:
        for j in range(n):
            if j % 2 == 1:
                output('*')
            else:
                output(' ')
    print()