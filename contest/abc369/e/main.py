# WA
N, M = map(int, input().split())

G = []
for _ in range(M):
    g = list(map(int, input().split()))
    # 0-indexed
    g[0] -= 1
    g[1] -= 1
    G.append(g)

Q = int(input())
    