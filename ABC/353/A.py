building_num = int(input())
buildings_height = list(map(int, input().split()))

ans = -1
for i, height in enumerate(buildings_height):
    if i == 0:
        continue
    if buildings_height[0] < height:
        ans = i + 1
        break

print(ans)
