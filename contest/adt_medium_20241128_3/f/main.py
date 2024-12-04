# WA
N = int(input())

graph_G = [[] for _ in range(N)]
graph_H = [[] for _ in range(N)]

MG = int(input())
for _ in range(MG):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph_G[a].append(b)
    graph_G[b].append(a)

MH = int(input())
for _ in range(MH):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph_H[a].append(b)
    graph_H[b].append(a)

costs = [[0] * N for _ in range(N)]
for i in range(N - 1):
    cost = list(map(int, input().split()))
    for j in range(i + 1, N):
        costs[i][j] = cost[j - i - 1]
        costs[j][i] = cost[j - i - 1]

ans = 0
for i in range(N):
    for j in range(N):
        if i in graph_G[i] and j not in graph_H[i]:
            ans += costs[i][j]
        elif i not in graph_G[i] and j in graph_H[i]:
            ans += costs[i][j]


ans = ans // 2
print(ans)
