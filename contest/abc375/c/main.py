N = int(input())

A = []
for _ in range(N):
    A.append(input())

B = [[' '] * N for _ in range(N)]

A_90 = [[' '] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_90[j][N-1-i] = A[i][j]

A_180 = [[' '] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_180[j][N-1-i] = A_90[i][j]

A_270 = [[' '] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_270[j][N-1-i] = A_180[i][j]

for i in range(N):
    for j in range(N):
        min_ij = min(i, j, N-1-i, N-1-j)
        if min_ij % 4 == 0:
            B[i][j] = A_90[i][j]
        elif min_ij % 4 == 1:
            B[i][j] = A_180[i][j]
        elif min_ij % 4 == 2:
            B[i][j] = A_270[i][j]
        elif min_ij % 4 == 3:
            B[i][j] = A[i][j]


for b in B:
    print(*b, sep='')
