import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
visited = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
empty = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt = 0
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                cnt += 1
                for k in range(4):
                    nx = x + dxy[k][0]
                    ny = y + dxy[k][1]
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
            empty.append(cnt)

if empty == []:
    M = -1
for space in empty:
    if space > K:
        M -= space//K + space%K
    else:
        M -= 1

if M < 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(M)        