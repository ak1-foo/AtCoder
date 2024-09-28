S = [input() for _ in range(12)]

ans = 0
for i, s in enumerate(S):
    if i+1 == len(s):
        ans += 1

print(ans)
