# WA
from collections import defaultdict

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def dfs(graph, start, seen, finished):
    stack = []
    history = []  # 探索履歴
    parent = {}  # 親情報を記録する辞書 (戻り道を防ぐため)

    stack.append(start)

    while stack:
        v = stack.pop()

        if v not in seen:
            seen.add(v)
            history.append(v)

            for v2 in graph[v]:
                if finished[v2]:  # 探索済みの頂点はスキップ
                    continue

                if v2 in seen and v2 not in finished:
                    # サイクル検出
                    cycle = []
                    while history:
                        node = history.pop()
                        cycle.append(node)
                    cycle.reverse()
                    return cycle

                # スタックに追加し、親情報を記録
                if v2 not in parent:
                    parent[v2] = v
                    stack.append(v2)

        finished[v] = True  # 帰りがけ時に探索終了をマーク

    return None


uf = UnionFind(N)
for i in range(N):
    for j in graph[i]:
        uf.union(i, j)

seen = set()
finished = [False] * N

for v in range(N):
    if v not in seen:
        cycle = dfs(graph, v, seen, finished)
        if cycle:
            print("サイクル検出:", cycle)
            break
else:
    print("サイクルは存在しません。")
