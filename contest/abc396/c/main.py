N, M = map(int, input().split())

B = list(map(int, input().split()))
B.sort(reverse=True)
B_pos = [b for b in B if b >= 0]
B_neg = [b for b in B if b < 0]
W = list(map(int, input().split()))
W.sort(reverse=True)
W_pos = [w for w in W if w >= 0]
W_neg = [w for w in W if w < 0]

ans = 0
ans += sum(B_pos)
if len(B_pos) >= len(W_pos):
    ans += sum(W_pos)
else:
    ans += sum(W_pos[: len(B_pos)])
    W_remain = W_pos[len(B_pos) :] + W_neg
    for i in range(min(len(B_neg), len(W_remain))):
        if B_neg[i] + W_remain[i] > 0:
            ans += B_neg[i] + W_remain[i]

print(ans)
