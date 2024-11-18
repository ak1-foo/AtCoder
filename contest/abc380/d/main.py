S = input()
Q = int(input())
K = list(map(int, input().split()))
K = [k - 1 for k in K]

borders = [len(S)]
for i in range(60 - 1):  # 10^18 < 2^60
    borders.append(borders[-1] * 2)


def reverse_case(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()


for k in K:
    # 大文字小文字の判定
    count = 0
    for b in reversed(borders):
        if k >= b:
            k -= b
            count += 1

    # 文字の取得
    c = S[k]
    if count % 2 == 1:
        c = reverse_case(c)
    print(c, end=" ")
