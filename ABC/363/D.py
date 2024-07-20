# 0 1 2 3... 9
# 11 22 33 ... 99
# 101 111 121 131 ... 191
# 202 212 222 232 ... 292
# 303 ... 999
# 1001 1111 1221 1331 ... 1991
# 2002 2112 2222 2332 ... 2992
# 3003 ... 9999
# 10001 10101 10201 ... 10901
# 11011 11111 11211 ... 11911

# i=0 1桁: 10個
# i=1 2桁: 9個 = 1桁(0除く=9)の数
# i=2 3桁: 9*10個 = 1桁(0除く=9)の数 * 10
# i=3 4桁: 9*10個 = 2桁の数(0n除く=90)
# i=4 5桁: 2桁の数の個数 * 10
# i=5 6桁: 3桁の数の個数(0nm除く=900)
# i=6 7桁: 3桁の数の個数 * 10


# abcba と abc|cba で2セットずつ、a != 0
# 0
# 1 2 3 ... 9 を2セット(1タイプ、11タイプ) = 9*2
# 10 11 ... 19 ... 99 を2セット(121タイプ、1221タイプ) = 90*2
# 900 * 2

N = int(input())
N_tmp = N

# i は片側の数
half_digit = 0
odd_digit = True
while (True):
    # ans = 0
    if (half_digit == 0):
        N_tmp -= 1
        if (N_tmp <= 0):
            print(0)
            exit()
        half_digit += 1
        continue

    # ans = abcbaタイプ
    N_tmp -= 9 * 10**(half_digit-1)
    if (N_tmp <= 0):
        break

    # ans = abccbaタイプ
    N_tmp -= 9 * 10**(half_digit-1)
    if (N_tmp <= 0):
        odd_digit = False
        break

    half_digit += 1

N_tmp += 9 * 10**(half_digit-1)


half_ans = 10**(half_digit-1) + N_tmp -1

half_ans_str = str(half_ans)
half_ans_str_reversed = ''.join(list(reversed(half_ans_str)))

if odd_digit:
    ans = half_ans_str + half_ans_str_reversed[1:]
else:
    ans = half_ans_str + half_ans_str_reversed

print(ans)
