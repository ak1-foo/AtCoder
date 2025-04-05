N, M = map(int, input().split())

tmp = 1
ans = 1
for _ in range(M):
    tmp *= N
    ans += tmp

if ans > 10**9:
    ans = "inf"

print(ans)
