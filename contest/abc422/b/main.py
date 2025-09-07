H, W = map(int, input().split())

stage = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        next_black_count = 0
        if stage[h][w] != "#":
            continue
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if stage[nh][nw] == "#":
                    next_black_count += 1

        if next_black_count != 2 and next_black_count != 4:
            print("No")
            exit()

print("Yes")
