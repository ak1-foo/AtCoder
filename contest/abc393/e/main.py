# WA
N, K = map(int, input().split())
A = list(map(int, input().split()))

maxA = max(A)

count = [0] * (int(maxA**0.5) + 1)

for num in A:
    for i in range(1, int(maxA**0.5) + 1):
        if num % i == 0:
            count[i] += 1

for i in range(N):
    divs = set()
    for j in range(1, int(A[i] ** 0.5) + 1):
        if A[i] % j == 0:
            divs.add(j)
            divs.add(A[i] // j)
    ans = 1
    for div in divs:
        if count[div] >= K:
            ans = max(ans, div)
    print(ans)
