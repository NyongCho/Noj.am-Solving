import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(n)
l = []
while m > 0:
    l.append(m%10)
    m //=10
l.sort(key = lambda x : (-x))
print(*l,sep="")