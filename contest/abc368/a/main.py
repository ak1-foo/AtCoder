N, K = map(int, input().split())
A = list(map(int, input().split()))

took_cards = A[:-K]
del A[:-K]
A.extend(took_cards)

print(*A)
