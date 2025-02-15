from collections import Counter
from itertools import permutations

N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]
dice = [{"num_face": d[0], "chance": Counter(d[1:])} for d in dice]

ans = 0
for d1, d2 in permutations(dice, 2):
    d1d2_max = 0
    for d1_face_num in d1["chance"]:
        if d2["chance"][d1_face_num]:
            v = (d1["chance"][d1_face_num] / d1["num_face"]) * (
                d2["chance"][d1_face_num] / d2["num_face"]
            )
            d1d2_max += v
    if d1d2_max > ans:
        ans = d1d2_max


print(ans)
