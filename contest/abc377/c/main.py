N, M = map(int, input().split())

ocupied = set()

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ocupied.add((x, y))

    dt = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in dt:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            ocupied.add((nx, ny))

ans = N * N - len(ocupied)
print(ans)
