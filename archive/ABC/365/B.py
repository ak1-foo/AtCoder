N = int(input())
A = list(map(int, input().split()))

A_with_index = [{"value": a, "index": i+1} for i, a in enumerate(A)]

A_with_index.sort(key=lambda a: a["value"])

print(A_with_index[-2]["index"])
