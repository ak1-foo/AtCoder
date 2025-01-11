N, D = map(int, input().split())

snakes = []
for _ in range(N):
    tickness, length = map(int, input().split())
    snakes.append({"tickness": tickness, "length": length})

for i in range(D):
    snake_weights = []
    for j in range(N):
        weight = snakes[j]["tickness"] * (snakes[j]["length"] + (i + 1))
        snake_weights.append(weight)

    ans = max(snake_weights)
    print(ans)
