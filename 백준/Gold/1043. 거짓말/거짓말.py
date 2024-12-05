import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

tp = input().strip().split()
if tp[0] == '0':
    for _ in range(m):
        input()
    print(m)
else:
    tp = list(map(int, tp))
    trust = [0] * (n+1)
    parties = []

    edge = {i:[] for i in range(1,n+1)}
    # print(edge)


    for i in range(1, tp[0]+1):
        trust[tp[i]] = 1

    for i in range(m):
        party = list(map(int, input().strip().split()))
        np, party = party[0], party[1:]
        parties.append(party)
        
        for p in range(np-1):
            if party[p+1] not in edge[party[p]]:
                edge[party[p]].append(party[p+1])
                edge[party[p+1]].append(party[p])

    visited = [0] * (n+1)

    queue = deque()

    for i in range(1, n+1):
        if trust[i] == 1 and visited[i] == 0:
            queue.append(i)
            visited[i] = 1
            while queue:
                x = queue.popleft()
                for y in edge[x]:
                    if visited[y] == 0:
                        visited[y] = 1
                        trust[y] = 1
                        queue.append(y)    


    cnt = 0
    for party in parties:
        f = 0
        for p in party:
            if trust[p] == 1:
                f = 1
                break
        
        if not f:
            cnt += 1

    print(cnt)