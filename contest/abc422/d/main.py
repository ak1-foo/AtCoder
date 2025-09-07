N, K = map(int, input().split())

base = K // (2**N)

segtree_sum = [[] for _ in range(N + 1)]
for i in range(N + 1):
    segtree_sum[i] = [base * (2 ** (N - i)) for _ in range(2 ** (i))]

remain = K % (2**N)
while remain > 0:
    remain -= 1
    pos = 0
    for i in range(0, N):
        segtree_sum[i][pos] += 1
        left_val = segtree_sum[i + 1][pos * 2]
        right_val = segtree_sum[i + 1][pos * 2 + 1]
        if left_val <= right_val:
            pos = pos * 2
        else:
            pos = pos * 2 + 1
    segtree_sum[N][pos] += 1


U = -1
if all(x == segtree_sum[-1][0] for x in segtree_sum[-1]):
    U = 0
else:
    U = 1
print(U)

print(*segtree_sum[-1])
