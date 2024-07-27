height, width = map(int, input().split())
start_height, start_width = map(int, input().split())

grid = [input() for _ in range(height)]

moves = input()

# 0からに補正
current_x = start_width - 1
current_y = start_height - 1

for move in moves:
    if move == 'L':
        if (current_x == 0): # wall
            continue
        elif (grid[current_y][current_x-1] == '#'): # filled
            continue
        else: # move
            current_x -= 1

    if move == 'R':
        if (current_x == width-1): # wall
            continue
        elif (grid[current_y][current_x+1] == '#'): # filled
            continue
        else: # move
            current_x += 1

    if move == 'U':
        if (current_y == 0): # wall
            continue
        elif (grid[current_y-1][current_x] == '#'): # filled
            continue
        else: # move
            current_y -= 1

    if move == 'D':
        if (current_y == height-1): # wall
            continue
        elif (grid[current_y+1][current_x] == '#'): # filled
            continue
        else: # move
            current_y += 1


# 1からに戻す
current_y += 1
current_x += 1

# 出力
print(current_y, current_x)
