S, T = input().split()

for c in range(1, len(S)):
    for w in range(c, len(S)):
        sepalate = []
        for i in range(int(len(S)/w)+1): # w文字ごとに区切る
            if (w == 1 and i == int(len(S)/w)):
                break
            else:
                sepalate.append(S[w*i : w*(i+1)])

        # c文字目を抜き出して文字列にする
        tmp_ans = ''
        for i in range(len(sepalate)):
            if (len(sepalate[i]) < c): # 分割部分がc文字より小さかったら辞める
                break
            tmp_ans += sepalate[i][c-1]

        if (tmp_ans == T):
            print('Yes')
            exit()

print('No')
