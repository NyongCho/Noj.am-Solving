import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

n = n*100 + m
if n == 218:
    print('Special')
elif n < 218:
    print('Before')
else:
    print('After')