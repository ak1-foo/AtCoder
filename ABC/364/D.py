# TLE
N, Q = map(int, input().split())
an = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

for query in queries:
    distances = [abs(a - query[0]) for a in an]
    distances.sort()
    print(distances[query[1]-1])
