N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

a_idx = -1
b_idx = -1
buyed = False
for i in range(N):
    if not buyed and i == N-1:
        print(A[0])
        exit()
    if A[a_idx] > B[b_idx]:
        if buyed:
            print(-1)
            exit()
        buyed = True
        ans = A[b_idx]
        b_idx += 1

    a_idx -= 1
    b_idx -= 1

print(ans)
