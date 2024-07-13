num_pair = int(input())
condition_LR = [list(map(int, input().split())) for _ in range(num_pair)]

# 最小値をデフォルトの値にする
ans_list = [r[0] for r in condition_LR]
current_score = sum(ans_list)

# きれいに出力して終了
def print_ans(list):
    print('Yes')
    for i in list:
        print(i, end=' ')
    print('')
    exit()

# 各要素を増やしていき、0になったら終了
for i in range(num_pair):
    if (current_score == 0):
        print_ans(ans_list)

    if (current_score < 0):
        diff_score = - (current_score)
        width = condition_LR[i][1] - condition_LR[i][0]
        if (width >= diff_score):
            ans_list[i] = condition_LR[i][0] + diff_score
            print_ans(ans_list)
        else:
            ans_list[i] = condition_LR[i][1]
            current_score += width

print('No')
