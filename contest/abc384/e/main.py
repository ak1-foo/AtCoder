from sortedcontainers import SortedList

H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P, Q = P - 1, Q - 1

S = [list(map(int, input().split())) for _ in range(H)]

power_cur = S[P][Q]
reachable = SortedList(key=lambda x: x[0])
targeted = [[False] * W for _ in range(H)]
targeted[P][Q] = True

for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    nr, nc = P + dr, Q + dc
    if 0 <= nr < H and 0 <= nc < W:
        reachable.add((S[nr][nc], (nr, nc)))
        targeted[nr][nc] = True

while reachable:
    power, (r, c) = reachable.pop(0)
    if power_cur / X <= power:
        break
    power_cur += power
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and not targeted[nr][nc]:
            reachable.add((S[nr][nc], (nr, nc)))
            targeted[nr][nc] = True


print(power_cur)
