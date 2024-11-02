# TLE
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for s in range(N):
    for g in range(N):
        ans += sum(A[s:g+1]) % M

print(ans)
