N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(N + 1):
    geq = [x for x in A if x >= i]
    if len(geq) >= i:
        ans = i

print(ans)
