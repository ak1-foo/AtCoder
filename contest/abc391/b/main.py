N, M = map(int, input().split())

S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

for sraw in range(N - M + 1):
    for scol in range(N - M + 1):
        is_match = True
        for traw in range(M):
            if S[sraw + traw][scol : scol + M] != T[traw]:
                is_match = False
                break

        if is_match:
            print(sraw + 1, scol + 1)
            exit()
