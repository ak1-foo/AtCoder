H, W, X, Y = map(int, input().split())
field = [list(input()) for _ in range(H)]
T = list(input())


santa_pos = {"row": X - 1, "col": Y - 1}
visited_house = set()

for t in T:
    r, c = santa_pos["row"], santa_pos["col"]
    if t == "U":
        nr, nc = r - 1, c
    elif t == "D":
        nr, nc = r + 1, c
    elif t == "L":
        nr, nc = r, c - 1
    elif t == "R":
        nr, nc = r, c + 1

    if 0 <= nr < H and 0 <= nc < W and field[nr][nc] != "#":
        santa_pos["row"] = nr
        santa_pos["col"] = nc
        if field[nr][nc] == "@":
            visited_house.add((nr, nc))

ans = list(santa_pos.values())
ans = [ans[0] + 1, ans[1] + 1]
ans.append(len(visited_house))
print(*ans)
