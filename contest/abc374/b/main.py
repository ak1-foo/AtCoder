S = input()
T = input()

min_len = min(len(S), len(T))

for i in range(min_len):
    if S[i] != T[i]:
        print(i + 1)
        exit()

if len(S) != len(T):
    print(min_len + 1)
else:
    print(0)
