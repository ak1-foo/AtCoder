Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

def which_brick(x, y):
    if ((x+y) % 2) == 0:
        return 'left'
    else:
        return 'right'

# 点を中央に寄せる
def center_xy(x, y):
    if which_brick(x, y) == 'left':
        return x+0.5, y
    else:
        return x-0.5, y

# x軸を/2すると、囲碁の目になる？
#def calc_ortho_distance(start_x, start_y, goal_x, goal_y):
#    return abs(goal_x - start_x) + abs(goal_y - start_y)
#
#cost = calc_ortho_distance(Sx//2, Sy, Tx//2, Ty)
#print(cost)

# 7/23 12:00
# 9min = (6min 発表)+(3min 質問)
# 人間の認知情報処理の特徴を考慮した上で、親密なパートナーとなるロボットもしくはエージェントを提案してください。
# 日常生活の中で個人が所有することを想定したパーソナルロボット

# ヒント:
#   - 注意や記憶の容量の限界
#   - フォールスメモリ、認知バイアス、情動による影響、印象形成、確証バイアス
# - 能力を補うか、精神を満足させるか
