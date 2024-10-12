import math

S = input()

encoded_S = {}
for index, s in enumerate(S):
    if s not in encoded_S:
        encoded_S[s] = []
    encoded_S[s].append(index)

ans = 0
for indexes in encoded_S.values():
    n = len(indexes)
    total_sum = sum(indexes)
    for i in range(n):
        ans += indexes[i] * (2 * i - n + 1)

    ans -= math.comb(n, 2)
print(ans)
