import sys
input = sys.stdin.readline

n = int(input().strip())
x = ''

for _ in range(n):
    a = input().strip()
    if 'S' in a:
        x = a
        
print(x)