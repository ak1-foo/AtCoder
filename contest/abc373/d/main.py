import math

N, M = map(int, input().split())

weight_edge = [math.inf] * N
weight_arc = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    weight_arc[u].append((v, w, 'forward'))
    weight_arc[v].append((u, w, 'backward'))

# スタックを使ってdfsを実装
def dfs(u):
    # 離れ小島の最初の頂点の重みは0
    if weight_edge[u] == math.inf:
        weight_edge[u] = 0
    stack = [u]
    while stack:
        u = stack.pop()
        for v, w, direct in weight_arc[u]:
            if weight_edge[v] == math.inf:
                if direct == 'forward':
                    weight_edge[v] = weight_edge[u] + w
                elif direct == 'backward':
                    weight_edge[v] = weight_edge[u] - w
                stack.append(v)

    return

# すべての頂点を訪問する
for i in range(N):
    if weight_edge[i] == math.inf:
        dfs(i)

print(*weight_edge)
