from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# find exit
exit = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            exit.append((i, j))

visit = [[False] * W for _ in range(H)]

# bfs
queue = deque()
for e in exit:
    queue.append({"pos": e, "prev_direction": None})

while queue:
    current = queue.popleft()
    pos = current["pos"]
    prev_direction = current["prev_direction"]

    # mark nearest exit direction
    if S[pos[0]][pos[1]] == ".":
        if prev_direction == (-1, 0):
            S[pos[0]][pos[1]] = "v"
        elif prev_direction == (1, 0):
            S[pos[0]][pos[1]] = "^"
        elif prev_direction == (0, -1):
            S[pos[0]][pos[1]] = ">"
        elif prev_direction == (0, 1):
            S[pos[0]][pos[1]] = "<"

    # add neighbors to queue
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if (
            0 <= new_pos[0] < H
            and 0 <= new_pos[1] < W
            and not visit[new_pos[0]][new_pos[1]]
            and S[new_pos[0]][new_pos[1]] != "#"
            and S[new_pos[0]][new_pos[1]] != "E"
        ):
            visit[new_pos[0]][new_pos[1]] = True
            queue.append({"pos": new_pos, "prev_direction": (dx, dy)})

for i in range(H):
    print("".join(S[i]))
