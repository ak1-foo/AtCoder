n, y = map(int, input().split())

## slow code
# for num10000 in range(n):
#     for num5000 in range(n):
#         for num1000 in range(n):
#             if (10000 * num10000 + 5000 * num5000 + 1000 * num1000 == y
#                 and num10000 + num5000 + num1000 == n):
#                 print(f'{num10000} {num5000} {num1000}')
#                 exit()

# print('-1 -1 -1')

# まず最小の札にする
num10000 = int(y / 10000)
num5000 = int((y - 10000*num10000) / 5000)
num1000 = int((y- 10000*num10000 - 5000*num5000) / 1000)


# 最小でOKなら終了
if (n == (num10000 + num5000 + num1000)):
    print(f'{num10000} {num5000} {num1000}')
    exit()

# 足りない枚数を考える
diff_num = n - (num10000 + num5000 + num1000)
if (diff_num < 0):
    print('-1 -1 -1')
    exit()


# 10000 * 1 => 5000 * 2 で、1枚増える
# 10000円が足りるのであれば、必要分変えて、終了
if (diff_num <= num10000):
    num5000 += diff_num * 2
    num10000 -= diff_num
    print(f'{num10000} {num5000} {num1000}')
    exit()


# 足りなければ、可能な限り10000円を5000円に変える
num5000 += num10000 * 2
num10000 = 0


# 足りない枚数を考える
diff_num = n - (num10000 + num5000 + num1000)
if (diff_num < 0):
    print('-1 -1 -1')
    exit()


# 5000 * 1 => 1000 * 5 で、4枚増える
# 5000*1 => 10000*2にして、4枚の倍数分足りないように調整する

## 3 mod 4 足りないとき、
#if (diff_num % 4 == 3):
#    num5000 -= 2
#    num10000 += 1
## 2 mod 4 足りないとき、
#if (diff_num % 4 == 2):
#    num5000 -= 4
#    num10000 += 2
## 1 mod 4 足りないとき、
#if (diff_num % 4 == 1):
#    num5000 -= 6
#    num10000 += 3

## => つまり
if (diff_num % 4 != 0):
    if (num5000 < 2 * (4 - (diff_num) % 4)):
        print('-1 -1 -1')
        exit()

    num10000 += (4 - (diff_num % 4))
    num5000 -= 2 * (4 - (diff_num % 4))



# 足りない枚数を考える、このとき4の倍数なはず
diff_num = n - (num10000 + num5000 + num1000)
if (diff_num < 0):
    print('-1 -1 -1')
    exit()


# 5000 * 1 => 1000 * 5 で、4枚増える
if (diff_num <= num5000 * 4):
    num1000 += int((diff_num / 4) * 5)
    num5000 -= int(diff_num / 4)
    print(f'{num10000} {num5000} {num1000}')
    exit()


# これでもだめなら無理
print('-1 -1 -1')
