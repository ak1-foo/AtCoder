from collections import deque

H, W, K = map(int, input().split())
field = [list(input()) for _ in range(H)]

# 最大11手、移動は4方向なので、4^11 = 4194304通り
# スタート地点は10*10=100通り
# これは多分全探索可能
# 深さ優先探索で探索する
ans = 0
Q = deque()

def dfs(x, y, move_count):
    if x < 0 or x >= H or y < 0 or y >= W:
        return
    if field[x][y] == '#':
        return
    if visited[x][y]:
        return

    if move_count == K:
        global ans
        ans += 1
        return

    visited[x][y] = True

    dc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in dc:
        nx = x + dx
        ny = y + dy
        dfs(nx, ny, move_count+1)

    visited[x][y] = False

for i in range(H):
    for j in range(W):
        visited = [[False] * W for _ in range(H)]
        dfs(i, j, 0)
print(ans)
