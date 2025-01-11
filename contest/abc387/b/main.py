X = int(input())

base = [i for i in range(1, 10)]

grid = []
for b1 in base:
    for b2 in base:
        grid.append(b1 * b2)

ans = 0
for g in grid:
    if g != X:
        ans += g

print(ans)
