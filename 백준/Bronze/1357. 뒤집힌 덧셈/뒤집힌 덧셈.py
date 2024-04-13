import sys
input = sys.stdin.readline
output = sys.stdout.write

def reverse(num):
    x = 0

    while num != 0:
        x = x*10 + num%10
        num //= 10

    return x
n,m = map(int, input().strip().split())

print(reverse(reverse(n)+reverse(m)))