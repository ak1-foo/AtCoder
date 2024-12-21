# TLE
# orderd set を使えば間に合うらしい

from collections import defaultdict

N, M, Sx, Sy = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
houses_dict_x_base = defaultdict(set)
houses_dict_y_base = defaultdict(set)
for house in houses:
    houses_dict_x_base[house[0]].add(house[1])
    houses_dict_y_base[house[1]].add(house[0])

count = 0
for _ in range(M):
    direction, distance = input().split()
    distance = int(distance)

    remove_houses = []
    if direction == "U":
        nx, ny = Sx, Sy + distance
        if Sx in houses_dict_x_base:
            for i, y in enumerate(houses_dict_x_base[Sx]):
                if Sy <= y <= ny:
                    remove_houses.append((Sx, y))
                    count += 1

    elif direction == "D":
        nx, ny = Sx, Sy - distance
        if Sx in houses_dict_x_base:
            for i, y in enumerate(houses_dict_x_base[Sx]):
                if ny <= y <= Sy:
                    remove_houses.append((Sx, y))
                    count += 1

    elif direction == "L":
        nx, ny = Sx - distance, Sy
        if Sy in houses_dict_y_base:
            for i, x in enumerate(houses_dict_y_base[Sy]):
                if nx <= x <= Sx:
                    remove_houses.append((x, Sy))
                    count += 1

    elif direction == "R":
        nx, ny = Sx + distance, Sy
        if Sy in houses_dict_y_base:
            for i, x in enumerate(houses_dict_y_base[Sy]):
                if Sx <= x <= nx:
                    remove_houses.append((x, Sy))
                    count += 1

    for house in remove_houses:
        houses_dict_x_base[house[0]].remove(house[1])
        houses_dict_y_base[house[1]].remove(house[0])

    Sx, Sy = nx, ny

ans = (Sx, Sy, count)
print(*ans)
