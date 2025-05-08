N, M = map(int, input().split())

if N != M:
    print("No")
    exit()


graph = [[] for _ in range(N)]
for i in range(N):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    graph[A].append(B)
    graph[B].append(A)

for i in range(N):
    if len(graph[i]) != 2:
        print("No")
        exit()

start = 0
next = start
visited = [False] * N
visited[next] = True

for _ in range(N - 1):
    prev = next
    next = graph[prev][0]
    if visited[next]:
        next = graph[prev][1]
        if visited[next]:
            print("No")
            exit()

    visited[next] = True

if all(visited):
    if graph[next][0] == start or graph[next][1] == start:
        print("Yes")
    else:
        print("No")
