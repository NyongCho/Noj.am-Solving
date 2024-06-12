from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    directions = [[1,0], [0,1], [-1, 0], [0, -1]]
    islands = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                s = 0
                q = deque()
                q.append([i,j])
                visited[i][j] = 1
                
                while q:
                    cx, cy = q.popleft()
                    s += int(maps[cx][cy])
                    
                    for dx, dy in directions:
                        tx = cx + dx
                        ty = cy + dy
                        
                        if 0 <= tx < n and 0 <= ty < m:
                            if maps[tx][ty] != 'X' and visited[tx][ty] == 0:
                                visited[tx][ty] = 1
                                q.append([tx,ty])
                islands.append(s)
                
    islands.sort()
    if not islands:
        islands.append(-1)
    
    return islands