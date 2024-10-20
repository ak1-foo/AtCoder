N = int(input())
A = list(map(int, input().split()))
A = [a-1 for a in A]

operation = []
for i in range(N):
    while A[i] != i:
        operation.append(sorted((i+1, A[i]+1)))
        tmp = A[i]
        A[i] = A[A[i]]
        A[tmp] = tmp


print(len(operation))
for o in operation:
    print(*o)
