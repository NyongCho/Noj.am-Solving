import sys
import math
input = sys.stdin.readline

n = int(input())

s = [0 for _ in range(n+1)]
s[0] = s[1] = 1
for i in range(2,int(math.sqrt(n))+1):
    if(s[i] == 1):
        continue
    for j in range(2,n//i+1):
        s[i*j]=1
ss = [i for i in range(n+1) if s[i] == 0]

m = len(ss)
r = 0
sum = 0
cnt = 0
for f in range(m):
    while (sum < n and r < m):
        sum += ss[r]
        r += 1
    if sum == n:
        #print(ss[f:r])
        cnt+=1
    sum -= ss[f]
    
print(cnt)

#print(ss)