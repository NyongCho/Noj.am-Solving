import sys
from collections import deque
input = sys.stdin.buffer.readline

R, C = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(R)]

queue = deque()
queue.append((0, 0))
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1
total = data[0][0]

while queue:
    y, x = queue.popleft()
    if y == R - 1 and x == C - 1:
        break
    max_y, max_x = 0, 0
    max = 0
    for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
            if data[ny][nx] > max:
                max = data[ny][nx]
                max_y, max_x = ny, nx

    ny, nx = max_y, max_x
    visited[ny][nx] = 1
    queue.append((ny, nx))
    total += data[ny][nx]

print(total)