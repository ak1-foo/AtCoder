# WA, 最小値を取れていない

N = int(input())

Mg = int(input())
G = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(Mg):
    a, b = map(int, input().split())
    a, b = a-1, b-1 # 0-indexed
    G[a][b] = 1
    G[b][a] = 1

Mh = int(input())
H = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(Mh):
    a, b = map(int, input().split())
    a, b = a-1, b-1 # 0-indexed
    H[a][b] = 1
    H[b][a] = 1

cost_list = [[] for _ in range(N-1)]
for i in range(N-1):
    cost_list[i] = list(map(int, input().split()))


cost = 0
for i in range(N):
    for j in range(N):
        if G[i][j] != H[i][j]:
            if i <= j:
                cost += cost_list[i][j-i-1]

print(cost)
