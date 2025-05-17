N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1

for a in A:
    ans *= a
    if ans >= 10**K:
        ans = 1

print(ans)
