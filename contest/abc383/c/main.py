from collections import deque
import math

H, W, D = map(int, input().split())
office = [list(input()) for _ in range(H)]

distance = [[math.inf] * W for _ in range(H)]
h_positions = []
for h in range(H):
    for w in range(W):
        if office[h][w] == "H":
            h_positions.append((h, w))
            distance[h][w] = 0


def bfs_fill(h, w):
    queue = [(h, w, 0)]  # (h, w, depth)

    while queue:
        h, w, depth = queue.pop(0)
        if depth >= D:
            return
        depth += 1
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue

            if office[next_h][next_w] != "." or distance[next_h][next_w] <= depth:
                continue
            distance[next_h][next_w] = depth
            queue.append((next_h, next_w, depth))


for h_pos in h_positions:
    bfs_fill(*h_pos)

count = 0
for h in range(H):
    for w in range(W):
        if distance[h][w] <= D:
            count += 1

print(count)
