# WA

# 全探索可能
# 木を下からまとめていくイメージで

from itertools import permutations
from collections import defaultdict

A = [list(map(int, input().split())) for _ in range(3)]


def recursive_defaultdict():
    return defaultdict(recursive_defaultdict)


winner = recursive_defaultdict()
index = [(i, j) for i in range(3) for j in range(3)]

for p in permutations(index):
    first_row = {0: 0, 1: 0, 2: 0}
    first_col = {0: 0, 1: 0, 2: 0}
    first_score = 0
    second_row = {0: 0, 1: 0, 2: 0}
    second_col = {0: 0, 1: 0, 2: 0}
    second_score = 0
    for i, pos in enumerate(p):
        if i % 2 == 0:
            first_score += A[pos[0]][pos[1]]
            first_row[pos[0]] += 1
            first_col[pos[1]] += 1
            if first_row[pos[0]] == 3 or first_col[pos[1]] == 3:
                winner[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]] = "First"
                break
        else:
            second_score += A[pos[0]][pos[1]]
            second_row[pos[0]] += 1
            second_col[pos[1]] += 1
            if second_row[pos[0]] == 3 or second_col[pos[1]] == 3:
                winner[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]] = "Second"
                break

    if first_score > second_score:
        winner[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]] = "First"
    else:
        winner[p[0]][p[1]][p[2]][p[3]][p[4]][p[5]][p[6]][p[7]][p[8]] = "Second"

for p in permutations(index)[:-1]:
    # まとめる
    # やってられない
