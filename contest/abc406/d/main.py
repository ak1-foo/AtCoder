H, W, N = map(int, input().split())

row_garbage = [{"total": 0, "col": {}} for _ in range(H)]
col_garbage = [{"total": 0, "row": {}} for _ in range(W)]

for _ in range(N):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    row_garbage[x]["total"] += 1
    col_garbage[y]["total"] += 1

    if y in row_garbage[x]["col"]:
        row_garbage[x]["col"][y] += 1
    else:
        row_garbage[x]["col"][y] = 1

    if x in col_garbage[y]["row"]:
        col_garbage[y]["row"][x] += 1
    else:
        col_garbage[y]["row"][x] = 1


Q = int(input())
for _ in range(Q):
    query_type, v = map(int, input().split())
    v -= 1

    if query_type == 1:
        ans = row_garbage[v]["total"]
        for col, count in row_garbage[v]["col"].items():
            col_garbage[col]["total"] -= count
            col_garbage[col]["row"][v] -= count
            if col_garbage[col]["row"][v] == 0:
                del col_garbage[col]["row"][v]

        row_garbage[v]["total"] = 0
        row_garbage[v]["col"] = {}

    elif query_type == 2:
        ans = col_garbage[v]["total"]
        for row, count in col_garbage[v]["row"].items():
            row_garbage[row]["total"] -= count
            row_garbage[row]["col"][v] -= count
            if row_garbage[row]["col"][v] == 0:
                del row_garbage[row]["col"][v]

        col_garbage[v]["total"] = 0
        col_garbage[v]["row"] = {}

    print(ans)
