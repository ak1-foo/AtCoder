board = [list(input()) for _ in range(8)]

rook_row = set()
rook_col = set()

for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            rook_row.add(i)
            rook_col.add(j)

ans = (8 - len(rook_row)) * (8 - len(rook_col))
print(ans)
