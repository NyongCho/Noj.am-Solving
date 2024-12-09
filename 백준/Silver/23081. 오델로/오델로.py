import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
M = [list(str(input().strip())) for _ in range(n)]

def count(i, j):
    num = 0
    directions = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

    for dx, dy in directions:
        tb = 0
        f = 0
        cnt = 0
        nx, ny = i+dx, j+dy
        while 0 <= nx < n and 0 <= ny < n:
            if M[nx][ny] == '.':
                f = 1
                break
            elif M[nx][ny] == 'W':
                cnt += 1
            else:
                tb = 1
                break
            nx += dx
            ny += dy
        if tb == 1 and f == 0:
            num += cnt
    return num
        
max_n = 0
max_coord = None

for i in range(n):
    for j in range(n):
        if M[i][j] == '.':
            cnt = count(i, j)
            if max_n < cnt:
                max_n = cnt
                max_coord = [i, j]

if max_n == 0:
    print("PASS")
else:
    print(max_coord[1], max_coord[0])
    print(max_n)