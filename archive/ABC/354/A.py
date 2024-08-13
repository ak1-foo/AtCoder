takahashi_height = int(input())

plant_height = 0
day = 0

while True:
    # morning
    if takahashi_height < plant_height:
        ans = day
        break
    # midnight
    plant_height += 2 ** day
    # next day
    day += 1

print(ans)
