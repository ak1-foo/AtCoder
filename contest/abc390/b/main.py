N = int(input())
A = list(map(int, input().split()))

for i in range(2, N):
    if A[i] * A[i - 2] != A[i - 1] ** 2:
        print("No")
        exit()

print("Yes")
