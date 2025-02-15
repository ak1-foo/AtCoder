N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
prev = 0
for i in range(M):
    next = A[i]
    ans.append(list(range(prev + 1, next)))
    prev = next

ans.append(list(range(prev + 1, N + 1)))

new_ans = []
for a in ans:
    new_ans.extend(a)
ans = new_ans

print(len(ans))
print(*ans)
