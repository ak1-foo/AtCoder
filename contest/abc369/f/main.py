# TLE
H, W, N = map(int, input().split())

grid = [[0] * W for _ in range(H)]
for _ in range(N):
    h, w = map(int, input().split())
    grid[h-1][w-1] = 1



import copy

dp = [[copy.deepcopy([0, '']) for _ in range(W)] for _ in range(H)]

for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            dp[h][w][0] = grid[h][w]
        elif h == 0:
            dp[h][w][0] = dp[h][w-1][0] + grid[h][w]
            dp[h][w][1] = dp[h][w-1][1] + 'R'
        elif w == 0:
            dp[h][w][0] = dp[h-1][w][0] + grid[h][w]
            dp[h][w][1] = dp[h-1][w][1] + 'D'
        else:
            if dp[h-1][w][0] > dp[h][w-1][0]:
                dp[h][w][0] = dp[h-1][w][0] + grid[h][w]
                dp[h][w][1] = dp[h-1][w][1] + 'D'
            else:
                dp[h][w][0] = dp[h][w-1][0] + grid[h][w]
                dp[h][w][1] = dp[h][w-1][1] + 'R'

print(dp[-1][-1][0])
print(dp[-1][-1][1])