# WA, TLE

height, width = map(int, input().split())
grid = [list(input()) for _ in range(height)]

for r in range(height):
    for c in range(width):
        if grid[r][c] == "S":
            start_pos = (r, c)
        elif grid[r][c] == "T":
            goal_pos = (r, c)

medicine_num = int(input())
medicines = []
for i in range(medicine_num):
    row, col, energy = map(int, input().split())
    row, col = row - 1, col - 1
    medicines.append((row, col, energy))
    grid[row][col] = i

if grid[start_pos[0]][start_pos[1]] == "S":
    print("No")
    exit()

route_graph = {}
for i in range(medicine_num):
    route_graph[i] = set()


def dfs(start_pos, start_idx, energy):
    if energy <= 0:
        return

    stack = [(start_pos[0], start_pos[1], energy)]
    visited = [[False] * width for _ in range(height)]
    while stack:
        r, c, e = stack.pop()
        if visited[r][c]:
            continue
        visited[r][c] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + dr < height and 0 <= c + dc < width:
                if grid[r + dr][c + dc] == "#":
                    continue
                if grid[r + dr][c + dc] == "T":
                    route_graph[start_idx].add("T")
                    continue
                if type(grid[r + dr][c + dc]) == int:
                    route_graph[start_idx].add(grid[r + dr][c + dc])
                    if e > 1:
                        stack.append((r + dr, c + dc, e - 1))

                if grid[r + dr][c + dc] == ".":
                    if e > 1:
                        stack.append((r + dr, c + dc, e - 1))


for i in range(medicine_num):
    dfs(medicines[i][0:2], i, medicines[i][2])

visited = [False] * medicine_num
stack = [grid[start_pos[0]][start_pos[1]]]
while stack:
    node = stack.pop()
    if node == "T":
        print("Yes")
        exit()
    if type(node) == int and not visited[node]:
        visited[int(node)] = True
        stack += route_graph[int(node)]

print("No")
