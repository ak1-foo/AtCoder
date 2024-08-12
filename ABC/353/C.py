# TLE
N = int(input())
A = list(map(int, input().split()))

def f(x, y):
    return (x + y) % (10 ** 8)

sum = 0
for i in range(N-1):
    for j in range(i+1, N):
        sum += f(A[i], A[j])

print(sum)
