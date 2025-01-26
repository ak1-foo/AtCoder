A = list(map(int, input().split()))

target = [
    [2, 1, 3, 4, 5],
    [1, 3, 2, 4, 5],
    [1, 2, 4, 3, 5],
    [1, 2, 3, 5, 4],
]

if A in target:
    print("Yes")
else:
    print("No")
