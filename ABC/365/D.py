# WA

# !手が変わるときは常に勝ち (=> RRSRRS で詰む、できない)
# 奇数(n)回手が同じ時は、
# 奇数番目で勝つ、偶数番目で引き分け = n // 2 + 1 回勝利
# 偶数(n)回同じ時は、
# 1. 奇数目勝ち、偶数目引き分け = n//2回勝利、次の手で勝てるかは不明 (RRCPPRCP... で詰む)
# 2. 奇数目引き分け、偶数目勝ち = n//2回勝利、前の手で勝てるかは不明 (=> 起こり得ない、なぜなら1回目で引き分けるに前の手も同じ手でなければならない => 偶数にならなくなってしまう)
# ここまで、前提が崩れたのでやりなおし

# 引き分けやむなしのタイミングとは?
# 1. 複数回同じ手を出された
# 2. 引き分けになった後、それに対抗する手を出された (R vs R => S vs S)
# 1がきっかけで引き分けが起こり、2が連鎖しうる

# 先を見ないと、RRSPRSP... もしくは RRSSPRSPで詰む


N = int(input())
aoki_hands = input()


encoded_aoki_hands = []
count = 1
for i in range(N):
    if i + 1 < N and aoki_hands[i] == aoki_hands[i + 1]:
        count += 1
    else:
        encoded_aoki_hands.append((aoki_hands[i], count))
        count = 1

# for encoded_aoki_hand in encoded_aoki_hands:
