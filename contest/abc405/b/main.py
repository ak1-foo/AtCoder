N, M = map(int, input().split())
A = list(map(int, input().split()))

first_appear_idx = [-1] * (M + 1)
first_appear_idx[0] = 0

for i in range(N):
    if first_appear_idx[A[i]] == -1:
        first_appear_idx[A[i]] = i

if -1 in first_appear_idx:
    ans = 0
else:
    ans = N - max(first_appear_idx)

print(ans)
