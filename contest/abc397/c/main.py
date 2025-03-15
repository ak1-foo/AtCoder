N = int(input())
A = list(map(int, input().split()))

types_left = [0] * (N - 1)
types_right = [0] * (N - 1)

types = {}
for i in range(N - 1):
    types[A[i]] = types.get(A[i], 0) + 1
    types_left[i] = len(types)

types = {}
for i in range(N - 1):
    types[A[N - 1 - i]] = types.get(A[N - 1 - i], 0) + 1
    types_right[i] = len(types)

ans = 0
for i in range(N - 1):
    ans = max(ans, types_left[i] + types_right[N - i - 2])

print(ans)
