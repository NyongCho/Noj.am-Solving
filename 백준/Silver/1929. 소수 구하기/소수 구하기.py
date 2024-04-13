import sys
import math
I = sys.stdin
r = [True for _ in range(1000001)]
r[1] = False

for i in range(2, int(math.sqrt(1000000))+1):
    if(r[i] == True):
        j = 2
        while i*j <= 1000000:
            r[i*j] = False
            j+=1

m,n = map(int, I.readline().split())

for i in range(m, n+1):
    if(r[i]):
        sys.stdout.write(str(i)+"\n")