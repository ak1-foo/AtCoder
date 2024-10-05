import itertools, math

N = int(input())
K = list(map(int, input().split()))

n = [i for i in range(N)]

group_min = math.inf
group = [0, 0]

for bit in range(2 << N):
    group = [0, 0]
    for i in range(N):
        group[bit >> i & 1] += K[i]
    group_min = min(group_min, max(group))

print(group_min)
