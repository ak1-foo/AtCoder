A, B = map(int, input().split())

ans = 0
suspects = {1, 2, 3}

if A == B:
    ans = -1
else:
    suspects.remove(A)
    suspects.remove(B)
    ans = suspects.pop()

print(ans)
