from collections import deque

def solution(n, edge):
    e = {i:[] for i in range(1,n+1)}
    for a, b in edge:
        e[a].append(b)
        e[b].append(a)
    
    distances = [float('inf') for _ in range(n+1)]
    distances[1] = 0
    q = deque()
    q.append([1, 0])
    
    while q:
        c, cnt = q.popleft()
        
        for d in e[c]:
            if distances[d] > cnt + 1:
                distances[d] = cnt + 1
                q.append([d, cnt+1])    
    
    m = max(distances[1:])
    answer = distances.count(m)
    return answer