N, K = map(int, input().split())

A = []
newest_sum_K = 0
for i in range(N + 1):
    if 0 <= i < K:
        A.append(1)
        newest_sum_K = (newest_sum_K + 1) % (10**9)
    elif K <= i:
        A.append(newest_sum_K)
        newest_sum_K = (newest_sum_K * 2 - A[i - K]) % (10**9)

ans = A[N] % (10**9)
print(ans)
