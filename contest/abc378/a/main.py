A = list(map(int, input().split()))

count = {}
for a in A:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

ans = 0
for v in count.values():
    ans += v // 2

print(ans)
