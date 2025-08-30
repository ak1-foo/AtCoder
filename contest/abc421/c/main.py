N = int(input())
S = list(input())

# abab.. か baba.. にしたい

a_index = []
for i, s in enumerate(S):
    if s == "A":
        a_index.append(i)

abab_score = sum([abs(a_idx - i * 2) for i, a_idx in enumerate(a_index)])
baba_score = sum([abs(a_idx - (i * 2 + 1)) for i, a_idx in enumerate(a_index)])

ans = min(abab_score, baba_score)
print(ans)
