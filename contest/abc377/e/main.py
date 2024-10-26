# WA
N, K = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    P[i] -= 1

for _ in range(K % N):
    copy = P[:]
    for i in range(N):
        P[i] = copy[copy[i]]

print(*[x + 1 for x in P])

# 54312 3確定
# 21354
# 12345
# 12345
