import sys

input = sys.stdin.readline
output = sys.stdout.write

n, m = map(int, input().split())

basket = [i for i in range(n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    temp = basket[i : k]
    
    f = k - i
    r = j-k+1
    for idx in range(r):
        basket[i + idx] = basket[k + idx]
    
    for idx in range(f):
        basket[i + r + idx] = temp[idx]
    

print(*basket[1:])