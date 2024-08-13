N = int(input())
An = list(map(int, input().split()))
Wn = list(map(int, input().split()))

cost = 0

# 初期化
situation_dict = {}
#for i in range(1, N+1):
#    situation_dict[i] = []
for i in range(1, N+1):
    situation_dict[i] = 0


#for i in range(N):
#   situation_dict[An[i]] = situation_dict[An[i]] + [Wn[i]]

# すでに入ってる値より大きければ入れ替え、小さければ移動、つまりコスト増
# コスト計算のみなので、移動先は気にしないで良い
for i in range(N):
    if situation_dict[An[i]] == 0:
        situation_dict[An[i]] = Wn[i]
    elif situation_dict[An[i]] < Wn[i]:
        cost += situation_dict[An[i]]
        situation_dict[An[i]] = Wn[i]
    else:
        cost += Wn[i]


## 分配
#for i in range(1, N+1): # 各箱に対して
#    #while len(situation_dict[An[i]]) > 1: # 残り1つになるまでやる
#    #    cost += situation_dict[An[i]].pop(situation_dict[An[i]].index(min(situation_dict[An[i]]))) # 1つ取り出す
#    if (len(situation_dict[i]) >= 2):
#        cost += (sum(situation_dict[i])-max(situation_dict[i]))

print(cost)
