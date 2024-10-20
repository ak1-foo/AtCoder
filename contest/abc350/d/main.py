import math

N, M = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        else:
            if self.parents[root_x] > self.parents[root_y]:
                root_x, root_y = root_y, root_x
            self.parents[root_x] += self.parents[root_y]
            self.parents[root_y] = root_x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def each_size(self):
        return [-x for x in self.parents if x < 0]

uf = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

ans = -M
for size in uf.each_size():
    ans += math.comb(size, 2)

print(ans)
