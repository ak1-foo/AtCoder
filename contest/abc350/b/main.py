N, Q = map(int, input().split())
T = list(map(int, input().split()))

teeth = [True] * N
for t in T:
    teeth[t-1] = not teeth[t-1]

print(sum(teeth))
