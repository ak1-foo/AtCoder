# WA

N = int(input())

# 2**59 = 5.7646075e+17
# 2**60 = 1.1529215e+18
# よって 0 < a < 60
# 0 < b < 10**9

# a==1, a==2 のときのみ考えれば良い
# a==3 のとき、X = 2**3 * b**2 = 2**1 * (2*b)**2

ans = 0
for a in range(1, 2 + 1):

    # incorrect
    b_max = int((N / 2**a) ** 0.5)
    # answer is below
    # b_max = isqrt((N // 2**a))

    ans += b_max

print(ans)
