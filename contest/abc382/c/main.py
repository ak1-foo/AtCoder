N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

B = list(map(int, input().split()))
B = [b - 1 for b in B]

# 美味しさによって、食べる人を決めるためのリストを作成
who_eat = [-1] * (2 * (10**5))
for i in range(N):
    j = 0
    while A[i] + j < len(who_eat) and who_eat[A[i] + j] == -1:
        who_eat[A[i] + j] = i
        j += 1

# 回答
for b in B:
    if who_eat[b] == -1:
        ans = -1
    else:
        ans = who_eat[b] + 1

    print(ans)
