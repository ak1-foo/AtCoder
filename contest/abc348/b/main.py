N = int(input())

positions = []
for _ in range(N):
    x, y = map(int, input().split())
    positions.append({"x": x, "y": y})


def calc_euclidean_distance(p1, p2):
    return ((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2) ** 0.5


for i in range(N):
    max_position = {"distance": -1, "index": -1}
    for j in range(N):
        if i == j:
            continue
        distance = calc_euclidean_distance(positions[i], positions[j])
        if distance > max_position["distance"]:
            max_position["distance"] = distance
            max_position["index"] = j
    print(max_position["index"] + 1)
