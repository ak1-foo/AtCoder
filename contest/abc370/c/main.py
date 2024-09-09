S = input()
T = input()

X = []

bigger_change_idx = []
smaller_change_idx = []
for i in range(len(S)):
    if S[i] > T[i]:
        smaller_change_idx.append(i)
    elif S[i] < T[i]:
        bigger_change_idx.append(i)

tmp = list(S)
for s in smaller_change_idx:
    tmp[s] = T[s]
    X.append(''.join(tmp))

bigger_change_idx.sort(reverse=True)
for b in bigger_change_idx:
    tmp[b] = T[b]
    X.append(''.join(tmp))

print(len(X))
for x in X:
    print(x)
