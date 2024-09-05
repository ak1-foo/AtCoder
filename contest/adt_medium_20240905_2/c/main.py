height, width = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(height)]

S = [[0] * width for _ in range(height)]

for h in range(height):
    for w in range(width):
        if A[h][w] == 0:
            S[h][w] = '.'
        else:
            S[h][w] = chr(ord('A') + A[h][w] - 1)

for h in range(height):
    print(''.join(S[h]))
