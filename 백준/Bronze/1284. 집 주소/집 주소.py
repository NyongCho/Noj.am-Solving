import sys
input = sys.stdin.readline

d = [4,2,3,3,3,3,3,3,3,3]

while True:
    a = int(input())
    if a == 0:
        break
    s = 0
    while a > 0 :
        s += d[a%10] + 1
        a //= 10
    s += 1
    print(s)