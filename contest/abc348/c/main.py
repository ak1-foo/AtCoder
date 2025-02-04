N = int(input())

min_taste = {}
for _ in range(N):
    taste, color = map(int, input().split())
    if color not in min_taste:
        min_taste[color] = taste
    else:
        min_taste[color] = min(min_taste[color], taste)


ans = max(min_taste.values())
print(ans)
