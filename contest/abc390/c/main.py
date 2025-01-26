H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

black_square = {"left": float("inf"), "right": -1, "top": float("inf"), "bottom": -1}

for h in range(H):
    for w in range(W):
        if field[h][w] == "#":
            black_square["left"] = min(black_square["left"], w)
            black_square["right"] = max(black_square["right"], w)
            black_square["top"] = min(black_square["top"], h)
            black_square["bottom"] = max(black_square["bottom"], h)

for h in range(black_square["top"], black_square["bottom"] + 1):
    for w in range(black_square["left"], black_square["right"] + 1):
        if field[h][w] == ".":
            print("No")
            exit()

print("Yes")
