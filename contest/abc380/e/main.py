# WA

N, Q = map(int, input().split())

color_num = [1 for _ in range(N)]

color_map = []
for i in range(N):
    color_map.append({"color": i, "location": [(i, i)], "num": 1})

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x, c = query[1:]
        x, c = x - 1, c - 1
        # ?
        #

    else:
        c = query[1]
        c = c - 1
        print(color_num[c])
