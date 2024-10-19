N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)

def bfs(s):
    q = [(s, 0)] # (node, distance)
    visited = [False] * N
    visited[s] = True
    while q:
        node, dist = q.pop(0)
        for next_node in G[node]:
            if next_node == s:
                return dist + 1
            if visited[next_node]:
                continue
            visited[next_node] = True
            q.append((next_node, dist+1))

    return -1

print(bfs(0))
