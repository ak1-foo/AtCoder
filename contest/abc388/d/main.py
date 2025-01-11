# WA

N = int(input())
A = list(map(int, input().split()))

B = []  # tmp
for i, d in enumerate(range(-N + 1, N, 2)):
    B.append(A[i] + d)

delta = [0] * (N + 1)
for i, b in enumerate(B):
    if b < 0:
        start = max(0, i + b + 1)
        delta[start] += 1
        delta[i + 1] -= 1

ans = []
current = 0
for i in range(N):
    current += delta[i]
    ans.append(current)
