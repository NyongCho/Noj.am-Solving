import sys
import heapq
input = sys.stdin.readline

def dijkstra(M, n):
    # visited = [[0 for _ in range(n)] for _ in range(n)]
    # visited[0][0] = 1
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    distances[0][0] = M[0][0]

    directions = [[0,1], [1,0], [0,-1],[-1,0]]

    pq = [[0, [0,0]]]
    while pq:
        current_weight, current_node = heapq.heappop(pq)

        for dx, dy in directions:
            tx = dx + current_node[0]
            ty = dy + current_node[1]

            if 0 <= tx < n and 0 <= ty < n:
                distance = distances[current_node[0]][current_node[1]] + M[tx][ty]

                if distance < distances[tx][ty]:
                    distances[tx][ty] = distance
                    heapq.heappush(pq, [distance, [tx, ty]])

    return distances[n-1][n-1]

cnt = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    M = []
    for _ in range(n):
        M.append(list(map(int, input().strip().split())))
    print("Problem {:}: {:}".format(cnt, dijkstra(M, n)))
    cnt += 1