S = input()
T = input()

idx = 0
for s in S:
    while s != T[idx]:
        idx += 1
    print(idx+1, end=" ")
    idx += 1
