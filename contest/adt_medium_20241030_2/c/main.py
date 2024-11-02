N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [{'index': i, 'value': v} for i, v in enumerate(A)]
B = [{'index': i, 'value': v} for i, v in enumerate(B)]
sum = [{'index': i, 'value': A[i]['value'] + B[i]['value']} for i in range(N)]

A.sort(key=lambda x: x['value'], reverse=True)
B.sort(key=lambda x: x['value'], reverse=True)
sum.sort(key=lambda x: x['value'], reverse=True)

is_passed = [False] * N

# A, X
passed_count = 0
i = -1
while passed_count < X and i < N-1:
    i += 1
    if is_passed[A[i]['index']]:
        continue
    is_passed[A[i]['index']] = True
    passed_count += 1

# B, Y
passed_count = 0
i = -1
while passed_count < Y and i < N-1:
    i += 1
    if is_passed[B[i]['index']]:
        continue
    is_passed[B[i]['index']] = True
    passed_count += 1

# sum, Z
passed_count = 0
i = -1
while passed_count < Z and i < N-1:
    i += 1
    if is_passed[sum[i]['index']]:
        continue
    is_passed[sum[i]['index']] = True
    passed_count += 1

# print
for i in range(N):
    if is_passed[i]:
        print(i+1)
