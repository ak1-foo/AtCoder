# TLE

N = int(input())

A = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = list(map(int, input().split()))


Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]


for q in queries:
    sum = 0
    for x in range(q[0]-1, q[1]):
        for y in range(q[2]-1, q[3]):
            for z in range(q[4]-1, q[5]):
                sum += A[x][y][z]

    print(sum)
