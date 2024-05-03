import sys
input = sys.stdin.readline

a = int(input())
x, y = 0, 0
if a // 1000 == 0:
    if a // 100 == 0:
        x = a//10
        y = a%10
    else:
        x = a//10
        y = a%10

        if x > 10:
            x = a // 100
            y = a % 100
else:
    x = 10
    y = 10

print(x+y)