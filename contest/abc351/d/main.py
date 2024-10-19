# WA

# . => empty cell
# #, M => wall
# V => visited cell

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

def get_adjacent_cells(h, w, H, W):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_cells = []
    for dh, dw in directions:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W:
            adjacent_cells.append((nh, nw))
    return adjacent_cells

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            cells = get_adjacent_cells(h, w, H, W)
            for nh, nw in cells:
                S[nh][nw] = 'M'

def dfs(S, h, w):
    area = 0
    stack = [(h, w)]
    while stack:
        h, w = stack.pop()
        if S[h][w] == 'V':
            continue
        S[h][w] = 'V'
        area += 1
        for nh, nw in get_adjacent_cells(h, w, H, W):
            if S[nh][nw] == 'M':
                area += 1
                continue
            else:
                stack.append((nh, nw))
    return area

max_area = 1
for h in range(H):
    for w in range(W):
        if S[h][w] == '.':
            max_area = max(max_area, dfs(S, h, w))

print(max_area)
