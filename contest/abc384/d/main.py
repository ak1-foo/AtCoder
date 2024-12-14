from collections import deque

N, S = map(int, input().split())
A = list(map(int, input().split()))

S %= sum(A)
AA = A + A


# 尺取法
q = deque()
sum_part = 0
for a in AA:
    q.append(a)
    sum_part += a
    while sum_part > S:
        sum_part -= q.popleft()

    if sum_part == S:
        print("Yes")
        exit()

print("No")
