N = int(input())
A = list(map(int, input().split()))
A = [a-1 for a in A]

last_index = {}
B = []
for i, a in enumerate(A):
    if a in last_index:
        B.append(last_index[a])
    else:
        B.append(-1)
    last_index[a] = i

for i, b in enumerate(B):
    if b != -1:
        B[i] = b + 1

print(*B)
