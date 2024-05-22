import sys
input = sys.stdin.readline

x = int(input().strip())
y = int(input().strip())
z = int(input().strip())

if x+y <= z:
    print(1)
else:
    print(0)