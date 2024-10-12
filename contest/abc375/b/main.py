def calc_euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N = int(input())
position = [tuple(map(int, input().split())) for _ in range(N)]

sum_distance = calc_euclidean_distance(0, 0, position[0][0], position[0][1])
for i in range(N-1):
    sum_distance += calc_euclidean_distance(position[i][0], position[i][1], position[i+1][0], position[i+1][1])
sum_distance += calc_euclidean_distance(position[-1][0], position[-1][1], 0, 0)

print(sum_distance)
