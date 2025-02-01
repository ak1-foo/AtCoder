# WA, TLE

N, W = map(int, input().split())

col = [[] for _ in range(W)]

for i in range(N):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    col[x].append({"index": i, "y": y})

vanish_times = [float("inf") for _ in range(N)]
prev_vanish_time = -1
while not any(len(c) == 0 for c in col):
    bottom = []
    for c in col:
        if len(c) > 0:
            bottom.append(c.pop(0))

    vanish_time = max(prev_vanish_time + 2, max(b["y"] for b in bottom) + 1)
    for b in bottom:
        vanish_times[b["index"]] = vanish_time

    prev_vanish_time = vanish_time


Q = int(input())
for _ in range(Q):
    t, block = map(int, input().split())
    block -= 1
    if t < vanish_times[block]:
        print("Yes")
    else:
        print("No")
