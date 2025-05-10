# WA
import math

A, B, C, D = map(int, input().split())

apple = A
orange = B
banana = C
grape = D

magic_number = 998244353

# <りんごゾーン> <バナナぶどうゾーン>
# オレンジはぶどうの前ならどこでも可能


# 以下を高速化する
# ans = 0
## <バナナぶどうゾーン>において、最初に出てくるブドウの位置を i とする
# for i in range(banana + 1):
#    banana_grape_zone_pattern = (
#        math.comb(banana + grape - i - 1, grape - 1) % magic_number
#    )
#    until_first_grape_space = apple + i + 1
#    orange_pattern = (
#        math.comb(orange + until_first_grape_space - 1, orange) % magic_number
#    )
#    ans += (banana_grape_zone_pattern * orange_pattern) % magic_number
#    ans %= magic_number
#
# print(ans)

factorial = [1] * (4 * (10**6) + 1)
for i in range(1, 10**6 + 1):
    factorial[i] = (factorial[i - 1] * i) % magic_number


def fast_comb(n, k):
    if n < k:
        return 0
    if n == k or k == 0:
        return 1
    return (
        factorial[n]
        * pow(factorial[k], -1, magic_number)
        * pow(factorial[n - k], -1, magic_number)
    ) % magic_number


ans = 0
# <バナナぶどうゾーン>において、最初に出てくるブドウの位置を i とする
for i in range(banana + 1):
    banana_grape_zone_pattern = (
        fast_comb(banana + grape - i - 1, grape - 1) % magic_number
    )
    until_first_grape_space = apple + i + 1
    orange_pattern = (
        fast_comb(orange + until_first_grape_space - 1, orange) % magic_number
    )
    ans += (banana_grape_zone_pattern * orange_pattern) % magic_number
    ans %= magic_number

print(ans)
