H, W, D = map(int, input().split())
office = [list(input()) for _ in range(H)]


def calc_manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


best_count = 0
# もっと綺麗にできるはず…
for h1 in range(H):
    for w1 in range(W):
        for h2 in range(H):
            for w2 in range(W):
                if h1 == h2 and w1 == w2:
                    continue
                if office[h1][w1] == "#" or office[h2][w2] == "#":
                    continue

                count = 0
                for i in range(H):
                    for j in range(W):
                        if office[i][j] == "#":
                            continue
                        if (
                            min(
                                calc_manhattan_distance((h1, w1), (i, j)),
                                calc_manhattan_distance((h2, w2), (i, j)),
                            )
                            <= D
                        ):
                            count += 1

                best_count = max(best_count, count)

print(best_count)
