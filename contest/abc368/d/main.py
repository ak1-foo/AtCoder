# TLE

from collections import deque
import itertools

N, K = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    
leave_nodes = list(map(int, input().split()))
leave_nodes = [node-1 for node in leave_nodes]

# 1つのノードしかない場合は、それだけ残して終了
if len(leave_nodes) == 1:
    print(1)
    exit()

# 幅優先探索で、1つ目のノードから2つ目以降の各ノードまでの最短の経路で通ったnodeのリストを求める
def bfs(start, goal):
    q = deque()
    q.append(start)
    dist = [-1] * N
    dist[start] = 0
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    path = []
    v = goal
    while v != start:
        path.append(v)
        for nv in g[v]:
            if dist[nv] == dist[v] - 1:
                v = nv
                break
    path.append(start)
    return path

path = []
for i, node in enumerate(leave_nodes):
    if i == 0:
        continue
    if node in list(itertools.chain.from_iterable(path)):
        continue
    path += [bfs(leave_nodes[0], node)]

ans = len(set(itertools.chain.from_iterable(path)))
print(ans)