N, M = map(int, input().split())

ans = 0
same_node = 0
graph = set()
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        ans += 1
        same_node += 1
        continue
    if a > b:
        a, b = b, a
    graph.add((a, b))

ans += M - len(graph) - same_node
print(ans)
