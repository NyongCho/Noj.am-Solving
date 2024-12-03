import sys
input = sys.stdin.readline

n = int(input().strip())
m = []
for _ in range(n):
    m.append(list(map(int,input().strip().split())))
#print(*m,sep='\n')

def check(x:int, y:int, len:int):
    if len == 1:
        if m[x][y] == 1:
            return [0,1]
        else:
            return [1,0]
    else:
        len //= 2
        b = [0 for _ in range(4)]
        b[0] = check(x,y,len)
        b[1] = check(x,y+len,len)
        b[2] = check(x+len,y,len)
        b[3] = check(x+len,y+len,len)
        if (b[0][0] == 0 or b[0][1] == 0) and (b[0] == b[1] and b[1] == b[2] and b[2] == b[3]):
            if b[0][0] == 0:
                return [0,1]
            else:
                return [1,0]
        else:
            l = [0,0]
            for i in range(4):
                l[0] += b[i][0]
                l[1] += b[i][1]
            return l
r = check(0,0,n)
print(*r,sep='\n')