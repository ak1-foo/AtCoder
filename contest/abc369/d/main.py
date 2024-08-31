N = int(input())
A = list(map(int, input().split()))

# dp[0][i] i番目までのモンスターを対応し、次のモンスターを倒すとき、ボーナスが得られる状態の最大値
# dp[1][i] i番目までのモンスターを対応し、次のモンスターを倒すとき、ボーナスが得られない状態の最大値
dp = [[0] * 2 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[0][0] = A[0]
        dp[0][1] = 0
    else:
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + A[i])
        dp[i][1] = max(dp[i-1][0] + A[i]*2, dp[i-1][1])

print(max(dp[-1]))