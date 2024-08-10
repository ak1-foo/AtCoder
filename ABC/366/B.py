N = int(input())
S = [input() for _ in range(N)]

# '*'を埋める
for i in range(len(S)-1):
    if (len(S[i]) > len(S[i+1])):
        for _ in range(len(S[i]) - len(S[i+1])):
            S[i+1] += ('*')

# ' 'を埋める
max_len = len(max(S, key=lambda x: len(x)))
for i in range(len(S)):
    whitespace = max_len - len(S[i])
    S[i] += (' ') * whitespace

S.reverse()


# print
for i in range(max_len):
    for j in range(len(S)):
        print(S[j][i], end='')
    print()
