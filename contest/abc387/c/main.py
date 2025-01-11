# WA
# 大きい桁のときうまくいかない

L, R = map(int, input().split())

# 先頭の桁がNのとき、他の下の桁で使っていい数字は
# N=1のとき、0
# N=2のとき、0, 1
# N=3のとき、0, 1, 2
# N=Nのとき、0, 1, 2, ..., N-1

# snake_num_table[桁数][先頭の桁]= (先頭の桁)9..9 以下のヘビ数の個数
snake_num_table = []
snake_num_table.append([0] * 10)
snake_num_table.append([0] * 10)
for i in range(2, 19):  # 10 <= 10^18
    append_list = [0]  # 先頭の桁が0のときはヘビ数ではない
    cur_value = snake_num_table[-1][-1]
    for j in range(1, 10):
        cur_value += j ** (i - 1)
        append_list.append(cur_value)
    snake_num_table.append(append_list)


def count_snake_num_smaller_than_or_equal(n):
    if n < 10:
        return 0
    n_str = list(str(n))
    head = int(n_str[0])

    # (初めの桁)0..0 以上 n 以下のヘビ数の個数
    for i in range(1, len(n_str)):
        if int(n_str[i]) >= head:
            n_str[i] = str(head - 1)

    result = 0
    if head == 1:
        result += snake_num_table[len(n_str) - 1][9] + 1
    else:
        result += int("".join(n_str[1:]), head) + 1
        result += snake_num_table[len(n_str)][head - 1]

    return result


ans = count_snake_num_smaller_than_or_equal(R) - count_snake_num_smaller_than_or_equal(
    L
)

is_L_snake = True
str_L = str(L)
for i in range(1, len(str_L)):
    if str_L[i] >= str_L[0]:
        is_L_snake = False
        break

if is_L_snake:
    ans += 1

print(ans)
