# WA

# lv 0
# #

# lv 1
# 0 0 0
# 0 . 0
# 0 0 0

# = 0 0 0 0 . 0 0 0 0

# lv 2
# 1 1 1
# 1 . 1
# 1 1 1

# = 1 1 1 1 . 1 1 1 1


def gen_grids(num):
    grids = [['#']] # Lv.0
    for i in range(num):
        grids.append([*grids[i] *4, *('.' * (3**i)**2), *grids[i] * 4])
        print(f"{i=}, {grids[i]=}")
    return grids

def print_grids(level):
    grids = gen_grids(level)

    # print grid upper
    for row in 3**(level-1):
        print(grids[0][(3**row)*row: (3**row)(row+1)-1])

print_grids(3)
