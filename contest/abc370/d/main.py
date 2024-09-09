# WA
H, W, Q = map(int, input().split())

burned_row = [[] for _ in range(H)]
burned_col = [[] for _ in range(W)]

for _ in range(Q):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1

    # 行について
    finded_flag = False
    for interval in burned_row[c]:
        # あれば、拡張
        if interval[0] <= r <= interval[1]:
            interval = [interval[0]-1, interval[1]+1]
            finded_flag = True
            break
    # なければ、新規追加
    if not finded_flag:
        burned_row[c].append([r, r])
    # 重なっているものがあれば、結合
    burned_row[c].sort()
    for i in range(len(burned_row[c])):
        for j in range(i+1, len(burned_row[c])):
            if burned_row[c][i][1] >= burned_row[c][j][0]:
                burned_row[c][i][1] = burned_row[c][j][1]
                burned_row[c].pop(j)
                break

    # 列について
    finded_flag = False
    for interval in burned_col[r]:
        # あれば、拡張
        if interval[0] <= c <= interval[1]:
            interval = [interval[0]-1, interval[1]+1]
            finded_flag = True
            break
    # なければ、新規追加
    if not finded_flag:
        burned_col[r].append([c, c])
    # 重なっているものがあれば、結合
    burned_col[r].sort()
    for i in range(len(burned_col[r])):
        for j in range(i+1, len(burned_col[r])):
            if burned_col[r][i][1] >= burned_col[r][j][0]:
                burned_col[r][i][1] = burned_col[r][j][1]
                burned_col[r].pop(j)
                break


# 0: 壁がない 1: 壁がある
grid_row = [[1] * W for _ in range(H)]
for b_r in burned_row:
    for start, end in b_r:
        for c in range(start, end+1):
            grid_row[r][c] = 0

grid_col = [[1] * W for _ in range(H)]
for b_c in burned_col:
    for start, end in b_c:
        for r in range(start, end+1):
            grid_col[r][c] = 0

wall_num = 0
for r in range(H):
    for c in range(W):
        if grid_row[r][c] == 1 and grid_col[r][c] == 1:
            wall_num += 1


print(wall_num)




# TLE
# # 0: 壁がない 1: 壁がある
# grid = [[1] * W for _ in range(H)]
#
# for _ in range(Q):
#     r, c = map(int, input().split())
#     # 0-indexedにする
#     r, c = r - 1, c - 1
#
#     # 投下による破壊
#     if grid[r][c] == 1:
#         grid[r][c] = 0
#         continue
#
#     r_center, c_center = r, c
#     # 爆発による破壊
#     # 左
#     r, c = r_center, c_center
#     while c >= 0:
#         if grid[r][c] == 1:
#             grid[r][c] = 0
#             break
#         else:
#             c -= 1
#
#     # 右
#     r, c = r_center, c_center
#     while c < W:
#         if grid[r][c] == 1:
#             grid[r][c] = 0
#             break
#         else:
#             c += 1
#
#     # 上
#     r, c = r_center, c_center
#     while r >= 0:
#         if grid[r][c] == 1:
#             grid[r][c] = 0
#             break
#         else:
#             r -= 1
#
#     # 下
#     r, c = r_center, c_center
#     while r < H:
#         if grid[r][c] == 1:
#             grid[r][c] = 0
#             break
#         else:
#             r += 1
#
# num_wall = sum(row.count(1) for row in grid)
# print(num_wall)
#
