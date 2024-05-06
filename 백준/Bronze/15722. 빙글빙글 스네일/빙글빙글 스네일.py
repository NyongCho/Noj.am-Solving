import sys
input = sys.stdin.readline

n = int(input())
# 2 6 8 10
# 2 8 17 27

num = 0
x = 0
y = 0
sign = 1
move = 1
while num < n:
    x += sign*move
    num += move
    if num >= n:
        if num > n:
            diff= abs(num-n)
            x -= sign*diff
        break
    y += sign*move
    num += move
    if num >= n:
        if num > n:
            diff= abs(num-n)
            y -= sign*diff
        break

    sign *= -1
    move += 1


print(y, x)