N, K = map(int, input().split())
S = input()

embed = []
count = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        count += 1
    else:
        embed.append((S[i - 1], count))
        count = 1
embed.append((S[-1], count))

count = 0
for i, e in enumerate(embed):
    if e[0] == "1":
        count += 1

    if count == K:
        embed[i - 1], embed[i] = embed[i], embed[i - 1]

print("".join([e[0] * e[1] for e in embed]))
