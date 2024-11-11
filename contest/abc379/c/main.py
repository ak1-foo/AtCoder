N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# Xでソート
embed = sorted(list(zip(X, A)), key=lambda x: x[0])
X = [x[0] for x in embed]
A = [x[1] for x in embed]

if X[0] != 1:
    print(-1)
    exit()

ans = 0
remain = 0
for i in range(M):
    if i == M-1:
        target_idx = N+1
    else:
        target_idx = X[i+1]

    # 残る石の数を計算
    remain += A[i] - (target_idx - X[i])
    if remain < 0:
        print(-1)
        exit()

    # 何回操作するか計算
    width = target_idx - X[i] - 1
    ans += (width + 1) * remain +  width * (width + 1) // 2

if remain != 0:
    print(-1)
    exit()
print(ans)
