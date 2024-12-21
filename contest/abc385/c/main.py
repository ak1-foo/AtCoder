N = int(input())
H = list(map(int, input().split()))

bildings = {h: [] for h in set(H)}
for i, h in enumerate(H):
    bildings[h].append(i)

ans = 1
for b in bildings.values():
    if len(b) < 2:
        continue
    len_seq = [{} for _ in range(len(b))]
    for i in range(1, len(b)):
        for j in range(i):
            diff = b[i] - b[j]
            if diff in len_seq[j]:
                len_seq[i][diff] = len_seq[j][diff] + 1
            else:
                len_seq[i][diff] = 2

            ans = max(ans, len_seq[i][diff])

print(ans)
