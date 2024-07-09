N, K, X = map(int, input().split())
An = list(map(int, input().split()))

An.insert(K, X)

for Ai in An:
    print(Ai, end=' ')
