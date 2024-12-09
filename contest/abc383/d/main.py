# 約数をちょうど9個持つ数nを求める
# n = a^2 * b^2 = (a*b)^2 となる数を求める。ただし、a, b は異なる素数
# または、n = a^8 となる数を求める。ただし、a は素数
import math

# 入力
N = int(input())

# N の平方根や 8乗根
sqrt_n = int(N**0.5)
sqrt_8_n = int(N**0.125)


# エラトステネスの篩で素数リストを作成
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):  # i * i から始める
                is_prime[j] = False
    return is_prime


# 素数リストの作成
is_prime = prime(sqrt_n)
primes = [i for i in range(sqrt_n + 1) if is_prime[i]]

count = 0

# n = a^2 * b^2 をカウント
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):  # 異なる素数の組み合わせ
        if primes[i] * primes[j] > sqrt_n:
            break
        if primes[i] * primes[j] ** 2 <= N:
            count += 1

# n = a^8 をカウント
for p in primes:
    if p**8 > N:
        break
    count += 1

# 結果を出力
print(count)
