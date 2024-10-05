# time over
import itertools, math

N, S, T = map(int, input().split())

lines = []
for _ in range(N):
    lines += [list(map(int, input().split()))]

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_time(mode, x1, y1, x2, y2):
    if mode == 'on':
        return get_distance(x1, y1, x2, y2) / T
    elif mode == 'off':
        return get_distance(x1, y1, x2, y2) / S

# オンになっている時間を求める
on_time = 0
for i in range(N):
    on_time += get_time('on', lines[i][0], lines[i][1], lines[i][2], lines[i][3])


order = [i for i in range(N)]
min_time = math.inf
# 線分の順番を全探索
for permutation in itertools.permutations(order):
    # 方向をビットで表現
    # 行くなら0, 戻るなら1
    for bit in range(1 << N):
        time = 0
        last_position = [0, 0]
        for i in range(N):
            # 始点に移動するまでの時間を加算
            if bit >> i & 1:
                time += get_time('off', last_position[0], last_position[1], lines[permutation[i]][2], lines[permutation[i]][3])
                last_position = [lines[permutation[i]][0], lines[permutation[i]][1]]
            else:
                time += get_time('off', last_position[0], last_position[1], lines[permutation[i]][0], lines[permutation[i]][1])
                last_position = [lines[permutation[i]][2], lines[permutation[i]][3]]

        # 最終的にかかった時間を求め、最小値を更新
        time += on_time
        min_time = min(min_time, time)

print(min_time)
