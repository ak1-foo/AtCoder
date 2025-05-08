N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def rotate_90(S):
    N = len(S)
    S_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            S_90[j][N - 1 - i] = S[i][j]
    return S_90


S_90 = rotate_90(S)
S_180 = rotate_90(S_90)
S_270 = rotate_90(S_180)


count = [0, 1, 2, 3]
for c, s in enumerate([S, S_90, S_180, S_270]):
    for i in range(N):
        for j in range(N):
            if s[i][j] != T[i][j]:
                count[c] += 1

print(min(count))
