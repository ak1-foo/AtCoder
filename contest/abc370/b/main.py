N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 0-indexedにするため、Aの値をすべて-1する
A = [[A[i][j] - 1 for j in range(i+1)] for i in range(N)]

current = 0
for i in range(N):
    if current >= i:
        current = A[current][i]
    else:
        current = A[i][current]

# 1-indexedに戻す
ans = current + 1
print(ans)
