N, M = map(int, input().split())

graph = [[] for _ in range(N)]
weights = [[None] * N for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    weights[a - 1][b - 1] = w
    weights[b - 1][a - 1] = w


# 0からN-1へのすべての単純パスを列挙
start = 0
goal = N - 1
stack = [(start, [start])]
paths = []
while stack:
    node, path = stack.pop()
    if node == goal:
        paths.append(path)
        continue
    for neighbor in graph[node]:
        if neighbor not in path:
            stack.append((neighbor, path + [neighbor]))

# 各パスについてXORを計算
ans = float("inf")
for path in paths:
    if len(path) < 2:
        continue
    cost = weights[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        cost ^= weights[path[i]][path[i + 1]]

    ans = min(ans, cost)

print(ans)
