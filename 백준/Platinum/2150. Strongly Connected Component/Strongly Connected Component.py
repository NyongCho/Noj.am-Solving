import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

V, E = map(int, input().split())

edges = [[] for _ in range(V + 1)]
stack = []
parent = [0 for _ in range(V + 1)]
completed = [False for _ in range(V + 1)]
scc = []

for _ in range(E):
    a, b = map(int, input().split())
    edges[a].append(b)
    
for edge in edges:
    edge.sort()


id = 1
def function(v):
    global stack, parent, completed, scc, id
    stack.append(v)
    parent[v] = id
    id += 1
    
    p = parent[v]
    for edge in edges[v]:
        if parent[edge] == 0:
            p = min(p, function(edge))
        elif not completed[edge]:
            p = min(p, parent[edge])
    
    if parent[v] == p:
        scc.append([])
        while True:
            node = stack.pop()
            completed[node] = True
            scc[-1].append(node)
            if node == v:
                scc[-1].sort()
                scc[-1].append(-1)
                break

    return p

for i in range(1, V + 1):
    if parent[i] == 0:
        function(i)

scc.sort()

print(len(scc))
for component in scc:
    print(*component)