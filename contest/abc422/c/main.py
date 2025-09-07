T = int(input())

for _ in range(T):
    na, nb, nc = map(int, input().split())
    if nb >= na or nb >= nc:
        ans = min(na, nc)
        print(ans)
        continue

    ans = nb
    na -= nb
    nc -= nb
    if max(na, nc) >= 2 * min(na, nc):
        ans += min(na, nc)
    else:
        ans += (na + nc) // 3
    print(ans)
